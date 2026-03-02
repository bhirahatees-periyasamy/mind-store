

import grpc
import vault_pb2
import vault_pb2_grpc


def test_index(grpc_test_server):
    channel = grpc.insecure_channel(f"localhost:{grpc_test_server}")
    stub = vault_pb2_grpc.VaultServiceStub(channel)

    response = stub.Index(
        vault_pb2.IndexRequest(path="/tmp/repo")
    )

    assert response.status == True