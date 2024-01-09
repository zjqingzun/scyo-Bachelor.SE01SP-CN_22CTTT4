import socket
import time

from datetime import datetime, timedelta

import email_socket
import handle_config
import handle_file



def create__messageid(emailName) :
    current_datetime = datetime.now()  # Get the current time
    current_datetime += timedelta(hours=7)  # Add 7 hours to get +07:00 timezone

    date_str = current_datetime.strftime("%Y%m%d")  # Get the current date in the format yyyymmdd
    time_str = current_datetime.strftime("%H%M%S")  # Get the current time in the format hhmmss


    encoded_email = ""
    for char in emailName:
        encoded_char = hex(ord(char) + 2)[2:]  # Increase the ASCII value of the character by 2 and convert to hex
        encoded_email += encoded_char

    utc_offset = "UTC+07:00"
    result = date_str + time_str + "-" + utc_offset + "-" + encoded_email
    return result

# def input__addr_to(addr) :
#     addr = input("To: ")
#     if addr :
#         list_addr = addr.split(",")
#         return list_addr
#     else :
#         list_addr = []
#         return list_addr

# def input__addr_cc(addr) :
#     addr = input("Cc: ")
#     if addr :
#         list_addr = addr.split(",")
#         return list_addr
#     else :
#         list_addr = []
#         return list_addr

# def input__addr_bcc(addr) :
#     addr = input("Bcc: ")
#     if addr :
#         list_addr = addr.split(",")
#         return list_addr
#     else :
#         list_addr = []
#         return list_addr

# def input__subject(subject : str) :
#     subject = input("Subject: ")
#     return subject

# def input__file(path) :
#     content = ""
#     i = 0
#     while i < amount_file :
#         path = str(input(f"Specify the with file path {i + 1}: "))
#         if handle_file.file_exists(path) :
#             if int(handle_file.get_file_size(path)) <= 3145728 :
#                 content = content + "\n\n--" + str(i + 1) + "--" 
#                 content = content + str(handle_file.get_file_name(path)) + "--" 
#                 content = content + str(handle_file.get_file_size(path)) +"\n\n"
#                 content = content + str(handle_file.read_and_encode_file(path))
#             else :
#                 print("Error: The file exceeds 3MB in size.\n")
#                 sub = str(input("Do you want to re-enter? (Yes or No): "))
#                 if sub == "Yes" :
#                     i = i - 1
#                 else :
#                     i = i - 1
#                     amount_file = amount_file - 1
#         else :
#             print(f"Error: File {path} not exists.\n")
#             sub = str(input("Do you want to re-enter? (Yes or No): "))
#             if sub == "Yes" :
#                 i = i - 1
#             else :
#                 i = i - 1
#                 amount_file = amount_file - 1
#         i = i + 1
        
#     return content

def input__content(content : str, file_path : list) :
    __content = "Content: " 
    __content += "\n\n"
    
    __content = __content + "----text----" + str(len(content)) + "\n\n"
    __content += content
       
    if len(file_path) > 0 :
        if '\n' in file_path[0] or ' ' in file_path[0] :
            file_path.pop()
            return __content
        
        __content = __content + "\n\n" + "----file----" 
        
        i = int(0)
        content_sub = ""
        while i < len(file_path) :
            content_sub = content_sub + "\n\n--" + str(i + 1) + "--"
            content_sub = content_sub + str(handle_file.get_file_name(file_path[i])) + "--"
            content_sub = content_sub + str(handle_file.get_file_size(file_path[i])) + "\n\n"
            content_sub = content_sub + str(handle_file.read_and_encode_file(file_path[i])) 
        
        __content = __content + str(len(file_path)) + content_sub
    
    
    return __content
    
def check__address_unit(list_addr) :
    if list_addr :
        return True
    else :
        list_addr = []
        return False

def email__send(client : socket, messageid : str, to_mail, cc_mail, bcc_mail, subject : str, __content : str) :
    msg = ""
    time.sleep(0.01)
    
    msg = "EHLO [" + str(socket.gethostbyname(socket.gethostname())) + "]"
    email_socket.send_to_server(client, msg)
    time.sleep(0.01)
    
    msg = "MAIL FROM:<" + handle_config.get_smtp('username') + ">"
    email_socket.send_to_server(client, msg)
    time.sleep(0.01)
    
    msg = "RCPT TO:<"
    if check__address_unit(to_mail) :
        for i in to_mail :
            email_socket.send_to_server(client, msg + i + ">")
            time.sleep(0.01)
    
    if check__address_unit(cc_mail) :
        for i in cc_mail :
            email_socket.send_to_server(client, msg + i + ">")
            time.sleep(0.01)
            
    if check__address_unit(bcc_mail) :
        for i in bcc_mail :
            email_socket.send_to_server(client, msg + i + ">")
            time.sleep(0.01)
    time.sleep(0.01)
    
    msg = "DATA"
    email_socket.send_to_server(client, msg)
    time.sleep(0.01)
    
    msg = "Message-ID: " + messageid
    email_socket.send_to_server(client, msg)
    time.sleep(0.01)
    
    msg = "Version: " + handle_file.handle__read('./app/email/plugins/version.txt')
    email_socket.send_to_server(client, msg)
    time.sleep(0.01)
    
    if check__address_unit(to_mail) :
        msg = "To: "
        for i in to_mail :
            msg += i
            if i != to_mail[len(to_mail) - 1] :
                msg += ','
        email_socket.send_to_server(client, msg)
        time.sleep(0.02)
    
    if check__address_unit(cc_mail) :
        msg = "Cc: "
        for i in cc_mail :
            msg += i
            if i != cc_mail[len(cc_mail) - 1] :
                msg += ','
        email_socket.send_to_server(client, msg)
        time.sleep(0.02)
    
    if check__address_unit(bcc_mail) :
        msg = "To: <undisclosed-recipients>"
        email_socket.send_to_server(client, msg)
        time.sleep(0.01)
    
    msg = "From: <" + handle_config.get_smtp('username') + ">"
    email_socket.send_to_server(client, msg)
    time.sleep(0.01)
    
    msg = "Subject: " + str(subject)
    email_socket.send_to_server(client, msg)
    time.sleep(0.2)
    
    msg = __content
    email_socket.send_to_server(client, msg)
    time.sleep(1)
    
    msg = "\n"
    email_socket.send_to_server(client, msg)
    time.sleep(0.01)
    
    msg = "."
    email_socket.send_to_server(client, msg)
    time.sleep(0.01)
    
    msg = "QUIT"
    email_socket.send_to_server(client, msg)
    time.sleep(0.01)
        
def email__compose(client : socket, to_mail : list, cc_mail: list, bcc_mail:list, subject : str, content : str, file_path : list) :
    # # head
    # content
    __content = input__content(content, file_path)
    
    if to_mail[0] == '' :
        to_mail.pop()
    if cc_mail[0] == '' :
        cc_mail.pop()
    if bcc_mail == '' :
        bcc_mail.pop()
    
    # send to server
    time.sleep(0.01)
    messageid = str(create__messageid(handle_config.get_smtp('username')))
    time.sleep(0.01)
    email__send(client, messageid, to_mail, cc_mail, bcc_mail, subject, __content)
    



