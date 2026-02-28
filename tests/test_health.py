
import grpc
import vault_pb2
import vault_pb2_grpc


def test_health(grpc_test_server):
    channel = grpc.insecure_channel(f"localhost:{grpc_test_server}")
    stub = vault_pb2_grpc.VaultServiceStub(channel)

    response = stub.Health(vault_pb2.HealthRequest())

    assert response.status == True