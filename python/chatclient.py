from __future__ import print_function
import threading
import logging
import sys

import const #- addresses, port numbers etc. (a rudimentary way to replace a proper naming service)

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
            self.conn.SendMessage(ChatService_pb2.Message(text = msg, nameRecipient = dest, nameSender = self.me))

    def __listen_for_messages(self):
        for message in self.conn.RelayMessage(ChatService_pb2.EmptyMessage()):
            print("MESSAGE: " + message.text + " - FROM: " + message.nameSender)       
        
if __name__ == '__main__':
    logging.basicConfig()
    c = Client()