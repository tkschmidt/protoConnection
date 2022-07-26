
PROTOC_OPTS_GRPC= --go-grpc_out=generate_golang
PROTOC_OPTS= --go_out=generate_golang
PROTOC_OPTS_GRPC_PY= --python-grpc_out=generate_golang
PROTOC_OPTS_PY= --python_out=generate_golang
GO_IMPORT_PATH=github.com/tkschmidt/protoConnection/pkg/protobuf/generate_golang



all_in_one:
	mkdir -p all_in_one
	protoc --go-grpc_out=all_in_one \
	   --go_out=all_in_one	-I ./ \
        --go-grpc_opt=paths=import \
        --go-grpc_opt=module=${GO_IMPORT_PATH} \
		--go-grpc_opt=Mexample.proto=${GO_IMPORT_PATH}/example \
        --go_opt=paths=import \
        --go_opt=module=${GO_IMPORT_PATH} \
		--go_opt=Mexample.proto=${GO_IMPORT_PATH}/example \
		 --openapiv2_out all_in_one \
         --openapiv2_opt logtostderr=true \
		--openapiv2_opt=Mexample.proto=${GO_IMPORT_PATH}/example \
         --openapiv2_opt generate_unbound_methods=true \
         example.proto


generate_golang:
	mkdir -p generate_golang
	protoc $(PROTOC_OPTS_GRPC) -I ./ \
        --go-grpc_opt=paths=import \
        --go-grpc_opt=module=${GO_IMPORT_PATH} \
		--go-grpc_opt=Mexample.proto=${GO_IMPORT_PATH}/example \
         example.proto
	protoc $(PROTOC_OPTS) -I ./ \
        --go_opt=paths=import \
        --go_opt=module=${GO_IMPORT_PATH} \
		--go_opt=Mexample.proto=${GO_IMPORT_PATH}/example \
         example.proto

generate_python:
	mkdir -p generate_python
	python3 -m grpc_tools.protoc --python_out=generate_python --grpc_python_out=generate_python -I ./ \
         example.proto

