import socket

import handle__compose
import handle__receive



def menu_manual() :
    print("Please select Menu: \n")
    print("1. To send emails\n")
    print("2. To view a list of received emails\n")
    print("3. Exit\n")
    
    
def email_manual() :
    print("This is the information to compose an email: ")
    print(" (If not filled in, please press 'enter' to skip)\n")

    
def create_compose(sock : socket) :
    email_manual()
    
    # initialize variable
    to_mail = []
    cc_mail = []
    bcc_mail = []
    subject = str("")
    content = str("")
    amount_file = int(0)
    
    # input and send mail to server
    handle__compose.email__compose(sock, to_mail, cc_mail, bcc_mail, subject, content, amount_file)
    
    
def email_box(sock : socket) :
    # connect to server and receive
    handle__receive.get_list_email(sock)
    
    
    # box
    # print("Here is a list of folders in your mailbox:")
    # print("1. Inbox")
    # print("2. Project")
    # print("3. Important")
    # print("4. Work")
    # print("5. Spam")
    return
    



    



    
    
    
# test 
# menu_manual()

