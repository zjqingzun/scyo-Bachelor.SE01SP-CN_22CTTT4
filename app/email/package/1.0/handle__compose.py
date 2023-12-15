import socket
import time

from datetime import datetime

import email_socket
import handle_config
import handle_file



def create__messageid(emailName) :
    current_datetime = datetime.now()
    date_str = current_datetime.strftime("%Y%m%d")  # Lấy ngày tháng hiện tại dưới định dạng yyyymmdd
    time_str = current_datetime.strftime("%H%M")  # Lấy thời gian hiện tại dưới định dạng hhmm

    email_str = emailName.split("@")[0]

    encoded_email = ""
    for char in email_str:
        encoded_char = hex(ord(char) + 2)[2:]  # Tăng giá trị mã ASCII của ký tự lên 2 và chuyển sang hệ 16
        encoded_email += encoded_char

    result = date_str + time_str + "-" + encoded_email
    return result

def input__address_send(address) :
    return

def input__subject(subject : str) :
    subject = input("Subject: ")
    return subject

def input__file(amount_file : int) :
    content = ""
    i = 0
    while i < amount_file :
        path = str(input(f"Specify the with file path {i + 1}: "))
        if handle_file.file_exists(path) :
            if int(handle_file.get_file_size(path)) <= 3145728 :
                content = content + "\n\n--" + str(i + 1) + "--" 
                content = content + str(handle_file.get_file_name(path)) + "--" 
                content = content + str(handle_file.get_file_size(path)) +"\n\n"
                content = content + str(handle_file.read_and_encode_file(path))
            else :
                print("Error: The file exceeds 3MB in size.\n")
                sub = str(input("Do you want to re-enter? (Yes or No): "))
                if sub == "Yes" :
                    i = i - 1
                else :
                    i = i - 1
                    amount_file = amount_file - 1
        else :
            print(f"Error: File {path} not exists.\n")
            sub = str(input("Do you want to re-enter? (Yes or No): "))
            if sub == "Yes" :
                i = i - 1
            else :
                i = i - 1
                amount_file = amount_file - 1
        i = i + 1
    return content

def input__content(content : str, amount_file : int) :
    __content = "Content: " 
    __content += "\n\n"
    
    content = str(input("Content: "))
    
    
    __content = __content + "----text----" + str(len(content)) + "\n\n"
    __content += content
    
    
    __flag = input("Are files attached ? (1. yes, 2. no): ")
    if str(__flag) == "1" :
        while True :
            amount_file = int(input("Number of files you want to send (no more than 10 files): "))
            if (amount_file > 0) and (amount_file <= 10) :
                break
            print(f"Error: is not within the allowable limit.")
            
        __content = __content + "\n\n" + "----file----"
        
        content_sub = input__file(amount_file)
            
        __content = __content + str(amount_file) + content_sub
    
    return __content
    
def check__address_unit(list) :
    if len(list) == 0 :
        return False
    else :
        return True

def email__send(client : socket, messageid : str, to_mail, cc_mail, bcc_mail, subject : str, __content : str) :
    msg = ""
    time.sleep(0.01)
    
    msg = "EHLO [" + handle_config.get_smtp('server') + "]"
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
    time.sleep(0.5)
    
    msg = "\n"
    email_socket.send_to_server(client, msg)
    time.sleep(0.01)
    
    msg = "."
    email_socket.send_to_server(client, msg)
    time.sleep(0.01)
        
def email__compose(client : socket, to_mail, cc_mail, bcc_mail, subject : str, content : str, amount_file : int) :
    # head
    # input__address_send(to_mail)
    # input__address_send(cc_mail)
    # input__address_send(bcc_mail)
    to_mail = ["admin@control.com"]
    
    # subject
    _subject = input__subject(subject)
    
    # content
    __content = input__content(content, amount_file)
    
    # send to server
    time.sleep(0.01)
    messageid = str(create__messageid(handle_config.get_smtp('username')))
    time.sleep(0.01)
    email__send(client, messageid, to_mail, cc_mail, bcc_mail, _subject, __content)
    



