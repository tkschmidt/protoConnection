package pkg

import (
	"context"
	"github.com/tkschmidt/protoConnection/pkg/protobuf/generate_golang/example"
)

type server struct {
	example.UnimplementedSampleServiceServer
}

func (s *server) Predict(context.Context, *example.PredictRequest) (*example.PredictResponse, error){
	ary := make([]float32, 3)
	return &example.PredictResponse{Value: ary}, nil

}