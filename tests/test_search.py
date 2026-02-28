

import grpc
import vault_pb2
import vault_pb2_grpc


def test_search(grpc_test_server):
    channel = grpc.insecure_channel(f"localhost:{grpc_test_server}")
    stub = vault_pb2_grpc.VaultServiceStub(channel)

    response = stub.Search(
        vault_pb2.SearchRequest(query="auth logic", k=5)
    )

    assert len(response.results) == 1
    assert response.results[0].content == "dummy snippet"
    assert response.results[0].path == "src/auth.rs"
    assert isinstance(response.results[0].score, float)