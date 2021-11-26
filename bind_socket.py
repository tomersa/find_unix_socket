#!/usr/bin/env python3
import socket
import os
import sys
import time

if __name__ == "__main__":
    assert len(sys.argv) == 2, f'Usage: {sys.argv[0]} <socket name>'
    socket_name = sys.argv[1]
    
    server = socket.socket(socket.AF_UNIX)
    sock = server.bind(socket_name)
    while True:
        print(f'bounded to socket: {socket_name}')
        time.sleep(1)
