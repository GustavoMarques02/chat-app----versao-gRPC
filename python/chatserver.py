from concurrent import futures
import logging

import const #- addresses, port numbers etc. (a rudimentary way to replace a proper naming service)

import grpc
import chatserver_pb2
import chatserver_pb2_grpc

class chatserver(chatserver_pb2_grpc.chatserverServicer):
    
    def SendMessage(text, nameRecipient, nameSender):
        print("RELAYING MSG: " + text + " - FROM: " + nameSender + " - TO: " + nameRecipient) # just print the message and destination
        #
        # Check that the destination exists
        try:
            dest_addr = const.registry[nameRecipient] # get address of destination in the registry
        except:
            print ("Error: Destination client does not exist") # to do: send a proper error code
        #
        # Forward the message to the recipient client
        dest_ip = dest_addr[0]
        dest_port = dest_addr[1]
        

        return

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chatserver_pb2_grpc.add_chatserverServicer_to_server(chatserver(), server)
    server.add_insecure_port('[::]:50051')
    print("Chat Server is ready...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
