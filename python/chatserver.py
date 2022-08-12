from concurrent import futures
import logging
import const
import grpc
import ChatService_pb2 as svc
import ChatService_pb2_grpc as svc_grpc

class ChatServer(svc_grpc.ChatServerServicer):

    def __init__(self):
        self.chatsRelaying = []
        self.chatsWaiting = []

    def RelayMessage(self, request, context):
        while True:
            auxChats = self.chatsWaiting
            for c in auxChats:
                self.chatsWaiting.remove(c)
                self.chatsRelaying.append(c)
            auxChats = self.chatsRelaying
            for c in self.chatsRelaying:
                dest_addr = const.registry[c.nameDestination]
                dest_ip = dest_addr[0]
                dest_port = dest_addr[1]
                if dest_ip == request.ip and dest_port == request.port:
                    auxChats.remove(c)
                    yield c
            self.chatsRelaying = auxChats    

    def SendMessage(self, request, context):
        print("RELAYING MSG: " + request.text + " - FROM: " + request.nameSender + " - TO: " + request.nameDestination)
        try:
            const.registry[request.nameDestination]
        except:
            return svc.Confirmation(confirmation = False)
        else:
            self.chatsWaiting.append(request)
            return svc.Confirmation(confirmation = True)
        

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    svc_grpc.add_ChatServerServicer_to_server(ChatServer(), server)
    server.add_insecure_port('[::]:5001')
    print("Chat Server is ready...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
