import socket


import _config
import _option


# global socket initialize
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# main
try :
    # sign in
    client.connect((_config.handle_config.get_pop3('server'), _config.handle_config.get_pop3('port')))
    _config.sign_in_to_server(client)
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _option.menu_choice(client)
except :
    print("Error: server is not responding...")
    client.close()
finally : 
    client.close()







# yet

# Line 12 - 25: File handle__compose.py. Yet build create_messageid(file_path)

# Line 27 - 28: File handle__compose.py. Yet build input__address_send(address)