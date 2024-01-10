# Library - Python
import tkinter as tk
import os
import re
import socket
import time
import threading

from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from pathlib import Path



# ./SE01SP/ins/
# ./SE01SP/manual/HDSD.docx

# ./SE01SP/app/
# ./SE01SP/app/server/test-mail-server.jar
# ./SE01SP/app/email/package/
import _config
import handle__compose
import handle_file
import standby_state




# Download Cache: ./SE01SP/app/email/appcache/download/
# Download Box Mail : ./SE01SP/app/email/data/box/




# Settings
FORMAT = "utf8"
  
SELECT = "select"
EXIT = "exit"
SENT = "sent"
VIEW = "view"

CUSTOMFONT  = ("",45)
CUSTOMFONT1 = ("",12)
CUSTOMFONT2 = ("", 10)
CUSTOMFONT3 = ("", 30)
CUSTOMFONT4 = ("",60)




# application function
# config 
# settings
# options
# main function
# test




# class program
class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.frame1 = tk.Frame(self, bg = "papayawhip", width = 666, height = 600)
        self.frame1.grid(row = 0, column = 0)

        self.frame2 = tk.Frame(self, bg = "slategray", width = 402, height = 600)
        self.frame2.grid(row = 0, column = 1)

        label_title = tk.Label(self.frame1, text = "EMAIL CLIENT", font = CUSTOMFONT4, bg = "papayawhip", fg = "firebrick")
        label_option1 = tk.Label(self.frame2, text = "1.Send mail", font = CUSTOMFONT1, bg = "slategray", fg = "snow")
        label_option2 = tk.Label(self.frame2, text = "2.View the list of received emails", font = CUSTOMFONT1, bg = "slategray", fg = "snow")
        label_option3 = tk.Label(self.frame2, text = "3.Exit", font = CUSTOMFONT1, bg = "slategray", fg = "snow")
        label_notice = tk.Label(self.frame2, text = "Select 1 option", font = CUSTOMFONT1, bg = "slategray", fg = "snow")

        self.label_notice = tk.Label(self.frame2, text = "", fg = "yellow", bg = "slategray", font = CUSTOMFONT2)
        self.entry_select = tk.Entry(self.frame2, width = 28, bg = 'ghostwhite', font = CUSTOMFONT1, fg = "darkslategray")

        btn_select = tk.Button(self.frame2, text = "SELECT", bg = "moccasin", fg = 'maroon', command = lambda: controller.select(self, client), font = CUSTOMFONT1)
        btn_select.configure(width = 8)

        label_title.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
        label_option1.place(relx = 0.22, rely = 0.17, anchor = tk.CENTER)
        label_option2.place(relx = 0.4, rely = 0.21, anchor = tk.CENTER)
        label_option3.place(relx = 0.165, rely = 0.25, anchor = tk.CENTER)
        label_notice.place(relx = 0.16, rely = 0.57, anchor = tk.CENTER)
        self.entry_select.place(relx = 0.35, rely = 0.62, anchor = tk.CENTER)
        self.label_notice.place(relx = 0.12, rely = 0.67, anchor = tk.CENTER)

        btn_select.place(relx = 0.83, rely = 0.62, anchor = tk.CENTER)


class ComposeMail (tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = "slategray")
        label_to = tk.Label(self, text = "To: ", font = CUSTOMFONT1, bg = "slategray", fg = "snow")
        label_Cc = tk.Label(self, text = "Cc: ", font = CUSTOMFONT1, bg = "slategray", fg = "snow")
        label_Bcc = tk.Label(self, text = "Bcc: ", font = CUSTOMFONT1, bg = "slategray", fg = "snow")
        label_content = tk.Label(self, text = "Content: ", font = CUSTOMFONT1, bg = "slategray", fg = "snow")
        label_file = tk.Label(self, text = "Attached File: ", font = CUSTOMFONT1, bg = "slategray", fg = "snow")
        label_subject = tk.Label(self, text = "Subject: ", font = CUSTOMFONT1, bg = "slategray", fg = "snow")
        
              
        self.label_notice = tk.Label(self, text = "",bg = "papayawhip", fg = "maroon")
        self.entry_to = tk.Entry(self, width = 100, bg = "papayawhip", font = CUSTOMFONT1)
        self.entry_Cc = tk.Entry(self, width = 100, bg = "papayawhip", font = CUSTOMFONT1)
        self.entry_Bcc = tk.Entry(self, width = 100, bg = "papayawhip", font = CUSTOMFONT1)
        self.entry_content = tk.Text(self, width = 110, height = 12, wrap = tk.WORD, font = CUSTOMFONT1, bg = "papayawhip")
        self.entry_file = tk.Text(self, width = 110, height = 4.5, wrap = tk.WORD, font = CUSTOMFONT1, bg = "papayawhip")
        self.entry_file.bind("<Button-1>", lambda event: self.on_entry_file_click())
        self.entry_sub = tk.Entry(self, width = 100, bg = "papayawhip", font = CUSTOMFONT1)
        
        btn_sent = tk.Button(self, text = "SENT", bg = "papayawhip", fg = 'maroon', command = lambda: controller.sent(self, client), font = CUSTOMFONT1)
        btn_sent.configure(width = 10)
        btn_back = tk.Button(self, text = "BACK", bg = "papayawhip", fg = 'maroon', command = lambda: controller.back(self, client), font = CUSTOMFONT1)
        btn_back.configure(width = 10)
        
        #Xuat cac thanh ra
        label_to.place(relx = 0.05, rely = 0.05, anchor = tk.CENTER)
        label_Cc.place(relx = 0.05, rely = 0.1, anchor = tk.CENTER)
        label_Bcc.place(relx= 0.05, rely = 0.15, anchor = tk.CENTER)
        label_content.place(relx = 0.05, rely = 0.25, anchor = tk.CENTER)
        label_subject.place(relx = 0.05, rely = 0.2, anchor = tk.CENTER)
        label_file.place(relx = 0.07, rely = 0.7, anchor = tk.CENTER)
        self.label_notice.place(relx = 0.1, rely = 0.94, anchor = tk.CENTER)
        self.entry_to.place(relx = 0.1, rely = 0.05, anchor = tk.W)
        self.entry_Cc.place(relx = 0.1, rely = 0.1, anchor = tk.W)
        self.entry_Bcc.place(relx = 0.1, rely = 0.15, anchor = tk.W)
        self.entry_sub.place(relx = 0.1, rely = 0.2, anchor = tk.W)
        self.entry_content.place(relx = 0.48, rely = 0.47, anchor = tk.CENTER)
        self.entry_file.place(relx = 0.015, rely = 0.82, anchor = tk.W)
        
        image_path = "./app/email/graphics/gra-set_file.png"
        self.image_label = tk.Label(self, bg = "mintcream", fg = "maroon")
        self.display_image(image_path)
        self.image_label.place(relx = 0.13, rely = 0.7, anchor = tk.CENTER)  # Adjust the placement if needed

        btn_sent.place(relx = 0.85, rely = 0.95, anchor = tk.W)
        btn_back.place(relx = 0.73, rely = 0.95, anchor = tk.W)
        
    def on_entry_file_click(self):
    # Hiển thị hộp thoại xác nhận và gọi hộp thoại chọn tệp khi xác nhận
        confirm = tk.messagebox.askyesno("Confirmation", "Do you want to attach file?")
        if confirm:
            file_paths = filedialog.askopenfilenames()
        # Xử lý các đường dẫn file được chọn
            if file_paths :
            # Lấy đường dẫn đầu tiên (nếu bạn muốn hiển thị nhiều đường dẫn, bạn có thể xử lý nó một cách phù hợp)
                selected_paths = ", ".join(file_paths)
                
                
                _selected_list_path = selected_paths.split(', ')
                _path_list = []
                for _path in _selected_list_path :
                    file_size =  handle_file.get_file_size(_path) / (1024 * 1024)
                    if file_size <= 3 :
                        _path_list.append(_path)
                selected_paths = ""
                for _path in _path_list :
                    selected_paths += str(_path) + ", "
                
            # Hiển thị đường dẫn trong entry_file
                self.entry_file.delete('1.0', tk.END)  # Xóa nội dung hiện tại (nếu có)
                self.entry_file.insert(tk.END, selected_paths)  # Chèn đường dẫn mới
                            
    def display_image(self, file_path):
        # Đọc hình ảnh từ đường dẫn và thay đổi kích thước nếu cần
        image_path = os.path.abspath(file_path)
        image = Image.open(image_path)
        image.thumbnail((22, 22))

        # Tạo PhotoImage từ hình ảnh để hiển thị trong Label
        tk_image = ImageTk.PhotoImage(image)
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image  # Giữ tham chiếu để ngăn hình ảnh bị thu hồi bởi garbage collector


class CompleteSent (tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = "slategray")
        label_notice = tk.Label(self, text = "Email sent successfully !", font = CUSTOMFONT, bg = "slategray", fg = "khaki")
        
        btn_exit = tk.Button(self, text = "EXIT", bg = "papayawhip", fg = 'maroon', command = lambda: controller.out(), font = CUSTOMFONT1)
        btn_exit.configure(width = 10)
        btn_menu = tk.Button(self, text = "MENU", bg = "papayawhip", fg = 'maroon', command = lambda: controller.menu(self, client), font = CUSTOMFONT1)
        btn_menu.configure(width = 10)
        
        # Imput
        label_notice.place(relx = 0.5, rely = 0.6, anchor = tk.CENTER)  
        btn_menu.place(relx = 0.4, rely = 0.74, anchor = tk.CENTER)
        btn_exit.place(relx = 0.6, rely = 0.74, anchor = tk.CENTER)
        image_path = "./app/email/graphics/gra-gui_send.webp"
        self.image_label = tk.Label(self, bg = "slategray", fg = "maroon")
        self.display_image(image_path)
        self.image_label.place(relx = 0.5, rely = 0.25, anchor = tk.CENTER)  # Adjust the placement if needed
                
    def display_image(self, file_path):
        # Đọc hình ảnh từ đường dẫn và thay đổi kích thước nếu cần
        image_path = os.path.abspath(file_path)
        image = Image.open(image_path)
        image.thumbnail((1700, 1700))

        # Tạo PhotoImage từ hình ảnh để hiển thị trong Label
        tk_image = ImageTk.PhotoImage(image)
        self.image_label.config(image = tk_image)
        self.image_label.image = tk_image  # Giữ tham chiếu để ngăn hình ảnh bị thu hồi bởi garbage collector
        

class OptionOfView(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # Khởi tạo Frame
        self.frame1 = tk.Frame(self, bg="papayawhip", width=160, height=600)
        self.frame1.grid(row=0, column=0, sticky="ns")

        self.canvas = tk.Canvas(self, bg="maroon", width=256, height=600)
        self.canvas.grid(row=0, column=1, sticky="nsew")

        self.frame3 = tk.Frame(self, bg="slategray", width=652, height=600)
        self.frame3.grid(row=0, column=2, sticky="nsew")

        # Tạo Frame container trong Canvas
        self.frame2 = tk.Frame(self.canvas, bg="maroon")  # Đặt màu nền để khớp với canvas
        self.canvas.create_window((0, 0), window=self.frame2, anchor="nw", width=256, height=600)

        # Tạo Text widget để hiển thị nội dung file cho frame2
        self.file_content_text_frame2 = tk.Text(self.frame2, wrap='word', bg="maroon", fg="lightyellow")
        self.file_content_text_frame2.grid(row=1, column=0, sticky="nsew")

        # Tạo Scrollbar cho Text widget trong frame2
        self.text_scrollbar_frame2 = tk.Scrollbar(self.frame2, command=self.file_content_text_frame2.yview)
        self.text_scrollbar_frame2.grid(row=1, column=1, sticky="ns")

        # Kết nối Scrollbar với Text widget trong frame2
        self.file_content_text_frame2.config(yscrollcommand=self.text_scrollbar_frame2.set)

        # Tạo Text widget để hiển thị nội dung file cho frame3
        self.file_content_text_frame3 = tk.Text(self.frame3, wrap='word', bg="slategray", fg="white")
        self.file_content_text_frame3.grid(row=1, column=0, sticky="nsew")

        # Tạo Scrollbar cho Text widget trong frame3
        self.text_scrollbar_frame3 = tk.Scrollbar(self.frame3, command=self.file_content_text_frame3.yview)
        self.text_scrollbar_frame3.grid(row=1, column=1, sticky="ns")

        # Kết nối Scrollbar với Text widget trong frame3
        self.file_content_text_frame3.config(yscrollcommand=self.text_scrollbar_frame3.set)

        # Cấu hình grid cho frame2 và frame3
        self.frame2.grid_columnconfigure(0, weight=1)
        self.frame2.grid_rowconfigure(1, weight=1)
        self.frame3.grid_columnconfigure(0, weight=1, minsize=100)
        
        # Tao nut bam trong frame1
        btn_option1 = tk.Button(self.frame1, text="Inbox", command=lambda: self.show_file_and_status('./app/email/data/box/inbox'), width=100, fg="maroon", bg="navajowhite")
        btn_option2 = tk.Button(self.frame1, text="Important", command=lambda: self.show_file_and_status('./app/email/data/box/important'), width=100, fg="maroon", bg="navajowhite")
        btn_option3 = tk.Button(self.frame1, text="Work", command=lambda: self.show_file_and_status('./app/email/data/box/work'), width=100, fg="maroon", bg="navajowhite")
        btn_option4 = tk.Button(self.frame1, text="Spam", command=lambda: self.show_file_and_status('./app/email/data/box/spam'), width=100, fg="maroon", bg="navajowhite")
        
        # Sort 
        btn_option1.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
        btn_option2.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        btn_option3.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        btn_option4.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        
        self.notification_update()

        # BACK
        btn_back = tk.Button(self.frame1, text = "BACK", command = lambda: controller.menu(self, client), width=100, fg="maroon", bg="navajowhite")
        btn_back.configure(width = 10)
        btn_back.place(relx = 0.5, rely = 0.4, anchor = tk.CENTER)
    
    def notification_update(self) :
        _flag = handle_file.handle__notification_update('check')
        if _flag == True :
            notification = tk.Label(self.frame1, text="There is new mail !!!", width=100, fg="maroon", bg="yellow")
            notification.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
            # self.frame1.after(30 * 1000, notification.place_forget())
            handle_file.handle__notification_update('change')
        
    def create_button(self, path_folder, _filename) :
        show_name = handle_file.get_file_subject(path_folder + '/' + _filename)
        
        no_mail = handle_file.get_file_name(_filename)
        no_mail = no_mail[:(len(no_mail) - 4)]
        flag = standby_state.handle__mail_status(no_mail)
        if flag :
            show_name += " (Read)"
        else :
            show_name += " (Unread)"
        
        return tk.Button(self.frame2, text=show_name, command=lambda: self.show_file_content(path_folder, _filename), width=100, fg="maroon", bg="navajowhite")
        
    def show_file_and_status(self, path_folder) :
         
        self.frame2 = tk.Frame(self.canvas, bg="maroon")  # Đặt màu nền để khớp với canvas
        self.canvas.create_window((0, 0), window=self.frame2, anchor="nw", width=256, height=600)
        
        
        list_name_file = []
        
        for filename in os.listdir(path_folder) :
            if os.path.isfile(os.path.join(path_folder, filename)) :
                if filename != 'permanent.tmp' :
                    list_name_file.append(filename)
        
        btn_file = [self.create_button(path_folder, value) for value in list_name_file]
        i = int(1)
        for pri in btn_file :
            pri.place(relx=0.5, rely=(0.05 * i), anchor=tk.CENTER)
            i = i + 1
    
    def show_file_content(self, path_folder, path_file) :
        _path = path_folder + "/" + path_file
        
        self.frame3 = tk.Frame(self, bg="slategray", width=652, height=600)
        self.frame3.grid(row=0, column=2, sticky="nsew")
        self.subject_label_frame3 = ""
        
        self.show_file_and_status(path_folder)
        str_data = handle_file.handle__read(_path)
        no_mail = handle_file.get_file_name(path_file)
        no_mail = no_mail[:(len(no_mail) - 4)]
        standby_state.change__status(no_mail)
        
        self.subject_label_frame3 = tk.Label(self.frame3, text=str_data, font=CUSTOMFONT2, bg="slategray", fg="white")
        self.subject_label_frame3.place(relx=0.1, rely=0.2, anchor=tk.W)


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Email Client")
        self.geometry("1068x600")
        self.resizable(width = False, height = False)

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (MenuPage, ComposeMail, CompleteSent, OptionOfView):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.frames[MenuPage].tkraise()

    def showFrame(self, container):
        frame = self.frames[container]
        if container == MenuPage:
            self.geometry("1068x600")
        elif container == ComposeMail:
            self.geometry("1068x600")
        else:
            self.geometry("1068x600")
        frame.tkraise()

    def select(self, currFrame, sck):
        try:
            option = currFrame.entry_select.get()
            currFrame.entry_select.delete(0,tk.END)
            if option == "" or option not in ["1", "2", "3"]:
                currFrame.label_notice["text"] = "Invalid value"
                return
            if option == "1":
                self.showFrame(ComposeMail)
            elif option == "3":
                self.out()
            elif option == "2":
                self.showFrame(OptionOfView)

        except Exception as e:
            currFrame.label_notice["text"] = f"Error: {str(e)}"
            print(f"Error: (432) {str(e)}")
    
    def sent(self, currFrame, sck):
        try:
            str_to_mail = currFrame.entry_to.get()
            str_cc_mail = currFrame.entry_Cc.get()
            str_bcc_mail = currFrame.entry_Bcc.get()
            str_content = currFrame.entry_content.get('1.0', tk.END)
            str_subject = currFrame.entry_sub.get()
            str_file_path = currFrame.entry_file.get('1.0', tk.END)

            to_mail = str_to_mail.split(',')
            cc_mail = str_cc_mail.split(',')
            bcc_mail = str_bcc_mail.split(',')
            content = str_content[:(len(str_content) - 1)]
            subject = str_subject
             
            str_file_path = str_file_path[:(len(str_file_path) - 1)]
            file_path = str_file_path.split(', ')
            if file_path[len(file_path) - 1] == '' or file_path[len(file_path) - 1] == ' ' :
                file_path.pop()
            
            if str_to_mail == "" and str_cc_mail == "" and str_bcc_mail == "":
                currFrame.label_notice["text"] = "Fields cannot be empty"
                return
            
            # connected
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((_config.handle_config.get_smtp('server'), _config.handle_config.get_smtp('port')))
            handle__compose.email__compose(client, to_mail, cc_mail, bcc_mail, subject, content, file_path)
            client.close()
            
            # Tiến hành gửi mail về server
            # Gui mail xong
            self.showFrame(CompleteSent)
            currFrame.entry_to.delete(0,tk.END)
            currFrame.entry_Cc.delete(0,tk.END)
            currFrame.entry_Bcc.delete(0,tk.END)
            currFrame.entry_sub.delete(0,tk.END)
            currFrame.entry_content.delete("1.0", tk.END)
            currFrame.label_notice["text"] = ""
        except Exception as e: 
            currFrame.label_notice["text"] = f"Error: {str(e)}"
            print(f"Error: (467) {str(e)}")
    
    def out(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()
            try:
                option = EXIT
                client.sendall(option.encode(FORMAT))
            except:  # noqa: E722
                pass
    
    def menu (self, currFrame, sck):
        self.showFrame(MenuPage)
    
    def back(self, currFrame, sck):
        currFrame.entry_to.delete(0,tk.END)
        currFrame.entry_Cc.delete(0,tk.END)
        currFrame.entry_Bcc.delete(0,tk.END)
        currFrame.entry_sub.delete(0,tk.END)
        currFrame.entry_content.delete("1.0", tk.END)
        currFrame.label_notice["text"] = ""        
        self.showFrame(MenuPage)
    
    def view(self,currFrame,sck):
        try:
            select=currFrame.entry_select.get()
            currFrame.entry_select.delete(0,tk.END)
            if select == "" or select not in ["1","2","3","4","5"]:
                currFrame.label_notice["text"] = "Invalid value"
                return
        except Exception as e: 
            currFrame.label_notice["text"] = f"Error: {str(e)}"
            print(f"Error: {str(e)}")




# build socket
# connecting...
# sign-in account
# running app
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client.connect((_config.handle_config.get_pop3('server'), _config.handle_config.get_pop3('port')))
_config.sign_in_to_server(client)
time.sleep(0.03)
client.close()




def program_App() :
    # main function
    app = App()
    try:
        app.mainloop()
    except:
        print("Error: Server is not responding")
        client.close()
    finally:
        client.close()
        
def program_updateBox() :
    time_update = int(_config.handle_config.update_autoload('autoload'))
    while True :
        # Update Box
        exec(open('./app/email/package/navigation_update.py').read())
        time.sleep(time_update)




thread__app = threading.Thread(target=program_App)
thread__update = threading.Thread(target=program_updateBox)


thread__app.start()
thread__update.start()


thread__app.join()
thread__update.join()



