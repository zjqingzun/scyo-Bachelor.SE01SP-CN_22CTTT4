import csv




def handle__mail_status(no_mail) :
    _path = './app/email/data/box/status.csv'
    
    desired_column = 1
    desired_row = int(no_mail)
    with open(_path, 'r') as file:
        reader = csv.reader(file)
    
        for i, row in enumerate(reader) :
            if i == desired_row - 1 :
                desired_data = row[desired_column]
                if desired_data == 'yet' :
                    return False
                else :
                    return True

def change__status(no_mail) :
    _path = './app/email/data/box/status.csv'
    
    note = int(no_mail)
    pause_list = []
    with open(_path, 'r+') as file :
        reader = csv.reader(file)
        for lines in reader :
            pause_list.append(lines)
        pause_list[note - 1][1] = 'read'
        
    with open(_path, 'w', newline="") as file :
        reader = csv.writer(file)
        for pri in pause_list :
            reader.writerow(pri)

def add__mail_status(data) :
    _path = './app/email/data/box/status.csv'
    with open(_path, 'a', newline='\n') as file :
        writer = csv.writer(file)
        writer.writerow(data)
        
        
def count__mail() :
    count = 0
    with open('./app/email/data/box/status.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            count = count + 1
            
    return count
        