import base64
import os
import shutil



# function 1
def handle__read(__path) :
    try :
        with open(__path, 'r') as file :
            content = file.read()
            
            # more line
            # for line in file.readline() :
            
            # first line
            # first_line = file.readline()
            # print(first_line)
            
        return content
    except FileNotFoundError :
        print(f"File '{__path}' does not exist.")
        return None
    except Exception as e :
        print(f"An error occurred: {e}")
        return None
    
    
def read_and_encode_file(__path):
    try:
        with open(__path, 'rb') as file:
            binary_content = file.read()
        return base64.b64encode(binary_content).decode('utf-8')
    except IOError as e:
        print(f"Error: {e}")
        return None
    
    
def decode_file_and_write(__path, __data) :
    decoded_data = base64.b64decode(__data)
    with open(__path, 'wb') as file:
        file.write(decoded_data)
    # print(f"The data has been written to the file at path {__path}.")
    
    
def get_file_name(path) :
    file_name = os.path.basename(path)
    return file_name


def get_file_size(path) :
    if os.path.exists(path) :
        size = os.path.getsize(path)
        return size
    else :
        print(" File does not exists.")
        return None


def file_exists(file_path):
    return os.path.exists(file_path)


def handle__copy(orig, copy):
    orig_path = './app/email/data/box/' + orig
    new_path = './app/email/data/box/' + copy
    try:
        shutil.copy2(orig_path, new_path)
    except IOError as e:
        print(f"File could not be copied {orig_path}: {e}.")


def get_file_subject(path) :
    str_data = handle__read(path)
    list_data = str_data.split('\n')
    result = list_data[0]
    return result[:15]