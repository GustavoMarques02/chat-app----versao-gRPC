# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ChatService_pb2 as ChatService__pb2


class ChatServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendMessage = channel.unary_unary(
                '/chat_service.ChatServer/SendMessage',
                request_serializer=ChatService__pb2.Message.SerializeToString,
                response_deserializer=ChatService__pb2.EmptyMessage.FromString,
                )
        self.RelayMessage = channel.unary_stream(
                '/chat_service.ChatServer/RelayMessage',
                request_serializer=ChatService__pb2.EmptyMessage.SerializeToString,
                response_deserializer=ChatService__pb2.Message.FromString,
                )


class ChatServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendMessage(self, request, context):
        """Send Message
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RelayMessage(self, request, context):
        """Relay Message
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessage,
                    request_deserializer=ChatService__pb2.Message.FromString,
                    response_serializer=ChatService__pb2.EmptyMessage.SerializeToString,
            ),
            'RelayMessage': grpc.unary_stream_rpc_method_handler(
                    servicer.RelayMessage,
                    request_deserializer=ChatService__pb2.EmptyMessage.FromString,
                    response_serializer=ChatService__pb2.Message.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'chat_service.ChatServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChatServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chat_service.ChatServer/SendMessage',
            ChatService__pb2.Message.SerializeToString,
            ChatService__pb2.EmptyMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RelayMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/chat_service.ChatServer/RelayMessage',
            ChatService__pb2.EmptyMessage.SerializeToString,
            ChatService__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
