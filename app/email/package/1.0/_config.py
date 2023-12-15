import socket
import time

import handle_config
import email_socket




def sign_in_to_server__tail(sock : socket) :
    time.sleep(0.01)
    msg = 'STAT' 
    email_socket.send_to_server(sock, msg)
    
    time.sleep(0.01)
    msg = 'QUIT'
    email_socket.send_to_server(sock, msg)    


def sign_in_to_server(sock : socket) :
    # while True :
    time.sleep(0.01)
    msg = 'CAPA' 
    email_socket.send_to_server(sock, msg)
    
    time.sleep(0.01)
    msg = 'USER ' + handle_config.get_pop3('username')
    email_socket.send_to_server(sock, msg)
    
    time.sleep(0.01)
    msg = 'PASS ' + handle_config.get_pop3('password')
    email_socket.send_to_server(sock, msg)
    
    sign_in_to_server__tail(sock)
    
        
