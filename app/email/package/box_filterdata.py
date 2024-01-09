import os
import json

from datetime import datetime, timedelta

import handle_file
import standby_state


def decode_string(encoded_string):
    encoded_email = encoded_string.split("-")[2]

    decoded_email = ""
    for i in range(0, len(encoded_email), 2):
        encoded_char = encoded_email[i:i + 2]
        decoded_char = chr(int(encoded_char, 16) - 2)
        decoded_email += decoded_char

    date_str = encoded_string[:8]
    time_str = encoded_string[8:14]
    utc_offset = encoded_string[15:24]

    new_s = f"{date_str} {time_str} {utc_offset}"

    current_datetime = datetime.strptime(new_s, "%Y%m%d %H%M%S %Z%z")
    formatted_datetime = current_datetime.strftime("%A, %B %d %Y, %H:%M:%S, %Z%z")
    return decoded_email, formatted_datetime


def cup_filterdata(filename) :
    str_data = handle_file.handle__read("./app/email/appcache/cache/" + filename)
    data = str_data.split()
    # print(data)
    
    i = int(5)
    if data[4] == 'Version:' :
        ver = ""
        while True :
            ver += data[i]
            if data[i + 1] == 'To:' or data[i + 1] == 'Cc:':
                break
            else :
                ver += ' '
            i = i + 1
        if ver == str(handle_file.handle__read("./app/email/plugins/version.txt")) :
            
            email_name, email_datetime = decode_string(data[3])
            to_mail = ""
            subject_mail = ""
            content_text_mail = ""
            flag_file = False
            link_file = []
                    
            if '----file----' in str_data :
                flag_file = True
                
                # get the number of files
                count_file = int(data[-3].split('--')[1])
                pos_file = int(0 - (count_file * 2 + 1))
                
                # path download: ./app/email/appcache/download/
                original_path_download = "./app/email/appcache/download/"
                
                while pos_file < -1 :
                    file_name = data[pos_file].split('--')[2]
                    pos_file = pos_file + 1
                    
                    ######################################## fig bug - trung ten file
                    
                    
                    handle_file.decode_file_and_write(original_path_download + file_name, data[pos_file])
                    pos_file = pos_file + 1
                    
                    link_file.append(file_name)
            
            i = i + 2
            while data[i] != 'From:' :
                to_mail += data[i] + ','
                i = i + 1
            
            i = i + 2
            if data[i] == 'Subject:' :
                i = i + 1
                while data[i] != 'Content:' :
                    subject_mail += data[i] + ' '
                    i = i + 1
            
            
            i = i + 1
            if '----text----' in data[i] :
                i = i + 1
                if flag_file :
                    while '----file----' not in data[i] :
                        content_text_mail += data[i] + ' '
                        i = i + 1
                else :
                    while data[i] != '.' :
                        content_text_mail += data[i] + ' '
                        i = i + 1
            
            no_mail = ''.join(filter(str.isdigit, filename))
            
            
            with open('./app/email/data/box/inbox/' + str(no_mail) + '.txt', 'w') as file:
                file.write(subject_mail.upper() + '\n\n')
                file.write("Time: " + email_datetime + '\n\n')
                file.write("To: " + to_mail + '\n')
                file.write("Content: " + '\n\n    ')
                file.write(content_text_mail + '\n\n\n\n')
                
                for pri in link_file :
                    file.write('./app/email/appcache/download/' + pri + '\n')

def get_data(count__mail : int) :
    if count__mail == 0 :
        return
    
    i = int(1)
    folder_path = "./app/email/appcache/cache"
    for filename in os.listdir(folder_path) :
        if i > count__mail :
            if os.path.isfile(os.path.join(folder_path, filename)) and ".txt" in filename :
                cup_filterdata(filename)
        
        i = i + 1
            
            
            
def mail_classificationdata(filename) :
    str_data = handle_file.handle__read("./app/email/data/box/inbox/" + filename)
    no_mail = ''.join(filter(str.isdigit, filename))
    with open('./app/email/config/box.json', 'r') as file :
        data = json.load(file)
        
        list_data = str_data.split('\n')
        
        for pri in data['important'] :
            if pri in list_data[0] :
                standby_state.add__mail_status([str(no_mail), 'yet'])
                handle_file.handle__copy('inbox/' + filename, 'important/' + filename)
                return 0
            
        for pri in data['work'] :
            flag = False
            for i in list_data :
                if "Content: " in i :
                    flag = True
                
                if  flag == True:
                    if pri in i :
                        standby_state.add__mail_status([str(no_mail), 'yet'])
                        handle_file.handle__copy('inbox/' + filename, 'work/' + filename)
                        return 0
            
        for pri in data['spam'] :
            if pri in str_data :
                standby_state.add__mail_status([str(no_mail), 'yet'])
                handle_file.handle__copy('inbox/' + filename, 'spam/' + filename)
                return 0
                
    
    

def handle__mail_classification(count__mail : int) :
    if count__mail == 0 :
        return
    
    i = int(1)
    original_path = './app/email/data/box/inbox'
    for filename in os.listdir(original_path) :
        if i > count__mail :
            if os.path.isfile(os.path.join(original_path, filename)) :
                mail_classificationdata(filename)
        
        i = i + 1