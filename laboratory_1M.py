import tkinter as tk
from tkinter import ttk
class Computer:
    def __init__(self, pc_number, pc_type):
        self.pc_number = pc_number
        self.pc_type = pc_type
class Queue:
    def __init__(self, name):
        self.queue = []
        self.total_pc_number = 40
        self.name = name
    
    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) > 0:
            self.queue.pop(0)

    def shape(self):
        return [self.name, self.total_pc_number - len(self.queue), len(self.queue)]
def log_in():
    global screen
    if username_entry.get() == "admin" and password_entry.get() == "admin":
        error_label.forget()
        log_in_frame.forget()
        dashboard_frame.pack()
    else:
        error_label.pack()
def dashboard_switch(screen):
    if screen == 0:
        dashboard_frame.pack()
        lab_stat_frame.forget()
    elif screen == 1:
        dashboard_frame.forget()
        lab_stat_frame.pack()

# Initializing Variables
clab1 = Queue('Comp Lab1')
clab2 = Queue('Comp Lab2')
clab3 = Queue('Comp Lab3')
maclab = Queue('Mac Lab')
rooms = [clab1, clab2, clab3, maclab]
# End of Initializing Variables
root = tk.Tk()
root.title("Laboratory Inventory")
root.geometry("300x500")
screen = "Log in"

# Log In Frame Start
log_in_frame = tk.Frame(root)
frame_header = tk.Frame(log_in_frame, padx= 10)
frame_header.pack()
welcome_label = tk.Label(frame_header, text="Welcome to the\nLaboratory Inventory!", font=("Monospace", 15, 'bold'))
welcome_label.pack(pady=10)

frame_body = tk.Frame(log_in_frame, padx = 10, pady= 30)
frame_body.pack()

login_label = tk.Label(frame_body, text= "Log in", font=("Monospace", 15, 'bold'))
login_label.pack()

username_label = tk.Label(frame_body, text= "Username:", font=("Monospace", 10, 'bold'), anchor='w')
username_label.pack(fill="x")
username_entry = tk.Entry(frame_body, width=30, justify= "left")
username_entry.pack(pady=5)

password_label = tk.Label(frame_body, text= "Password:", font=("Monospace", 10, 'bold'), anchor='w')
password_label.pack(fill="x")
password_entry = tk.Entry(frame_body, width=30, justify= "left", show= "*")
password_entry.pack(pady=5)

get_button = tk.Button(log_in_frame, text="Log in", command=log_in, font=("Monospace", 15, 'bold'), bg='gray')
get_button.pack(fill="x" , pady=10, padx= 20)
error_label = tk.Label(log_in_frame, text= "Account not found.", font=("Monospace", 12, 'bold'), fg= 'red')
log_in_frame.pack()
# Log In Frame End

# Dashboard Frame Start
dashboard_frame = tk.Frame(root)
dashboard_label = tk.Label(dashboard_frame, text="Dashboard", font=("Monospace", 18, 'bold'))
dashboard_label.pack(pady= 30)
frame_top = tk.Frame(dashboard_frame, padx= 20, pady= 100)
status_btn = tk.Button(frame_top, text= "Laboratory\nStatus", font=("Monospace", 12, 'bold'), width= 10, height= 3, command=lambda : dashboard_switch(1))
status_btn.pack(side="left", padx= 5)

report_btn = tk.Button(frame_top, text= "Report", font=("Monospace", 12, 'bold'), width= 10, height= 3)
report_btn.pack(side="left", padx= 5)
frame_top.pack()

frame_bottom = tk.Frame(dashboard_frame, padx= 20)
inventory_btn = tk.Button(frame_bottom, text= "Inventory", font=("Monospace", 12, 'bold'), width= 10, height= 3)
inventory_btn.pack(side="left", padx= 5)
logout_btn = tk.Button(frame_bottom, text= "Log out", font=("Monospace", 12, 'bold'), width= 10, height= 3)
logout_btn.pack(side="left", padx= 5)
frame_bottom.pack()
# Dashboard Frame End

# Laboratory Status Frame Start
lab_stat_frame = tk.Frame(root)
lab_stat_label = tk.Label(lab_stat_frame, text="Laboratory Status", font=("Monospace", 18, 'bold'))
lab_stat_label.pack(pady= 20)

columns = ("Room", "Working", "Broken")
lab_treeview = ttk.Treeview(lab_stat_frame, columns= columns, show= 'headings')
style = ttk.Style()
lab_treeview.heading("Room", text = "Room")
lab_treeview.heading("Working", text = "Number of \nWorking PC")
lab_treeview.heading("Broken", text = "Number of \nBroken PC")

style.configure("Treeview.Heading", font=("Monospace", 6, "bold"),)

lab_treeview.column("Room", width= 100, anchor= 'center')
lab_treeview.column("Working", width= 100, anchor= 'center')
lab_treeview.column("Broken", width= 100, anchor= 'center')
lab_treeview_data = (tuple(room.shape()) for room in rooms)

for item in lab_treeview_data:
    lab_treeview.insert("", tk.END, values= item)

lab_treeview.pack(pady = 10)

go_back_btn = tk.Button(lab_stat_frame, text= "Go Back", command= lambda: dashboard_switch(0))
go_back_btn.pack(padx= 10, pady= 10)


# Laboratory Status Frame End

# Run the application
root.mainloop()
