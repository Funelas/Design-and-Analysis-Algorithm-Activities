import tkinter as tk
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) > 0:
            self.queue.pop(0)
def log_in():
    global account_notfound
    if username_entry.get() == "admin" and password_entry.get() == "admin":
        print("Session on")
        error_label.forget()
    else:
        error_label.pack()


root = tk.Tk()
root.title("Tkinter Input Window")
root.geometry("300x500")

# Create Entry widget
frame_header = tk.Frame(root, padx= 10)
frame_header.pack()
welcome_label = tk.Label(frame_header, text="Welcome to the\nLaboratory Inventory!", font=("Monospace", 15, 'bold'))
welcome_label.pack(pady=10)

frame_body = tk.Frame(root, padx = 10, pady= 30)
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

# Create buttons
get_button = tk.Button(root, text="Log in", command=log_in, font=("Monospace", 15, 'bold'), bg='gray')
get_button.pack(fill="x" , pady=10, padx= 20)
error_label = tk.Label(root, text= "Account not found.", font=("Monospace", 12, 'bold'), fg= 'red')


# Run the application
root.mainloop()
