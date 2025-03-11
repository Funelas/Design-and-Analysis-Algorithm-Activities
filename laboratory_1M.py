import tkinter as tk
from tkinter import ttk
class Computer:
    def __init__(self, pc_number, pc_type):
        self.pc_number = pc_number
        self.pc_type = pc_type
class Queue:
    def __init__(self, name = ""):
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
        lab_stat_frame.forget()
        report_frm.forget()
        dashboard_frame.pack()
    elif screen == 1:
        dashboard_frame.forget()
        lab_stat_frame.pack()
    elif screen == 2:
        dashboard_frame.forget()
        report_frm.pack()
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        self.stack.pop()
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

report_btn = tk.Button(frame_top, text= "Report", font=("Monospace", 12, 'bold'), width= 10, height= 3, command=lambda: dashboard_switch(2))
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

def report(source):
    global report_stack
    if source == 5:
        report_type_frm.forget()
        report_frm.pack()
        report_broken_frm.forget()
        report_stack.pop()
    elif source == 1:
        report_frm.forget()
        report_type_frm.forget()
        report_broken_frm.pack()
        report_stack.push(source)
    elif source == 6:
        report_frm.forget()
        report_broken_frm.forget()
        report_stack.pop()
        report_type_frm.pack()
    else:
        report_frm.forget()
        report_type_frm.pack()
        report_stack.push(source)

# Report Frame Start
report_stack = Stack()
report_frm = tk.Frame(root)
clab1_btn = tk.Button(report_frm, text= "Comp Lab 1", font=("Monospace", 12, 'bold'), command=lambda: report(0), width= 40, height= 3)
clab1_btn.pack(fill= "x", padx= 5, pady= 10)
clab2_btn = tk.Button(report_frm, text= "Comp Lab 2", font=("Monospace", 12, 'bold'), command=lambda: report(1), width= 40, height= 3)
clab2_btn.pack(fill= "x", padx= 5, pady= 10)
clab3_btn = tk.Button(report_frm, text= "Comp Lab 3", font=("Monospace", 12, 'bold'), command=lambda: report(2), width= 40, height= 3)
clab3_btn.pack(fill= "x", padx= 5, pady= 10)
maclab_btn = tk.Button(report_frm, text= "Mac Lab", font=("Monospace", 12, 'bold'), command=lambda: report(3), width= 40, height= 3)
maclab_btn.pack(fill= "x", padx= 5, pady= 10)
report_goback_btn = tk.Button(report_frm, text= "Go back", font=("Monospace", 12, 'bold'), command=lambda: dashboard_switch(0), width= 40, height= 3)
report_goback_btn.pack(fill="x", padx= 20, pady= 50)

## Complete or Broken Frame Start ##
report_type_frm = tk.Frame(root)
report_fix_btn = tk.Button(report_type_frm, text= "Report Fix", font=("Monospace", 12, 'bold'), height= 3, width= 20)
report_fix_btn.pack(fill="x", padx= 20, pady= 50)
report_broken_btn = tk.Button(report_type_frm, text= "Report Broken", font=("Monospace", 12, 'bold'), height= 3, width= 20, command= lambda: report(1))
report_broken_btn.pack(fill="x", padx= 20, pady= 50)
report_type_goback_btn = tk.Button(report_type_frm, text= "Go back", font=("Monospace", 12, 'bold'), command=lambda: report(5), height= 3, width= 20)
report_type_goback_btn.pack(fill="x", padx= 20, pady= 50)
## Complete or Broken Frame End ##

def submit():
    global dropdown_value, pc_number_entry, rooms, report_stack
    if dropdown_value.get() and pc_number_entry_value.get():
        rooms[report_stack.stack[0]].enqueue(Computer(pc_number_entry_value.get(), dropdown_value.get()))
        report_broken_error_label.forget()
        report_broken_success_label.pack(pady = 10)
        pc_number_entry_value.set("")
        dropdown_value.set("")
    else:
        report_broken_success_label.forget()
        report_broken_error_label.pack(pady = 10)
### Report Broken Frame Start ###
report_broken_frm = tk.Frame(root)
report_broken_label = tk.Label(report_broken_frm, text= "Report Broken PC", font=("Monospace", 15, 'bold'))
report_broken_label.pack(pady= 20)
pc_number_label = tk.Label(report_broken_frm, text= "PC Number: ", font=("Monospace", 10, 'bold'), anchor='w')
pc_number_label.pack(fill="x")
pc_number_entry_value = tk.StringVar()
pc_number_entry = tk.Entry(report_broken_frm, width=30, justify= "left", textvariable= pc_number_entry_value)
pc_number_entry.pack(pady=5)

pc_type_label = tk.Label(report_broken_frm, text= "PC Type: ", font=("Monospace", 10, 'bold'), anchor='w')
pc_type_label.pack(fill="x")
dropdown_value = tk.StringVar()
dropdown = ttk.Combobox(report_broken_frm, textvariable= dropdown_value, state="readonly")
dropdown['values'] = ("Windows Computer", "Macintosh Computer")
dropdown.pack(pady= 10)
report_broken_submit_btn = tk.Button(report_broken_frm, text= "Submit", font=("Monospace", 12, 'bold'), command=submit, height= 3, width= 20)
report_broken_submit_btn.pack(fill="x", padx= 20, pady= 25)
report_broken_goback_btn = tk.Button(report_broken_frm, text= "Go back", font=("Monospace", 12, 'bold'), command=lambda: report(6), height= 3, width= 20)
report_broken_goback_btn.pack(fill="x", padx= 20, pady= 25)
report_broken_error_label = tk.Label(report_broken_frm, text= "Please fill out all\nnecessary information", font=("Monospace", 8, 'bold'), fg= 'red')
report_broken_success_label = tk.Label(report_broken_frm, text= "Record submitted.", font=("Monospace", 8, 'bold'), fg= 'green')
### Report Broken Frame End ###
# Report Frame End
# Run the application
root.mainloop()
