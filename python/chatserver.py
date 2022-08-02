from cgitb import text
from concurrent import futures
import logging

import const #- addresses, port numbers etc. (a rudimentary way to replace a proper naming service)

import grpc
import ChatService_pb2
import ChatService_pb2_grpc

class ChatServer(ChatService_pb2_grpc.ChatServerServicer):

    def __init__(self):
        self.chats = []

    def RelayMessage(self, request, context):
        lastindex = 0
        while True:
            while len(self.chats) > lastindex:
                n = self.chats[lastindex]

                # Check that the destination exists
                try:
                    dest_addr = const.registry[n.nameRecipient] # get address of destination in the registry
                except:
                    print ("Error: Destination client does not exist") # to do: send a proper error code
                
                dest_ip = dest_addr[0]
                dest_port = dest_addr[1]
                
                if dest_ip == request.ip and dest_port == request.port:
                    lastindex += 1
                    yield n
                

    def SendMessage(self, request, context):
        print("RELAYING MSG: " + request.text + " - FROM: " + request.nameSender + " - TO: " + request.nameRecipient) 
        # just print the message and destination
        self.chats.append(request)
        return ChatService_pb2.EmptyMessage()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ChatService_pb2_grpc.add_ChatServerServicer_to_server(ChatServer(), server)
    server.add_insecure_port('[::]:5001')
    print("Chat Server is ready...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
