import socket
import time # this is just to close the sever after 2 minutes

def socket_demo():
    target_host = 'chatgpt.com'

    ip  = socket.gethostbyname('chatgpt.com')
    print(ip)

    # AF_INET = transport mechanism  (IPv4)
    # SOCK_STREAM = connection oriented protocol (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind s to a port to listen 
    # use s to make an outbound connection 

    s.connect((target_host,80))

    s.sendall(b"HEAD /  HTTP/1.1\r\nHost: chatgpt.com\r\n\r\n")

    # receive the data from the server
    print(s.recv(1024).decode()) #1024 is the max bytes received at once.

    s.close() #close our connection

#socket_demo()

choice = input('Client = 1 \nServer = 2 \nWhat do you want to run? (1 or 2): ')

while (choice != '1') and (choice != '2'):
    choice = input('Client = 1 \nServer = 2 \nWhat do you want to run? (1 or 2): ')

client = False
server = False
if choice == '1':
    client = True
elif choice == '2':
    server = True


port = 8080
local_host = "127.0.0.7"
# make a new connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print
# Run a server
if server:
    # bind socket to speciffied adress
    s.bind((local_host, port))
    s.listen()
    start_time = time.time()
    while True: # waiting to make a connection
        connect, addr  = s.accept() #server will accept connection, returns new pair of socket object 
        connect.send(b"You made it to the socket :-) !")
        connect.close()
        # Check if 2 minutes have elapsed
        if time.time() - start_time >= 120:
            print("Server is shutting down...")
            s.close()
            break

if client:
    s.connect((local_host,port))
    print(s.recv(1024))
    s.close()
