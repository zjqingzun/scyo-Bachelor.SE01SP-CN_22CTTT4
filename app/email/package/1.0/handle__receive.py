import socket
import time

import email_socket
import handle_config
import handle_file


def question_head(client : socket) :
    msg = "CAPA"
    time.sleep(0.01)
    
    email_socket.send_to_server(client, msg)
    time.sleep(0.01)
    
    msg = "USER " + handle_config.get_pop3('username')
    email_socket.send_to_server(client, msg)
    time.sleep(0.01)
    
    msg = "PASS " + handle_config.get_pop3('password')
    email_socket.send_to_server(client, msg)
    time.sleep(0.01)
    
    msg = "LIST"
    email_socket.send_to_server(client, msg)
    time.sleep(0.01)
    
    
def question_destroy(client : socket) :
    email_socket.send_to_server(client, "QUIT")
    time.sleep(0.01)


def get_list_email(client : socket) :
    question_head(client)
    
    # get list email from server
    amout = email_socket.get_amount_mail(client)
    original_path = "./app/email/appcache/cache/"
    for i in range(1, amout + 1) :
        email_socket.send_to_server(client, f"RETR {i}")
        email_data = email_socket.get_receive_data(client)
        handle_file.decode_file_and_write(original_path + f"email-cache-{i}.txt", email_data)
        time.sleep(0.5)
    
    question_destroy(client)