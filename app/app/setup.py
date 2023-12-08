

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
BUFFER_SIZE = 3145728    #3MB = 3.145.728 byte



# variable message
msg = ""



# variable option
option = "0"
index_list = int(0)
index_mail = int(-1)



# variable check-test & recv
data = ""
str_data = ""



# handle file
limit_file = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
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



#main
try :
    # account
    while True :
        # save account
        
        
        # account not saved yet
        msg = "CAPA"
        handle.send_to_server(client, msg)
        
        # account    
        while True :
            account = input("Account: ")
            handle.send_to_server(client, "USER" + account)
            # test
            data = client.recv(1024)
            str_data = data.decode(FORMAT)
            if str_data == "+OK" :
                break
            print("Account does not exist !")
        
        # password
        while True :
            password = input("Password: ")
            handle.send_to_server(client, "PASS" + password)
            #test 
            data = client.recv(1024)
            str_data = data.decode(FORMAT)
            if str_data == "+OK" :
                break
            print("Password does not exist !")

        msg = "STAT"
        handle.send_to_server(client, msg)
        break
           
    # menu
    while True:
        print("Please select Menu: \n")
        print("1. To send emails\n")
        print("2. To view a list of received emails\n")
        print("3. Exit\n")
        option = input("Your choice: ")
    
    
        if option == "1" :
            # config
            client.close()
            client.connect(server_send)
            
            
            
            # begin email
            print("This is the information to compose an email: ")
            print(" (If not filled in, please press 'enter' to skip)\n")
            # enter text
            
            
            to = input("To: ")
            cc = input("CC: ")
            bcc = input("BCC: ")
            
            
            subject = input("Subject: ")
            content = input("Content: ")
            flag_file = int(input("Are files attached? (1. yes, 2. no): "))
            if flag_file == 1 :
                count_file = int(input("Number of files you want to send (no more than 10 files): "))
                for i in count_file :
                    limit_file[i] = input("Specify the ith file path ", i, ": ")
                    
            
            
            # send data to server
            msg = "EHLO [10.0.140.42]"
            handle.send_to_server(client, msg)
            msg = "MAIL FROM: <" + account + ">"
            handle.send_to_server(client, msg)
            
            # msg = "RCPT TO: <" +  + ">"
            # handle.send_to_server(client, msg)
            
            msg = "DATA"
            handle.send_to_server(client, msg)
            msg = "Message-ID: " + id
            handle.send_to_server(client, msg)
            msg = "User-Agent: " + VERSION
            handle.send_to_server(client,msg)
            
            # To: CC, BCC
            
            # From: 
            
            msg = "Subject: " + subject
            handle.send_to_server(client, msg)
            msg = "Content: "
            handle.send_to_server(client, msg)
            msg = "\n"
            handle.send_to_server(client, msg)
            msg = content
            handle.send_to_server(client, msg)
            msg = "\n"
            handle.send_to_server(client, msg)
            msg = "."
            handle.send_to_server(client, msg)
            
            
            

            # Confirm email
            print("Email sent successfully !")
            
            # Test not data
            # data = client.recv(4096)
            # str_data = data.decode(FORMAT)
            # if not data:
            #     break 
        elif option == "2" :
            #config
            client.close()
            client.connect(server_recv)
            
            
            
            # connect the transmission line
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
        index_list = "0"
        data = ""
        str_data = ""
        limit_file = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
        flag_file = int(2)
        count_file = int(0) 
except :
    print("Error: server is not responding")
finally:
    msg = "QUIT"
    handle.send_to_server(client, msg)
    client.close()
