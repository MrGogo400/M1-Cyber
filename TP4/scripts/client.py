#!/bin/python3

import socket
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-a', '--host', type=str, help='address of the host')
    parser.add_argument('-p', '--port', type=int, help='port')
    parser.add_argument('-pt', '--protocol', type=str, help='protocol (TCP or UDP)')
    args = parser.parse_args()
    return args

def tcp(args):
    """ TCP connection
    """
    try: 
        # Creation of the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((args.host, args.port))
        print("Connection on host {}, port {}".format(args.host, args.port), '\n')

        # Receive welcome 
        response = s.recv(1024)
        print("Server sent: ", response.decode(), '\n')

        while True:
                command = input("$>")
                if 'exit' in command:
                    s.send('exit'.encode())
                    break
                else:
                    s.send(command.encode())
                    response = s.recv(1024)
                    if response != "":
                        print(response.decode())

        print("Close session")
        s.close()
    except Exception as err:
        print(err)
        raise

def udp(args):
    """ UDP connection.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Connection on host {}, port {}".format(args.host, args.port), '\n')

        while True:
            msg = input("> ")

            if msg == "exit":
                s.sendto(msg.encode(), (args.host, args.port))
                s.close()
            else:
                s.sendto(msg.encode(), (args.host, args.port))

            (data, addr) = s.recvfrom(1024)
            print("Server {}, sent: {} ".format(addr[0], data.decode()))
        
        s.close()
    except Exception as err:
        print(err)
        raise

def main():
    try:
        args = parse_args()

        if args.protocol == "TCP":
            tcp(args)
        elif args.protocol == "UDP":
            udp(args)
        else:
            print("Error protocol. Choose between TCP or UDP")
            raise

    except Exception as err:
        print(err)
        raise

main()