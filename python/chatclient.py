from __future__ import print_function
from cgitb import text
import logging
import sys

import const #- addresses, port numbers etc. (a rudimentary way to replace a proper naming service)

import grpc
import ChatService_pb2
import ChatService_pb2_grpc

def run():
    me = str(sys.argv[1]) # User's name (as registered in the registry. E.g., Alice, Bob, ...)
    while True:
        dest = input("ENTER DESTINATION: ")
        msg = input("ENTER MESSAGE: ")
        with grpc.insecure_channel(const.CHAT_SERVER_HOST+':'+const.CHAT_SERVER_PORT) as channel:
            stub = ChatService_pb2_grpc.ChatServerStub(channel)
            stub.SendMessage(ChatService_pb2.Message(text = msg, nameRecipient = dest, nameSender = me))

if __name__ == '__main__':
    logging.basicConfig()
    run()