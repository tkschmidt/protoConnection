# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rexample.proto\x12\x08tutorial\"%\n\x0ePredictRequest\x12\x13\n\x0binputString\x18\x01 \x03(\t\" \n\x0fPredictResponse\x12\r\n\x05value\x18\x01 \x03(\x02\x32O\n\rSampleService\x12>\n\x07Predict\x12\x18.tutorial.PredictRequest\x1a\x19.tutorial.PredictResponseb\x06proto3')



_PREDICTREQUEST = DESCRIPTOR.message_types_by_name['PredictRequest']
_PREDICTRESPONSE = DESCRIPTOR.message_types_by_name['PredictResponse']
PredictRequest = _reflection.GeneratedProtocolMessageType('PredictRequest', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTREQUEST,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.PredictRequest)
  })
_sym_db.RegisterMessage(PredictRequest)

PredictResponse = _reflection.GeneratedProtocolMessageType('PredictResponse', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTRESPONSE,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.PredictResponse)
  })
_sym_db.RegisterMessage(PredictResponse)

_SAMPLESERVICE = DESCRIPTOR.services_by_name['SampleService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PREDICTREQUEST._serialized_start=27
  _PREDICTREQUEST._serialized_end=64
  _PREDICTRESPONSE._serialized_start=66
  _PREDICTRESPONSE._serialized_end=98
  _SAMPLESERVICE._serialized_start=100
  _SAMPLESERVICE._serialized_end=179
# @@protoc_insertion_point(module_scope)