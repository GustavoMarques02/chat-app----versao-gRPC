# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ChatService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x43hatService.proto\x12\x0c\x63hat_service\"B\n\x07Message\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x15\n\rnameRecipient\x18\x02 \x01(\t\x12\x12\n\nnameSender\x18\x03 \x01(\t\"%\n\tRecipient\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\t\"\x0e\n\x0c\x45mptyMessage2\x94\x01\n\nChatServer\x12\x42\n\x0bSendMessage\x12\x15.chat_service.Message\x1a\x1a.chat_service.EmptyMessage\"\x00\x12\x42\n\x0cRelayMessage\x12\x17.chat_service.Recipient\x1a\x15.chat_service.Message\"\x00\x30\x01\x42\x37\n\x1bio.grpc.examples.iotserviceB\x0fIoTServiceProtoP\x01\xa2\x02\x04TEMPb\x06proto3')



_MESSAGE = DESCRIPTOR.message_types_by_name['Message']
_RECIPIENT = DESCRIPTOR.message_types_by_name['Recipient']
_EMPTYMESSAGE = DESCRIPTOR.message_types_by_name['EmptyMessage']
Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'ChatService_pb2'
  # @@protoc_insertion_point(class_scope:chat_service.Message)
  })
_sym_db.RegisterMessage(Message)

Recipient = _reflection.GeneratedProtocolMessageType('Recipient', (_message.Message,), {
  'DESCRIPTOR' : _RECIPIENT,
  '__module__' : 'ChatService_pb2'
  # @@protoc_insertion_point(class_scope:chat_service.Recipient)
  })
_sym_db.RegisterMessage(Recipient)

EmptyMessage = _reflection.GeneratedProtocolMessageType('EmptyMessage', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYMESSAGE,
  '__module__' : 'ChatService_pb2'
  # @@protoc_insertion_point(class_scope:chat_service.EmptyMessage)
  })
_sym_db.RegisterMessage(EmptyMessage)

_CHATSERVER = DESCRIPTOR.services_by_name['ChatServer']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033io.grpc.examples.iotserviceB\017IoTServiceProtoP\001\242\002\004TEMP'
  _MESSAGE._serialized_start=35
  _MESSAGE._serialized_end=101
  _RECIPIENT._serialized_start=103
  _RECIPIENT._serialized_end=140
  _EMPTYMESSAGE._serialized_start=142
  _EMPTYMESSAGE._serialized_end=156
  _CHATSERVER._serialized_start=159
  _CHATSERVER._serialized_end=307
# @@protoc_insertion_point(module_scope)
