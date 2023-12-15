import re
import tkinter as tk
import socket
import json
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import os

# ./SE01SP/app/email
# ./SE01SP/app/mail/package/email.py


#download : ./SE01SP/app/email/appcache/download/
account = 'tranhoangkimngan@example.com'

FORMAT="utf8"


SELECT ="select"
EXIT="exit"
SENT="sent"
VIEW="view"


CUSTOMFONT4=("",60)
CUSTOMFONT=("",45)
CUSTOMFONT1=("",12)
CUSTOMFONT2=("", 10)
CUSTOMFONT3=("", 30)


class EmailConfig:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        with open(self.config_file) as f:
            self.config = json.load(f)

    def get_smtp_config(self):
        smtp_config = self.config['SMTP']
        smtp_host = smtp_config['host']
        smtp_port = smtp_config['port']
        return smtp_host, smtp_port
    
    
    def get_pop3_config(self):
        return self.config['POP3']


class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.frame1 = tk.Frame(self, bg="papayawhip", width=666, height=600)
        self.frame1.grid(row=0, column=0)

        self.frame2 = tk.Frame(self, bg="slategray", width=402, height=600)
        self.frame2.grid(row=0, column=1)

        label_title = tk.Label(self.frame1, text="EMAIL CLIENT", font=CUSTOMFONT4, bg="papayawhip", fg="firebrick")
        label_option1 = tk.Label(self.frame2, text="1.Send mail", font=CUSTOMFONT1, bg="slategray", fg="snow")
        label_option2 = tk.Label(self.frame2, text="2.View the list of received emails", font=CUSTOMFONT1, bg="slategray", fg="snow")
        label_option3 = tk.Label(self.frame2, text="3.Exit", font=CUSTOMFONT1, bg="slategray", fg="snow")
        label_notice = tk.Label(self.frame2, text="Select 1 option", font=CUSTOMFONT1, bg="slategray", fg="snow")

        self.label_notice = tk.Label(self.frame2, text="", fg="yellow", bg="slategray", font=CUSTOMFONT2)
        self.entry_select = tk.Entry(self.frame2, width=28, bg='ghostwhite', font=CUSTOMFONT1, fg="darkslategray")

        btn_select = tk.Button(self.frame2, text="SELECT", bg="moccasin", fg='maroon',
                               command=lambda: controller.select(self, client), font=CUSTOMFONT1)
        btn_select.configure(width=8)

        label_title.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        label_option1.place(relx=0.22, rely=0.17, anchor=tk.CENTER)
        label_option2.place(relx=0.4, rely=0.21, anchor=tk.CENTER)
        label_option3.place(relx=0.165, rely=0.25, anchor=tk.CENTER)
        label_notice.place(relx=0.16, rely=0.57, anchor=tk.CENTER)
        self.entry_select.place(relx=0.35, rely=0.62, anchor=tk.CENTER)
        self.label_notice.place(relx=0.12, rely=0.67, anchor=tk.CENTER)

        btn_select.place(relx=0.83, rely=0.62, anchor=tk.CENTER)

class ComposeMail (tk.Frame):
    def __init__ (self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="slategray")
        label_to=tk.Label(self,text="To: ",font=CUSTOMFONT1, bg="slategray", fg="snow")
        label_Cc=tk.Label(self,text="Cc: ", font=CUSTOMFONT1,  bg="slategray", fg="snow")
        label_Bcc=tk.Label(self,text="Bcc: ",font=CUSTOMFONT1,  bg="slategray", fg="snow")
        label_content=tk.Label(self,text="Content: ",font=CUSTOMFONT1,  bg="slategray", fg="snow")
        label_file=tk.Label(self,text="Attached File: ",font=CUSTOMFONT1, bg="slategray", fg="snow")
        label_subject=tk.Label(self,text="Subject: ",font=CUSTOMFONT1, bg="slategray", fg="snow")
        
        
        
        self.label_notice = tk.Label(self,text="",bg="papayawhip",fg="maroon")
        self.entry_to=tk.Entry(self,width=100,bg="papayawhip", font=CUSTOMFONT1)
        self.entry_Cc=tk.Entry(self,width=100,bg="papayawhip",font=CUSTOMFONT1)
        self.entry_Bcc=tk.Entry(self,width=100,bg="papayawhip",font=CUSTOMFONT1)
        self.entry_content = tk.Text(self, width=110, height=12, wrap=tk.WORD, font=CUSTOMFONT1, bg="papayawhip")
        self.entry_file=tk.Text(self, width=110, height=4.5, wrap=tk.WORD, font=CUSTOMFONT1, bg="papayawhip")
        self.entry_file.bind("<Button-1>", lambda event: self.on_entry_file_click())
        self.entry_sub=tk.Entry(self,width=100,bg="papayawhip",font=CUSTOMFONT1)
        
        btn_sent = tk.Button(self,text="SENT", bg="papayawhip",fg='maroon',command=lambda: controller.sent(self, client), font=CUSTOMFONT1)
        btn_sent.configure(width=10)
        btn_back= tk.Button(self,text="BACK", bg="papayawhip",fg='maroon',command=lambda: controller.back(self, client), font=CUSTOMFONT1)
        btn_back.configure(width=10)
        
        #Xuat cac thanh ra
        label_to.place(relx=0.05, rely=0.05, anchor=tk.CENTER)
        label_Cc.place(relx=0.05, rely=0.1, anchor=tk.CENTER)
        label_Bcc.place(relx=0.05, rely=0.15, anchor=tk.CENTER)
        label_content.place(relx=0.05, rely=0.25, anchor=tk.CENTER)
        label_subject.place(relx=0.05,rely=0.2,anchor=tk.CENTER)
        label_file.place(relx=0.07, rely=0.7,anchor=tk.CENTER)
        self.label_notice.place(relx=0.1, rely=0.94, anchor=tk.CENTER)
        self.entry_to.place(relx=0.1, rely=0.05, anchor=tk.W)
        self.entry_Cc.place(relx=0.1, rely=0.1, anchor=tk.W)
        self.entry_Bcc.place(relx=0.1, rely=0.15, anchor=tk.W)
        self.entry_sub.place(relx=0.1,rely=0.2,anchor=tk.W)
        self.entry_content.place(relx=0.48, rely=0.47, anchor=tk.CENTER)
        self.entry_file.place(relx=0.015,rely=0.82,anchor=tk.W)
        
        image_path = "image_file.png"
        self.image_label = tk.Label(self, bg="mintcream", fg="maroon")
        self.display_image(image_path)
        self.image_label.place(relx=0.13, rely=0.7, anchor=tk.CENTER)  # Adjust the placement if needed

        btn_sent.place(relx=0.85, rely=0.95, anchor=tk.W)
        btn_back.place(relx=0.73,rely=0.95,anchor=tk.W)
        
    def on_entry_file_click(self):
    # Hiển thị hộp thoại xác nhận và gọi hộp thoại chọn tệp khi xác nhận
        confirm = tk.messagebox.askyesno("Confirmation", "Do you want to attach file?")
        if confirm:
            file_paths = filedialog.askopenfilenames()
        # Xử lý các đường dẫn file được chọn
            if file_paths:
            # Lấy đường dẫn đầu tiên (nếu bạn muốn hiển thị nhiều đường dẫn, bạn có thể xử lý nó một cách phù hợp)
                selected_paths = ", ".join(file_paths)
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
    def __init__ (self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="slategray")
        label_notice = tk.Label (self,text="Email sent successfully !",font=CUSTOMFONT, bg="slategray", fg="khaki")
        
        btn_exit = tk.Button(self,text="EXIT", bg="papayawhip",fg='maroon',command=lambda: controller.out(), font=CUSTOMFONT1)
        btn_exit.configure(width=10)
        btn_menu = tk.Button(self,text="MENU", bg="papayawhip",fg='maroon',command=lambda: controller.menu(self, client), font=CUSTOMFONT1)
        btn_menu.configure(width=10)
        
        #Xuat ra
        label_notice.place(relx=0.5, rely=0.6, anchor=tk.CENTER)  
        btn_menu.place(relx=0.4, rely=0.74, anchor=tk.CENTER)
        btn_exit.place(relx=0.6, rely=0.74, anchor=tk.CENTER)
        image_path = "complete.png"
        self.image_label = tk.Label(self, bg="slategray", fg="maroon")
        self.display_image(image_path)
        self.image_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)  # Adjust the placement if needed
        
        
    def display_image(self, file_path):
        # Đọc hình ảnh từ đường dẫn và thay đổi kích thước nếu cần
        image_path = os.path.abspath(file_path)
        image = Image.open(image_path)
        image.thumbnail((1700, 1700))

        # Tạo PhotoImage từ hình ảnh để hiển thị trong Label
        tk_image = ImageTk.PhotoImage(image)
        self.image_label.config(image=tk_image)
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

        # Tạo Label để hiển thị Subject cho frame2
        self.subject_label_frame2 = tk.Label(self.frame2, text="Subject: ", bg="maroon", fg="white", cursor="hand2")
        self.subject_label_frame2.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.subject_label_frame2.bind("<Button-1>", self.show_subject_info_frame3)

        # Tạo Text widget để hiển thị nội dung file cho frame3
        self.file_content_text_frame3 = tk.Text(self.frame3, wrap='word', bg="slategray", fg="white")
        self.file_content_text_frame3.grid(row=1, column=0, sticky="nsew")

        # Tạo Scrollbar cho Text widget trong frame3
        self.text_scrollbar_frame3 = tk.Scrollbar(self.frame3, command=self.file_content_text_frame3.yview)
        self.text_scrollbar_frame3.grid(row=1, column=1, sticky="ns")

        # Kết nối Scrollbar với Text widget trong frame3
        self.file_content_text_frame3.config(yscrollcommand=self.text_scrollbar_frame3.set)

        # Tạo Label để hiển thị Subject cho frame3
       # Tạo Label để hiển thị Subject cho frame3
        self.subject_label_frame3 = tk.Label(self.frame3, text="Subject: ", bg="slategray", fg="white", cursor="hand2")
        self.subject_label_frame3.grid(row=0, column=0, sticky="w", padx=10, pady=5)


        # Cấu hình grid cho frame2 và frame3
        self.frame2.grid_columnconfigure(0, weight=1)
        self.frame2.grid_rowconfigure(1, weight=1)
        self.frame3.grid_columnconfigure(0, weight=1, minsize=100)

        # Tạo nút bấm trong frame1
        btn_option1 = tk.Button(self.frame1, text="1. Inbox", command=lambda: self.show_file_contents("D:\\22CTT4\\Namhai\\HK1 23-24\\MMT\\TH\\mail-sample-01.txt"), width=100, fg="maroon", bg="navajowhite")
        btn_option2 = tk.Button(self.frame1, text="2. Project", command=lambda: self.show_files("D:\\22CTT4\\Namhai\\HK1 23-24\\MMT\\TH\\Báo Cáo"), width=100, fg="maroon", bg="navajowhite")
        btn_option3 = tk.Button(self.frame1, text="3. Important", command=lambda: self.show_files("D:\\22CTT4\\Namhai\\HK1 23-24\\XSTK (TH)\\BTVN Week2"), width=100, fg="maroon", bg="navajowhite")
        btn_option4 = tk.Button(self.frame1, text="4. Work", command=lambda: self.show_page("Page 4"), width=100, fg="maroon", bg="navajowhite")
        btn_option5 = tk.Button(self.frame1, text="5. Spam", command=lambda: self.show_page("Page 5"), width=100, fg="maroon", bg="navajowhite")

        # Sắp xếp nút bấm
        btn_option1.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
        btn_option2.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        btn_option3.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        btn_option4.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        btn_option5.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
        
        

            
    def show_file_contents(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Xóa n
                self.file_content_text_frame2.delete('1.0', tk.END)
                # Hiển thị nội dung mới
                #self.file_content_text_frame2.insert(tk.END, content)

                # Hiển thị Subject trong frame2
                subject = self.extract_subject(file_path)
                self.subject_label_frame2.config(text=f"Subject: {subject}")  
        except Exception as e:
            print(f"Lỗi khi đọc file: {e}")

    def extract_subject(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    # Sử dụng regex để tìm kiếm giá trị của Subject
                    match = re.search(r'Subject: (.+)', line)
                    if match:
                        return match.group(1)
        except FileNotFoundError:
            print(f"Tệp {file_path} không tồn tại.")
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}")

    def show_subject_info_frame3(self, event):
    # Lấy tên Subject từ frame2
        subject_text = self.subject_label_frame2.cget('text')
        self.subject_label_frame3.config(text=f"{subject_text}")

    # Hiển thị thông tin chi tiết về Subject trong frame3
        subject_info = "\n\n"

    # Đọc và hiển thị toàn bộ nội dung từ file trong frame3
        file_path = "D:\\22CTT4\\Namhai\\HK1 23-24\\MMT\\TH\\mail-sample-01.txt"  # Thay đổi đường dẫn file nếu cần
        with open(file_path, 'r', encoding='utf-8') as file:
                content = file.readlines()

        # Xác định index của dòng chứa subject
        start_index = next((i for i, line in enumerate(content) if subject_text in line), None)

        if start_index is not None:
            # Loại bỏ dòng chứa subject
            content.pop(start_index)

            # Kiểm tra xem file có ít hơn 2 dòng không
        if len(content) >= 2:
                # Loại bỏ hai dòng cuối cùng
            content = content[:-2]

            # Nối lại thành chuỗi
        cleaned_content = ''.join(content)
        subject_info += cleaned_content.strip()

        self.file_content_text_frame3.delete('1.0', tk.END)
        self.file_content_text_frame3.insert(tk.END, subject_info)
             # Inside the __init__ method
        n = self.count_lines_until_blank(file_path)

        # Create a list to store Label instances and data from the last n lines
        subject_labels_frame3 = []
        last_n_lines_data = []

        # Get the last n lines from the file
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                last_n_lines_data = lines[-n:]
                for i in range(n):
                    subject_label = tk.Button(self.frame3, text=f"{last_n_lines_data[i]}", bg="papayawhip", fg="maroon")
                    subject_label.place(relx=0.15 + i * 0.3, rely=0.88, anchor=tk.CENTER)
                    subject_labels_frame3.append(subject_label)
        except Exception as e:
            print(f"Lỗi khi đọc file: {e}")

        # Create and place labels based on the count
                
                
    def count_lines_until_blank(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            # Start counting from the end of the file
                count = 0
                for line in reversed(lines):
                    if line.strip():  # Check if the line is not blank
                        count += 1
                    else:
                        break  # Break the loop when a blank line is encountered

            return count
        except Exception as e:
            print(f"Lỗi khi đọc file: {e}")
            return 0
        

              
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Email Client")
        self.geometry("1068x600")
        self.resizable(width=False, height=False)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MenuPage, ComposeMail, CompleteSent, OptionOfView):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

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
            print(f"Error: {str(e)}")
    def sent(self, currFrame, sck):
        try:
            to = currFrame.entry_to.get()
            cc = currFrame.entry_Cc.get()
            bcc = currFrame.entry_Bcc.get()
            content = currFrame.entry_content.get("1.0", "end-1c")
            sub=currFrame.entry_sub.get()
            
            
            if to == "" and cc == "" and bcc == "":
                currFrame.label_notice["text"] = "Fields cannot be empty"
                return

            # Tiến hành gửi mail về server
            #Gui mail xong
            self.showFrame(CompleteSent)
            currFrame.entry_to.delete(0,tk.END)
            currFrame.entry_Cc.delete(0,tk.END)
            currFrame.entry_Bcc.delete(0,tk.END)
            currFrame.entry_sub.delete(0,tk.END)
            currFrame.entry_content.delete("1.0", tk.END)
            currFrame.label_notice["text"] = ""
        except Exception as e: 
            currFrame.label_notice["text"] = f"Error: {str(e)}"
            print(f"Error: {str(e)}")
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
        


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

email_config=EmailConfig()
HOST, PORT=email_config.get_smtp_config()
server_address = (HOST, PORT)

client.connect(server_address)


app = App()



#main
try:
    app.mainloop()
except:  # noqa: E722
    print("Error: Server is not responding")
    client.close()

finally:
    client.close()



