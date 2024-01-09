# import socket

# def get_ip_address():
#     try:
#         # Sử dụng socket.gethostbyname(socket.gethostname()) để lấy địa chỉ IP
#         ip_address = socket.gethostbyname(socket.gethostname())
#         print("Địa chỉ IP mạng hiện tại của máy:", ip_address)
#     except socket.error as e:
#         print("Không thể lấy địa chỉ IP:", e)

# # Gọi hàm để lấy và in địa chỉ IP
# get_ip_address()








# from tkinter import Tk, filedialog
# import os

# def open_files_with_limit(file_size_limit_MB):
#     root = Tk()
#     root.withdraw()  # Ẩn cửa sổ chính

#     # Cấu hình các tùy chọn cho hộp thoại
#     file_options = {
#         'title': 'Select Files',
#         'filetypes': [('All Files', '*.*')],
#         'initialdir': '/path/to/initial/directory'
#     }

#     # Mở hộp thoại và lấy danh sách đường dẫn tệp tin được chọn
#     file_paths = filedialog.askopenfilenames(**file_options)

#     # Kiểm tra dung lượng của từng tệp tin
#     selected_files_within_limit = []
#     for path in file_paths:
#         file_size_MB = os.path.getsize(path) / (1024 * 1024)  # Chuyển đổi dung lượng về Megabyte
#         if file_size_MB <= file_size_limit_MB:
#             selected_files_within_limit.append(path)
#         else:
#             print(f"File {path} exceeds the size limit.")

#     # In danh sách đường dẫn tệp tin trong giới hạn dung lượng
#     print("Selected files within the size limit:")
#     for path in selected_files_within_limit:
#         print(path)

# # Gọi hàm để mở hộp thoại và lấy đường dẫn tệp tin được chọn trong giới hạn dung lượng
# open_files_with_limit(file_size_limit_MB=3)








# import threading
# import time

# def user_input_program():
#     while True:
#         user_input = input("Nhập một số (để dừng nhập, nhập 'stop'): ")
#         if user_input.lower() == 'stop':
#             break

# def hello_program():
#     while True:
#         print("Hello")
#         time.sleep(5)

# # Tạo hai luồng
# user_input_thread = threading.Thread(target=user_input_program)
# hello_thread = threading.Thread(target=hello_program)

# # Bắt đầu chạy các luồng
# user_input_thread.start()
# hello_thread.start()

# # Đợi cho đến khi luồng nhập từ người dùng kết thúc
# user_input_thread.join()

# # Khi luồng nhập từ người dùng kết thúc, thông báo cho luồng "Hello" dừng lại
# hello_thread.join()




# count = 0
# with open('./app/email/data/box/status.csv', 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         count = count + 1


# print("Count: ", count)




# import os
# import json
# import csv
# import shutil
# def handle__read(__path) :
#     try :
#         with open(__path, 'r') as file :
#             content = file.read()
            
#             # more line
#             # for line in file.readline() :
            
#             # first line
#             # first_line = file.readline()
#             # print(first_line)
            
#         return content
#     except FileNotFoundError :
#         print(f"File '{__path}' does not exist.")
#         return None
#     except Exception as e :
#         print(f"An error occurred: {e}")
#         return None

# def add__mail_status(data) :
#     _path = './app/email/data/box/status.csv'
#     with open(_path, 'a', newline='\n') as file :
#         writer = csv.writer(file)
#         writer.writerow(data)

# def handle__copy(orig, copy):
#     orig_path = './app/email/data/box/' + orig
#     new_path = './app/email/data/box/' + copy
#     try:
#         shutil.copy2(orig_path, new_path)
#     except IOError as e:
#         print(f"File could not be copied {orig_path}: {e}.")


# def mail_classificationdata(filename) :
#     str_data = handle__read("./app/email/data/box/inbox/" + filename)
#     no_mail = ''.join(filter(str.isdigit, filename))
#     with open('./app/email/config/box.json', 'r') as file :
#         data = json.load(file)
        
#         list_data = str_data.split('\n')
        
#         for pri in data['important'] :
#             if pri in list_data[0] :
#                 add__mail_status([str(no_mail), 'yet'])
#                 handle__copy('inbox/' + filename, 'important/' + filename)
#                 return 0
            
#         for pri in data['work'] :
#             flag = False
#             for i in list_data :
#                 if "Content: " in i :
#                     flag = True
                
#                 if  flag == True:
#                     if pri in i :
#                         add__mail_status([str(no_mail), 'yet'])
#                         handle__copy('inbox/' + filename, 'work/' + filename)
#                         return 0
            
#         for pri in data['spam'] :
#             if pri in str_data :
#                 add__mail_status([str(no_mail), 'yet'])
#                 handle__copy('inbox/' + filename, 'spam/' + filename)
#                 return 0
                    
# def handle__mail_classification() :
#     original_path = './app/email/data/box/inbox'
#     for filename in os.listdir(original_path) :
#         if os.path.isfile(os.path.join(original_path, filename)) :
#             mail_classificationdata(filename)
                    

# handle__mail_classification()








# import os
# import tkinter as tk
# from tkinter import filedialog

# def show_files():
#     folder_path = filedialog.askdirectory()  # Hiển thị hộp thoại chọn thư mục
#     if folder_path:
#         file_list = os.listdir(folder_path)
#         file_listbox.delete(0, tk.END)  # Xóa danh sách hiện tại (nếu có)
#         for file_name in file_list:
#             file_listbox.insert(tk.END, file_name)  # Thêm tên file vào danh sách

# # Tạo cửa sổ chính
# root = tk.Tk()
# root.title("Hiển thị Tên File")

# # Frame thứ nhất để chọn thư mục
# frame1 = tk.Frame(root)
# frame1.pack(padx=10, pady=10)

# select_button = tk.Button(frame1, text="Chọn Thư Mục", command=show_files)
# select_button.pack()

# # Frame thứ hai để hiển thị tên file
# frame2 = tk.Frame(root)
# frame2.pack(padx=10, pady=10)

# file_listbox = tk.Listbox(frame2, width=50, height=10)
# file_listbox.pack()

# root.mainloop()







# chuoi_goc = "Chuỗi ký tự cần cắt"
# chuoi_moi = chuoi_goc[:15]

# print(chuoi_moi)








# import csv
# def handle__mail_status(no_mail) :
#     _path = './app/email/data/box/status.csv'
    
#     desired_column = 1
#     desired_row = int(no_mail)
#     with open(_path, 'r') as file:
#         reader = csv.reader(file)
    
#         for i, row in enumerate(reader) :
#             if i == desired_row - 1 :
#                 desired_data = row[desired_column]
#                 if desired_data == 'yet' :
#                     return False
#                 else :
#                     return True
                
                
# if handle__mail_status(1) :
#     print("Read")
# else:
#     print("Unread")









# from pathlib import Path

# # Lấy đường dẫn tuyệt đối của tệp hiện tại
# current_file_path = Path(__file__).resolve()

# print("Đường dẫn tệp hiện tại:", current_file_path)
# import csv

# def change__status(no_mail) :
#     _path = './app/email/data/box/status.csv'
    
#     pause_list = []
#     with open(_path, 'r+') as file :
#         reader = csv.reader(file)
#         for lines in reader :
#             pause_list.append(lines)
#         pause_list[no_mail - 1][1] = 'read'
        
#     with open(_path, 'w', newline="") as file :
#         reader = csv.writer(file)
#         for pri in pause_list :
#             reader.writerow(pri)
        
        

# change__status(3)











# def get_data(count__mail : int) :
#     if count__mail == 0 :
#         return
    
#     i = int(1)
#     folder_path = "./app/email/appcache/cache"
#     for filename in os.listdir(folder_path) :
#         if i > count__mail :
#             if os.path.isfile(os.path.join(folder_path, filename)) and ".txt" in filename :
#                 cup_filterdata(filename)
        
#         i = i + 1









# from tkinter import *
# root = Tk()
# txt = Text(root, spacing3 = 100, width = 50)
# txt.insert('0.1',"My name is Abhishek Bhardwaj")
# txt.pack()

# #get() method of text widget
# x = txt.get('5.7')            
# print(x)                      

# root.mainloop()











from tkinter import *
root = Tk()
txt = Text(root, spacing3 = 100, width = 50)
txt.insert('1.0', "My name is Abhishek Bhardwaj")
txt.pack()

#get() method of text widget
x = txt.get('1.0', '1.5') # 1.3 is in form x.y where x being line number and y being char number ON THAT LINE
print(x)

root.mainloop()