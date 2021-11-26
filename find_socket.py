#!/usr/bin/env python3
import os
import sys
import glob

assert len(sys.argv) == 2, f'Usage: {sys.argv[0]} <socket name>'
socket_name = sys.argv[1]

def find_socket_inode() -> None:
    with open('/proc/net/unix') as f:
        for line in f.readlines():
            if socket_name in line:
                return line.split(' ')[6]
    raise Exception(f'Couldnt find inode associated with socket {socket_name}.')

def find_proccess_by_inode(socket_inode: str) -> None:
    for f in glob.glob('/proc/[0-9]*/fd/*', recursive=False):
        try:
            if socket_inode in os.readlink(f):
                return f.split('/')[2]
        except FileNotFoundError:
            pass # Sometimes file descriptors or process already closed so in that case the file won't be found. So we can skip.

    print(f'Couldnt find process holding the socket with inode: {socket_inode}')

if __name__ == "__main__":
    socket_inode = find_socket_inode()
    proc_file = find_proccess_by_inode(socket_inode)
    print(proc_file)
            
