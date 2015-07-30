'''
    Simple socket server using threads
'''
 
import socket
import sys
from _thread import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

# Tu dodałem funkcyjki tłumaczące dane na string,
# w przykładzie był python 2, a w nim dane są auto
# matycznie tłumaczone, w pythonie 3 już tak nie jest.
# dodałem też obsługę polskich znaków i tyle.

def strToBytes(strToConvert):
    return str.encode(strToConvert, 'UTF-8')
def bytesToStr(dataToConvert):
    return str(dataToConvert, 'UTF-8')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as err:
    raise err
    sys.exit()
     
print('Socket bind complete')
 
#Start listening on socket
s.listen(10)
print('Socket now listening')
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    txxt='Welcome to the server. Type something and hit enter\n'
    conn.send(strToBytes(txxt)) #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = conn.recv(1024)
        datatext = bytesToStr(data)
        reply = 'OK...' + datatext
        if not data: 
            break
     
        conn.sendall(strToBytes(reply))
     
    #came out of loop
    conn.close()
 
#now keep talking with the client
while True:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
 
s.close()
