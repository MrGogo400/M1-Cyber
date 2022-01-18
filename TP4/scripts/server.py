#!/bin/python3

import socket
import argparse
import os
import subprocess
import logging

def parse_args():
    """ Parse arguments
    """
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-a', '--host', type=str, help='address of the host')
    parser.add_argument('-p', '--port', type=int, help='port')
    parser.add_argument('-pt', '--protocol', type=str, help='protocol (TCP or UDP)')
    args = parser.parse_args()
    return args

def tcp(args):
    """ TCP server.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((args.host, args.port))
        s.listen(5)
        logging.info('Server TCP listening on port {}'.format(args.port))
        print("Listen on port {} ".format(args.port), '\n')

        choose_shell = True

        while choose_shell:
            shell = input("Choose shell: ")
            if shell not in ['/bin/bash', '/bin/sh']:
                print("bad shell")
                choose_shell = True
            else:
                choose_shell = False

        (clientsocket, address) = s.accept()
        logging.info('Client {} connect on the server TCP'.format(address))
        print("\n", "Connexion client : {}".format(address), '\n')
        print('Send a message to the client {} :'.format(address))
        clientsocket.send(input("> ").encode('utf-8'))

        while True:
            response = clientsocket.recv(1024)
            response = response.decode()

            if 'exit' in response:
                print("Close client session")
                logging.info('Client {} disconnect from the server'.format(address))
                clientsocket.close()
                break
            elif 'cd' in response:
                try:
                    if response == "cd":
                        clientsocket.send(" ".encode())
                    else:
                        dir = response.split(" ")
                        os.chdir(dir[1])
                        clientsocket.send(" ".encode())
                except FileNotFoundError as err:
                    clientsocket.send(str(err).encode())
                except Exception as err:
                    print(err)
                    raise
            else:
                sh = subprocess.Popen(response, shell=True, executable=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                clientsocket.send(sh.stdout.read())
                clientsocket.send(sh.stderr.read())

    except Exception as err:
        logging.error('Error: {}'.format(err))
        print(err)
        raise

def udp(args):
    """ UDP server.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((args.host, args.port))
        logging.info('Server UDP listening on port {}'.format(args.port))
        print("Listen on port {} ".format(args.port),'\n')

        while True:
            (data, client) = s.recvfrom(1024)
            print("Client ({}) sent: ".format(client[0]), data.decode())

            msg = input("> ")
            s.sendto(msg.encode(), client)
        
    except Exception as err:
        logging.error('Error: {}'.format(err))
        print(err)
        raise

def main():
    """ 
    """
    try:
        args = parse_args()
        logging.basicConfig(filename='log_server.log', level=logging.DEBUG)
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