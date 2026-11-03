# Week 1: Achour Nazim

Track: A
Kernel on the host (uname -r): 6.18.54.1-microsoft-standard-WSL2
Kernel inside the alpine container (uname -r): 6.18.54.1-microsoft-standard-WSL2
RAM and CPU cores (free -h, nproc):
free -h:
               total        used        free      shared  buff/cache   available
Mem:            15Gi       1.0Gi        13Gi        50Mi       1.6Gi        14Gi
Swap:          4.0Gi          0B       4.0Gi

nproc: 22

## Security questions

1. the alpine container may look like an independent linux system, but the OS stays the same. for security, it matters >

2. -p 127.0.0.1:8080:80 only allows the host (me) to access, whereas -p 8080:80 allows other machines

3. potential download of a malicious file

4. because the host is giving said user the privileges to act as root (?)

5. there is only one token per repository and can only be seen once, a password can be easily hacked through guessing o>
