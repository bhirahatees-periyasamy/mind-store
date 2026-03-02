import vault_pb2
import vault_pb2_grpc
from app.services.vault_service import VaultService


class VaultServicer(vault_pb2_grpc.VaultServiceServicer):

    def __init__(self, service: VaultService):
        self.service = service

    def Health(self, request, context):
        result = self.service.health()
        return vault_pb2.HealthResponse(status=result)

    def Search(self, request, context):
        results = self.service.search(request.query, request.k)

        return vault_pb2.SearchResponse(
            results=[
                vault_pb2.SearchResult(
                    content=r["content"],
                    path=r["path"],
                    score=r["score"]
                )
                for r in results
            ]
        )

    def Index(self, request, context):
        status = self.service.index(request.path)
        return vault_pb2.IndexResponse(status=status)