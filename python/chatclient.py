from __future__ import print_function
import threading
import logging
import sys
import const
import grpc
import ChatService_pb2
import ChatService_pb2_grpc

class Client:
    
    def __init__(self):
        self.me = str(sys.argv[1])
        channel = grpc.insecure_channel(const.CHAT_SERVER_HOST+':'+const.CHAT_SERVER_PORT)
        self.conn = ChatService_pb2_grpc.ChatServerStub(channel)
        threading.Thread(target=self.__listen_for_messages).start()

        while True:
            dest = input("ENTER DESTINATION: ")
            msg = input("ENTER MESSAGE: ")
            message = ChatService_pb2.Message(text = msg, nameDestination = dest, nameSender = self.me)
            confimation = self.conn.SendMessage(message)
            if not confimation:
                print("Error: Destination does not exist\n")

    def __listen_for_messages(self):
        me_addr = const.registry[self.me]
        me_ip = me_addr[0]
        me_port = me_addr[1]
        for message in self.conn.RelayMessage(ChatService_pb2.Destination(ip = me_ip, port = me_port)):
            print("\nMESSAGE: " + message.text + " - FROM: " + message.nameSender + "\n")       
        
if __name__ == '__main__':
    logging.basicConfig()
    c = Client()