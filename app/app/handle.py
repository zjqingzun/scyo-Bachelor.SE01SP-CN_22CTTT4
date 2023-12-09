import os
import socket
from datetime import datetime



FORMAT = "utf8"
BUFFER_SIZE = 3145728

# request : yeu cau
# receive : nhan duoc
# encode : chuoi ky tu duoc ma hoa
# decode : chuoi ky tu sau khi giai ma

# s.recv()  Phương thức này nhận TCP message.
# s.send()	Phương thức này truyền TCP message.




def option__menu():
    print("Please select Menu: \n")
    print("1. To send emails\n")
    print("2. To view a list of received emails\n")
    print("3. Exit\n")


def send_to_server(sock: socket, s: str) :
    if sock is None :
        print(s)
    else :
        try :
            sock.sendall(bytes(s + "\n", FORMAT))
        except :
            raise ConnectionError
