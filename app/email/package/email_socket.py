import socket
import base64
import time
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
    chunk = sock.recv(1024)
    data += chunk
    time.sleep(0.5)
    
    test_data = int(data.split()[1])
    
    print(test_data)
    
    while len(data) < test_data:
        chunk = sock.recv(1024)
        if not chunk :
            break
        data += chunk
        time.sleep(0.5)
    time.sleep(0.02)
        
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