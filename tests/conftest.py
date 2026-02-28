import grpc
import pytest
import time
from concurrent import futures

import vault_pb2_grpc
from app.grpc.vault_servicer import VaultServicer
from app.services.vault_service import VaultService
from app.retrieval.retriever import Retriever
from app.indexing.index_pipeline import IndexPipeline


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


@pytest.fixture(scope="session")
def grpc_test_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))

    embedder = DummyEmbedder()
    vector_store = DummyVectorStore()
    retriever = Retriever(embedder, vector_store)
    index_pipeline = IndexPipeline()

    service = VaultService(retriever, index_pipeline)

    vault_pb2_grpc.add_VaultServiceServicer_to_server(
        VaultServicer(service),
        server
    )

    port = server.add_insecure_port("localhost:0")
    server.start()

    yield port   

    server.stop(0)