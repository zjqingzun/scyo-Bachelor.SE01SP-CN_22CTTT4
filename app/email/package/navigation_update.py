import socket
import time

import standby_state
import box_receive
import box_filterdata

import _config




# function




# main function
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((_config.handle_config.get_pop3('server'), _config.handle_config.get_pop3('port')))

count_mail = standby_state.count__mail()
if count_mail == 0 :
    box_receive.get_list_email(client)
else :
    box_receive.get_list_mail_update(client, count_mail)
    
box_filterdata.get_data(count_mail)
box_filterdata.handle__mail_classification(count_mail)


client.close()