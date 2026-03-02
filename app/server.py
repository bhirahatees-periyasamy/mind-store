import grpc
from concurrent import futures

import vault_pb2_grpc
import vault_pb2
from app.grpc.vault_servicer import VaultServicer
from app.services.vault_service import VaultService
from app.retrieval.retriever import Retriever
from app.indexing.index_pipeline import IndexPipeline

from grpc_reflection.v1alpha import reflection

class DummyEmbedder:
    def embed(self, texts):
        return [[0.1, 0.2, 0.3] for _ in texts]


class DummyVectorStore:
    def search(self, query_vector, k):
        return [
            {
                "content": "dummy snippet",
                "path": "src/auth.rs",
                "score": 0.91
            }
        ]


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    embedder = DummyEmbedder()
    vector_store = DummyVectorStore()
    retriever = Retriever(embedder, vector_store)

    index_pipeline = IndexPipeline()
    service = VaultService(retriever, index_pipeline)

    vault_pb2_grpc.add_VaultServiceServicer_to_server(
        VaultServicer(service),
        server
    )

    # Add reflection for grpcurl
    service_names = (
        vault_pb2.DESCRIPTOR.services_by_name['VaultService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(service_names, server)

    server.add_insecure_port("[::]:50051")
    server.start()
    print("Vault running on 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()