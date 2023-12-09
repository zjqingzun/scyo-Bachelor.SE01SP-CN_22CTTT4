

# library
import socket 
import os
import time
import datetime
import array as arr
# import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk
from datetime import datetime



# file .py
import handle


# version
VERSION = "1.0 SE01SP"


# config
HOST = "10.0.140.42"
PORT_SMTP = 2500
PORT_POP3 = 1100



# encode and limit
FORMAT = "utf8"
# BUFFER_SIZE = 3145728    #3MB = 3.145.728 byte



# variable message
msg = ""



# variable option
option = "0"
index_list = int(0)
index_mail = int(-1)



# variable check-test & recv
data = ""
str_data = ""
sub = ""



# handle file
limit_file = []
flag_file = int(2)
count_file = int(0)



# account
account = ""
password = ""



# global socket initialize
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_send = (HOST, PORT_SMTP)
server_recv = (HOST, PORT_POP3)



# connected
client.connect(server_recv)



#main (yet)
try :
    # account (yet)
    while True :
        # save account (file path) (yet)
        
        
        # account not saved yet (yet)
        msg = "CAPA"
        handle.send_to_server(client, msg)
        
        # account (yet)
        while True :
            account = input("Account: ")
            handle.send_to_server(client, "USER" + account)
            # test
            data = client.recv(1024)
            str_data = data.decode(FORMAT)
            if str_data == "+OK" :
                break
            print("Account does not exist !")
        
        # password (yet)
        while True :
            password = input("Password: ")
            handle.send_to_server(client, "PASS" + password)
            #test 
            data = client.recv(1024)
            str_data = data.decode(FORMAT)
            if str_data == "+OK" :
                break
            print("Password does not exist !")

        # (yet)
        msg = "STAT"
        handle.send_to_server(client, msg)
        msg = "QUIT"
        handle.send_to_server(client, msg)
        break
           
    # menu (yet)
    while True:
        # option menu (perfect)
        handle.option__menu()
        option = input("Your choice: ")

    
        if option == "1" :
            # config (yet)
            msg = "STAT"
            handle.send_to_server(client, msg)
            msg = "QUIT"
            handle.send_to_server(client, msg)
            client.connect(server_send)
            
            
            
            # begin email (perfect)
            print("This is the information to compose an email: ")
            print(" (If not filled in, please press 'enter' to skip)\n")
            # text editor (yet)
            to_mail = []            # input to (yet)
            cc_mail = []            #input cc (yet)
            bcc_mail = []            # input bcc (yet)
            subject = input("Subject: ")
            
            # input content (yet)
            content = ""
            print("Content: (Enter '..' to end the Content section)\n")
            while True :
                sub = input()
                if sub == "..":
                    break
                sub += '\n'
                content += sub
            sub = ""
            
            flag_file = int(input("Are files attached? (1. yes, 2. no): "))
            if flag_file == 1 :
                while True :
                    count_file = int(input("Number of files you want to send (no more than 10 files): "))
                    if count_file > 0 and count_file <= 10 :
                        break
                    print("Error: is not within the allowable limit.")
                for i in count_file :
                    sub = input("Specify the ith file path ", i, ": ")
                    limit_file.append(sub)
                    
            
            
            # send data to server (yet)
            # initialize id (yet)
            mess_id = "202312302053-uiwciew3498ncw834t"
            
            # from (yet)
            msg = "EHLO [10.0.140.42]"
            handle.send_to_server(client, msg)
            msg = "MAIL FROM:<" + account + ">"
            handle.send_to_server(client, msg)
            
            # to (yet)
            msg = "RCPT TO:<"
            for i in to_mail :
                handle.send_to_server(client, msg + i + ">")
            for i in cc_mail :
                handle.send_to_server(client, msg + i + ">")
            for i in bcc_mail :
                handle.send_to_server(client, msg + i + ">")
            
            # text (yet)
            msg = "DATA"
            handle.send_to_server(client, msg)
            msg = "Message-ID: " + mess_id
            handle.send_to_server(client, msg)
            msg = "User-Agent: " + VERSION
            handle.send_to_server(client,msg)
            # to of mail (yet)
            if len(to_mail) != 0 :
                msg = "To: "
                for i in to_mail :
                    msg += i
                    if i != to_mail[len(to_mail) - 1] :
                        msg += ","
            handle.send_to_server(client, msg)
            # cc of mail (yet)
            if len(cc_mail) != 0 :
                msg = "Cc: "
                for i in cc_mail :
                    msg += i
                    if i != cc_mail[len(cc_mail) - 1] :
                        msg += ","
            handle.send_to_server(client, msg)
            # bcc of mail (yet)
            if len(bcc_mail) != 0 :
                msg = "To: undisclosed-recipients "
            # from of mail (yet)
            msg = "From: " + account
            handle.send_to_server(client, msg)
            msg = "Subject: " + subject
            handle.send_to_server(client, msg)
            
            # content
            msg = "Content: " + str(count_file)
            handle.send_to_server(client, msg)
            
            if flag_file == 1 :
                msg = "\n"
                handle.send_to_server(client, msg)
                msg = "--text--"
                handle.send_to_server(client, msg)
                msg = "\n"
                handle.send_to_server(client, msg)
                msg = content
                handle.send_to_server(client, msg)
                msg = "\n"
                handle.send_to_server(client, msg)
                msg = "----" + mess_id
                handle.send_to_server(client, msg)
                
                # file (yet)
                for i in count_file :
                    msg = "\n"
                    handle.send_to_server(client, msg)
                    msg = "--file--" + str(i)
                    handle.send_to_server(client, msg)
                    msg = "\n"
                    handle.send_to_server(client, msg)
                    
                    # send file (yet)
                
                
                msg = "\n"
                handle.send_to_server(client, msg)
                msg = "."
                handle.send_to_server(client, msg)
            else :
                msg = "\n"
                handle.send_to_server(client, msg)
                msg = content
                handle.send_to_server(client, msg)
                msg = "\n"
                handle.send_to_server(client, msg)
                msg = "."
                handle.send_to_server(client, msg)
            
            # Confirm email (perfect)
            msg = "QUIT"
            handle.send_to_server(client, msg)
            print("Email sent successfully !")
            
            # Test not data
            # data = client.recv(4096)
            # str_data = data.decode(FORMAT)
            # if not data:
            #     break 
        elif option == "2" :
            #config
            client.connect(server_recv)
            
            
            
            # connect the transmission line
            msg = "CAPA"
            handle.send_to_server(client, msg)
            msg = "USER " + account
            handle.send_to_server(client, msg)
            msg = "PASS " + password
            handle.send_to_server(client, msg)
            msg = "LIST" 
            handle.send_to_server(client, msg)
            msg = "UIDL"
            handle.send_to_server(client, msg)
            
            
            
            
            
            
            # option
            print("Here is a list of folders in your mailbox:")
            print("1. Inbox")
            print("2. Project")
            print("3. Important")
            print("4. Work")
            print("5. Spam")
            index_list = int(input("Which folder do you want to see emails in: "))
            index_mail = int(input("Which Email do you want to read: "))
            
            # path -> sub (count email)
            
            if index_mail == 0:
                continue
            # elif index_mail > 0 and index_mail <= sub :    
            
            
            
            
            
            
            
            
                
        elif option == "3" :
            option = "0"
            break
        
        
        # return initially for the next session
        msg = ""
        option = "0"
        index_list = int(0)
        index_mail = int(-1)
        data = ""
        str_data = ""
        sub = ""
        limit_file = []
        flag_file = int(2)
        count_file = int(0) 
except :
    print("Error: server is not responding")
finally:
    msg = "QUIT"
    handle.send_to_server(client, msg)
    client.close()
