'''
    Simple socket server using threads for chatting
    v1.0
'''
import socket
import sys
from _thread import * 
#======================================================================
#
#   Here set variables for your server.
#   HOST - on which device server should be, left empty
#          leaves it everywhere, it's better to not
#          change that
#   PORT - on which port server should listen.
#          8888 by default
#   PASS - password to type to connect to server, it's
#          better to change it. When this is a public
#          server, you can leave empty.
#   ADMPASS - password to type to connect with full
#             access. It's recommended to change it.
#   NAME - name of the server displayed in the hello
#          message to clients
#
#=====================================================================
HOST = ''
PORT = 8888
PASS = ''
ADMPASS = 'password'
NAME = 'Sample Server'
def strToBytes(strToConvert):
    return str.encode(strToConvert, 'UTF-8')
def bytesToStr(dataToConvert):
    return str(dataToConvert, 'UTF-8')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
try:
    s.bind((HOST, PORT))
except socket.error as err:
    raise err
    sys.exit()
print('Socket bind complete')
s.listen(10)
print('Socket now listening')
#======================================================================
#
#    Commands:
#    /help - shows help
#    /nick <newnick> - changes nick
#    /admin <password> - gives admin previleges
#    /m <nick> <message> - tells another user
#    /quit - exits server
#
#    Admin commands(allowed only when authorized with '/admin'):
#    /mute <nick> - mutes user with this nick
#    /kick <nick> - kicks user with this nick
#    /ban <nick> - bans this nick until stopping server
#    /quit quiet - exits server without showing message
#    /quit noquit - displays message about quitting, but doesn't quit
#    /status - shows list of connected users, threir ip, port and nicks
#
#======================================================================
def commandfind(recieved):
	if recieved.startswith("/help"):
		
def clientthread(conn):
    txxt='Welcome to the '+NAME+'. Type password and hit enter\n'
    conn.send(strToBytes(txxt))
    data = conn.recv(1024)
    while not PASS == bytesToStr(data):
		conn.send(strToBytes('Wrong password. Try again.\n'))
		data = conn.recv(1024)
	conn.send(strToBytes('Connected. Type nick you want to recieve now.\n'))
    nick=bytesToStr(conn.recv(1024))
    conn.send(strToBytes('Nick set to '+nick+'. Type /help for help. Begin chatting!\n'))
    while True:
        data = conn.recv(1024)
        datatext = bytesToStr(data)
        reply = 'OK...' + datatext
        if not data: 
            break
        conn.sendall(strToBytes(reply))
    conn.close()
while True:
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    start_new_thread(clientthread ,(conn,))
s.close()
