

import time


from datetime import datetime, timedelta

def convert_to_string(email):
    current_datetime = datetime.now()  # Lấy thời gian hiện tại
    current_datetime += timedelta(hours=7)  # Cộng thêm 7 giờ để có mũi giờ +07:00

    date_str = current_datetime.strftime("%Y%m%d")  # Lấy ngày tháng hiện tại dưới định dạng yyyymmdd
    time_str = current_datetime.strftime("%H%M%S")  # Lấy thời gian hiện tại dưới định dạng hhmm

    email_str = email.split("@")[0]

    encoded_email = ""
    for char in email_str:
        encoded_char = hex(ord(char) + 2)[2:]  # Tăng giá trị mã ASCII của ký tự lên 2 và chuyển sang hệ 16
        encoded_email += encoded_char

    result = date_str + time_str + "-+0700-" + encoded_email
    return result
    

def decode_string(encoded_string):
    encoded_email = encoded_string.split("-")[2]

    decoded_email = ""
    for i in range(0, len(encoded_email), 2):
        encoded_char = encoded_email[i:i + 2]
        decoded_char = chr(int(encoded_char, 16) - 2)
        decoded_email += decoded_char

    date_str = encoded_string[:8]
    time_str = encoded_string[8:14]
    timezone_str = encoded_string[15:20]

    new_s = f"{date_str} {time_str} {timezone_str}"

    current_datetime = datetime.strptime(new_s, "%Y%m%d %H%M%S %z")
    formatted_datetime = current_datetime.strftime("%A, %Y/%m/%d %H:%M:%S, UTC%z")
    return decoded_email + "@gmail.com", formatted_datetime
    
    
    
s1 = convert_to_string("admin@control.com")
print(s1)

time.sleep(2)

s2, s = decode_string(s1)
print(s2)
print(s)















