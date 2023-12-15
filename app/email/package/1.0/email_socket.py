import socket
import base64
from socket import socket




def send_to_server(sock : socket, s: str) :
    if sock is None :
        print(s)
    else :
        try :
            sock.sendall(bytes(s + "\n", 'utf8'))
        except :
            raise ConnectionError
        
        
def get_receive_data(sock) :
    data = b""
    while True :
        chunk = sock.recv(1024)
        if not chunk :
            break
        data += chunk
        if b"\r\n" in data :
            break
        
    data = base64.b64encode(data).decode('utf-8')
    return data


def get_amount_mail(sock) :
    data = b""
    while True :
        chunk = sock.recv(1024)
        if not chunk :
            break
        data += chunk
        if b"\r\n" in data :
            break
    data = data.decode("utf-8")
    sub = data.split("\r\n")[-3]
    count = int(sub.split()[0])    
    return count