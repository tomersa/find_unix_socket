# find_unix_socket
Instead of getting a unix socket by running:
$ netstat -xp | grep <socket name>

This script does it searching for the socket under /proc directory. 

In the 1st terminal run:
`$ bind_socket.py test` - Will create a socket named `test` and wait on it forever.

In the 2nd terminal run:
`$ find_socket.py test` - The program will return the pid(process id) of the process holding the socket. 

You may verify this by running:
`ps aux | grep <pid>` and see it is acctualy the same process id in the output of `netstat -xp | grep test`


The idea for this project came up by looking at the netstat source code. Which can be found here: [netstat.c](https://github.com/ecki/net-tools/blob/master/netstat.c)
