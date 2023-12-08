import socket 
import os
import time
import datetime
import array as arr
# import tkinter as tk

# from tkinter import messagebox
# from tkinter import ttk
from datetime import datetime

import handle



# config
VERSION = "1.0 SE01SP"
HOST = "10.0.140.42"
PORT = 2500
FORMAT = "utf8"
BUFFER_SIZE = 3145728    #3MB = 3.145.728 byte

# settings
msg = ""
option = "0"
index_list = "0"

# handle file
limit_file = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
flag_file = "2"
count_file = "0"

# account
account_from = "job_letrongnghia@hotmail.com"
account_to = "job_letrongnghia@hotmail.com"

# global socket initialize
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
client.connect(server_address)




#main
try :
    # account
    
    
    
    
    # menu
    while True:
        print("Please select Menu: \n")
        print("1. To send emails\n")
        print("2. To view a list of received emails\n")
        print("3. Exit\n")
        option = input("Your choice: ")
    
    
        if option == "1" :
            option = "0"
            print("This is the information to compose an email: ")
            print(" (If not filled in, please press 'enter' to skip)\n")
            
            
            
            # enter text
            to = input("To: ")
            cc = input("CC: ")
            bcc = input("BCC: ")
            subject = input("Subject: ")
            content = input("Content: ")
            flag_file = input("Are files attached? (1. yes, 2. no): ")
            if flag_file == "1" :
                count_file = input("Number of files you want to send (no more than 10 files): ")
                for i in count_file :
                    limit_file[i] = input("Specify the ith file path ", i, ": ")
                    
            
            
            # send data to server
            msg = "EHLO [10.0.140.42]"
            handle.send_to_server(client, msg)
            msg = "MAIL FROM: <" + account_from + ">"
            handle.send_to_server(client, msg)
            msg = "RCPT TO: <" + account_to + ">"
            handle.send_to_server(client, msg)
            msg = "DATA"
            handle.send_to_server(client, msg)
            msg = "Message-ID: " + id
            handle.send_to_server(client, msg)
            msg = "User-Agent: " + VERSION
            handle.send_to_server(client,msg)
            
            
            # msg = "To: " +
            # handle.send_to_server(client,msg)
            # msg = "From: " +
            # handle.send_to_server(client,msg)
            # msg = "Subject: " +
            # handle.send_to_server(client,msg)
            # msg = "Content-Type: " +  + ";charset=" + + ";format="
            # handle.send_to_server(client,msg)
            # msg = "Content-Transfer-Encoding: " +
            # handle.send_to_server(client,msg)
            # msg = " "
            # handle.send_to_server(client,msg)
            # msg = "Wao!"
            # handle.send_to_server(client,msg)
            # msg = " "
            # handle.send_to_server(client,msg)

            # Confirm email
            print("Email sent successfully !")
            
            # Test not data
            # data = client.recv(4096)
            # str_data = data.decode(FORMAT)
            # if not data:
            #     break 
        elif option == "2" :
            option = "0"
            print("Here is a list of folders in your mailbox:")
            print("1. Inbox")
            print("2. Project")
            print("3. Important")
            print("4. Work")
            print("5. Spam")
            index_list = input("Which folder do you want to see emails in: ")
            
            
            
        elif option == "3" :
            option = "0"
            break
        
    
except :
    print("Error: server is not responding")
finally:
    msg = "QUIT"
    handle.send_to_server(client, msg)
    client.close()