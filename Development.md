### For building the proto buff

```bash
python -m grpc_tools.protoc \
    -I=proto \
    --python_out=. \
    --grpc_python_out=. \
    proto/vault.proto

```