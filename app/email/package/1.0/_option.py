import socket

import handle_option
import _config

from socket import socket




def menu_choice(client : socket) :
    option = int(3)
    while True :  
        if option > 0 and option <= 3 :
            handle_option.menu_manual()
            
        option = int(input("Your choice: ")) 
        
        if option == 3 :
            break
        elif option == 2 :
            # connect to server pop3
            client.connect((_config.handle_config.get_pop3('server'), _config.handle_config.get_pop3('port')))
            
            # receive mail from server
            handle_option.email_box(client)
        elif option == 1 :
            # connect to server smtp
            client.connect((_config.handle_config.get_smtp('server'), _config.handle_config.get_smtp('port')))
            
            # compose
            handle_option.create_compose(client)
            
            # confirm
            print("Email sent successfully !")
            # option = 1
        else :
            print("Error: You chose wrong!")
            
            
  
# # test          
# menu_choice()
        