from concurrent import futures
import logging
import const
import grpc
import ChatService_pb2
import ChatService_pb2_grpc

class ChatServer(ChatService_pb2_grpc.ChatServerServicer):

    def __init__(self):
        self.chats = []

    def RelayMessage(self, request, context):
        while True:
            auxChats = self.chats
            for c in self.chats:
                dest_addr = const.registry[c.nameDestination]
                dest_ip = dest_addr[0]
                dest_port = dest_addr[1]
                if dest_ip == request.ip and dest_port == request.port:
                    auxChats.remove(c)
                    yield c
            self.chats = auxChats    

    def SendMessage(self, request, context):
        print("RELAYING MSG: " + request.text + " - FROM: " + request.nameSender + " - TO: " + request.nameDestination)
        try:
            const.registry[request.nameDestination]
        except:
            return ChatService_pb2.Confirmation(confimation = False)
        else:
            self.chats.append(request)
            return ChatService_pb2.Confirmation(confimation = True)
        

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
