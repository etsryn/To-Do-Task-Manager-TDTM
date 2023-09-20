import jsonSetup as jsSetup
import pyttsx3
import tkinter as tk
import cv2 
from tkinter import messagebox, ttk
from datetime import datetime
import pywhatkit as kit
import os

# Initialize Setups ---------------------------------------------------------------------------------------------------------
jsSetup.__init__64bit__ini()
jsSetup.__init__64bit_rp()
jsSetup.__init__64bit__dp()
def __init__64bit_():
    with open("temp.txt", "r") as f:
        __init__64bit_data = f.readlines()
    if os.path.exists("temp.txt"):
        os.remove("temp.txt")
    return [line.strip() for line in __init__64bit_data[:4]]
data__init__64bitMan = __init__64bit_()

# Initialize the main application window ---------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------
app = tk.Tk()
# ------------------------------------------------------------------------------------------------------------------------------------------------
    # Set the application's title
app.title(f"{data__init__64bitMan[0]}")
# ------------------------------------------------------------------------------------------------------------------------------------------------
    # Set the background color to black
app.configure(bg="black")
# ------------------------------------------------------------------------------------------------------------------------------------------------
    # Excludes the Minimizing and Maximizing Button
app.resizable(False, False)
# ------------------------------------------------------------------------------------------------------------------------------------------------
    # Put icon
app.iconbitmap("icon.ico")
# ------------------------------------------------------------------------------------------------------------------------------------------------
    # Coordinate of where the application will be launched first
app.geometry("+200+60")
# ------------------------------------------------------------------------------------------------------------------------------------------------
# Define a custom function to handle window close
def on_closing():
    if messagebox.askokcancel(f"{data__init__64bitMan[1]}", f"{data__init__64bitMan[2]}"):
        app.destroy()
app.protocol("WM_DELETE_WINDOW", on_closing)
# ------------------------------------------------------------------------------------------------------------------------------------------------
engine = pyttsx3.init()
# Set properties (optional)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# Text to be converted to speech
text = f"{data__init__64bitMan[3]}"
# ------------------------------------------------------------------------------------------------------------------------------------------------
# Function to capture intruder : (it requires several modification according to your device)
def start_camera():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        messagebox.showerror("Camera Error", "Failed to open laptop's built-in camera.")
        return

    ret, frame = cap.read()

    if not ret:
        messagebox.showerror("Camera Error", "Failed to capture a frame from the camera.")
    else:
        current_time = datetime.now().strftime("%d_%m_%Y__%H_%M_%S")
        filename = f"captured_intruder_{current_time}.jpg"
        cv2.imwrite(f"{filename}", frame)

    cap.release()
# ------------------------------------------------------------------------------------------------------------------------------------------------
# Function to execute whatsAap alert : ( it requires several setups in your own device )
def sendWPMsg():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    alert_message = f"There is an intruder trying to access your personal data at {hour} hour and {minute} minute"
    if minute==59:
        kit.sendwhatmsg("##########", alert_message, hour+1,1)
    else:
        kit.sendwhatmsg("##########", alert_message, hour,minute+2)

# Create a password entry dialog
def check_password():
    password = password_entry.get()
    if password == "******":
        password_dialog.destroy()
        engine.say(text)
        engine.runAndWait()
        app.deiconify()
    else:
        start_camera()
        # sendWPMsg() # Uncoment it if you want program to send whatsAap alert (it requires several setups in your own device)
        messagebox.showerror("Incorrect Password", "The password you entered is incorrect. Please try again.")

app.withdraw()

# Create the password dialog window
password_dialog = tk.Toplevel()
password_dialog.title("Password Protected")
password_dialog.geometry("300x150")
password_dialog.configure(bg="black")
password_dialog.iconbitmap("icon_2.ico")
password_dialog.resizable(False, False)

# Create a label and entry widget for the password
password_label = tk.Label(password_dialog, text="Enter Password", bg="black", fg="white", width=25)
password_label.pack(pady=10)
password_entry = tk.Entry(password_dialog, show="*")
password_entry.pack(pady=5)
password_button = tk.Button(password_dialog, text="Let Me In", command=check_password, bg="black", fg="white", width=15, height=1)
password_button.pack(pady=10)

# WINDOW SETTINGS TILL HERE-----------------------------------------------------------------------------------------------------------------------

# Create a list to store tasks as dictionaries
tasks = []

# Function to add a task
def add_task():
    load_tasks_1()
    remove_button.config(state='disabled')
    save_button.config(state='normal')
    load_button.config(state='disabled')
    status = "Pending"
    task = entry.get("1.0", tk.END)
    task = task.strip()
    if task:
        engine.say("Processing The Data On Console Terminal")
        engine.runAndWait()
        priority = priority_var.get()
        due_date = due_date_var.get()
        
        task_info = {
            "task": task,
            "priority": priority,
            "due_date": due_date,
            "completed": status
        }
        
        tasks.append(task_info)
        add_button.config(state='disabled')
        engine.say("Click on Save Tasks to add the data to data base")
        engine.runAndWait()
        update_listbox()
        entry.delete("1.0", tk.END) 
    else:
        clear_listbox()
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to load tasks from a file
def load_tasks_1():
    global tasks
    tasks = []
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_info = line.strip().split(" - ")
                if len(task_info) == 4:
                    task = task_info[0].split(":")[1].strip()
                    priority = task_info[1].split(":")[1].strip()
                    due_date = task_info[2].split(":")[1].strip()
                    completed = task_info[3].split(":")[1].strip()
                    tasks.append({
                        "task": task,
                        "priority": priority,
                        "due_date": due_date,
                        "completed": completed
                    })
        load_button.config(state='disabled')
        mark_completed_button.config(state='normal')
        remove_button.config(state='normal')
        save_button.config(state='disabled')
        clear_button.config(state='normal')
        update_listbox_1()
    except FileNotFoundError:
        pass

# Function to remove a task
def remove_task():
    save_button.config(state='normal')
    selected_task_index = listbox.curselection()
    if selected_task_index:
        index = int(selected_task_index[0])
        tasks.pop(index)
        engine.say("Kindly Click on Save Tasks To Complete the removing procedure")
        engine.runAndWait()
        update_listbox()

# Function to mark a task as completed
def mark_completed():
    engine.say("Assigning This task as Completed")
    engine.runAndWait()
    selected_task_index = listbox.curselection()
    save_button.config(state='normal')
    load_button.config(state='disabled')
    if selected_task_index:
        index = int(selected_task_index[0])
        tasks[index]["completed"] = "Completed"
        engine.say("Kindly Click on Save Tasks To Complete the completion procedure")
        engine.runAndWait()
        update_listbox()

# Function to clear all tasks
def clear_all_tasks():
    global tasks
    tasks = []
    load_button.config(state='disabled')
    save_button.config(state='normal')
    save_button.invoke()
    save_button.config(state='disabled')
    engine.say("Console and Text File is cleared")
    engine.runAndWait()
    update_listbox()

# Function to update the listbox with current tasks
def update_listbox():
    listbox.delete(0, tk.END)
    for task_info in tasks:
        task = task_info["task"]
        priority = task_info["priority"]
        due_date = task_info["due_date"]
        completed = task_info["completed"]
        
        if completed == "Completed":
            task = f"[Completed] {task}"
        
        listbox.insert(tk.END, f"Priority: {priority} - [Due Date: {due_date} - Task: {task} - Status: {completed}")

def save_tasks():
    with open("tasks.txt", "w") as file:
        if not load_button.cget("state") == "disabled"or add_button.cget("state") == "disabled":
            for task_info in tasks:
                file.write(f"Task Detail : {task_info['task']} - Task Priority : {task_info['priority']} - Due Date : {task_info['due_date']} - Status : {task_info['completed']}\n")
        else:
            for task_info in tasks:
                file.write(f"Task Detail : {task_info['task']} - Task Priority : {task_info['priority']} - Due Date : {task_info['due_date']} - Status : {task_info['completed']}\n")
    load_button.config(state='normal')
    add_button.config(state='normal')
    engine.say("Action Successfuly Executed")
    engine.runAndWait()
    clear_listbox()
    clear_button.config(state="disabled")

def clear_listbox():
    engine.say("Clearing Console Terminal")
    engine.runAndWait()
    listbox.delete(0, tk.END)
    save_button.config(state='disabled')
    mark_completed_button.config(state='disabled')
    remove_button.config(state='disabled')
    load_button.config(state='normal')

# Function to load tasks from a file
def load_tasks():
    clear_button.config(state="normal")
    engine.say("Fetching Data from Data base to Console Terminal")
    engine.runAndWait()
    global tasks
    tasks = []
    update_listbox()
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_info = line.strip().split(" - ")
                if len(task_info) == 4:
                    task = task_info[0].split(":")[1].strip()
                    priority = task_info[1].split(":")[1].strip()
                    due_date = task_info[2].split(":")[1].strip()
                    completed = task_info[3].split(":")[1].strip()
                    tasks.append({
                        "task": task,
                        "priority": priority,
                        "due_date": due_date,
                        "completed": completed
                    })
        load_button.config(state='disabled')
        mark_completed_button.config(state='normal')
        remove_button.config(state='normal')
        save_button.config(state='disabled')
        clear_button.config(state='normal')
        update_listbox()
    except FileNotFoundError:
        pass

# Function to update the listbox with current tasks
def update_listbox_1():
    listbox.delete(0, tk.END)
    for task_info in tasks:
        task = task_info["task"]
        priority = task_info["priority"]
        due_date = task_info["due_date"]
        completed = task_info["completed"]
        
        if completed == "Completed":
            task = f"[Completed] {task}"
        
        listbox.insert(tk.END, f"Priority: {priority} - Due Date: {due_date} - Task: {task} - [Status: {completed}")

# Create and configure widgets
# Create a frame to hold the Text widget and button vertically
frame = tk.Frame(app, bg="black")
frame.pack(pady=10)
frame = tk.LabelFrame(app, text="------------------------------------ User Input Text Field ------------------------------------", bg="black", fg="white", borderwidth=2, relief="solid", highlightbackground="white")
frame.pack(pady=(0, 1))

# Create a Text widget
entry = tk.Text(frame, font=("Helvetica", 10), bg="black", fg="white", height=2, width=62, border=10)
entry.pack(side=tk.TOP, padx=10, pady=20)



# Frame to hold "Priority" and "Due Date" in a rectangular box with a white border
def on_entry_focus_in(event):
    if due_date_var.get() == "dd/mm/yyyy":
        due_date_var.set("")

def on_entry_focus_out(event):
    if not due_date_var.get():
        due_date_var.set("dd/mm/yyyy")

# Create a label frame to hold the elements Priority and Due Date
selection_frame = tk.LabelFrame(app, text="\n---------------------------------- Priority and Due Date ----------------------------------\n", bg="black", fg="white", borderwidth=2, relief="solid", highlightbackground="white")
selection_frame.pack(pady=(0, 1))

# Priority elements
priority_label = tk.Label(selection_frame, text="Priority:", bg="black", fg="white")
priority_label.grid(row=0, column=0, padx=5)

priority_var = tk.StringVar(value="Please Choose")
priority_combobox = ttk.Combobox(selection_frame, textvariable=priority_var, values=["High", "Medium", "Low"])
priority_combobox.grid(row=0, column=1, padx=5)

# Due Date elements
due_date_label = tk.Label(selection_frame, text="Due Date:", bg="black", fg="white")
due_date_label.grid(row=0, column=2, padx=5)

due_date_var = tk.StringVar(value="dd/mm/yyyy")

due_date_entry = tk.Entry(selection_frame, textvariable=due_date_var)
due_date_entry.grid(row=0, column=3, padx=5)

due_date_entry.bind("<FocusIn>", on_entry_focus_in)
due_date_entry.bind("<FocusOut>", on_entry_focus_out)


# Center the label across columns
selection_frame.grid_columnconfigure(0, weight=1)
selection_frame.grid_columnconfigure(1, weight=1)
selection_frame.grid_columnconfigure(2, weight=1)
selection_frame.grid_columnconfigure(3, weight=1)

add_button = tk.Button(selection_frame, text="Add Task", width=12, command=add_task, bg="black", fg="white", cursor="hand2")  # Set button colors
add_button.grid(row=1, column=0, columnspan=4, pady=(35, 15), padx=10, sticky='ew')



# Frame to hold "Remove Task," "Mark Completed," and "Clear All Tasks" buttons horizontally
# Create a label frame for the "Remove Task," "Mark Completed," and "Clear All Tasks" section
button_frame = tk.LabelFrame(app, text="------------------------------------- Console Actions -------------------------------------\n", bg="black", fg="white", borderwidth=2, relief="solid", highlightbackground="white", cursor="hand2")
button_frame.pack(pady=(9, 0))

# Remove Task button
remove_button = tk.Button(button_frame, text="Remove Task", width=15, command=remove_task, bg="black", fg="white", cursor="hand2")
remove_button.pack(side=tk.LEFT, padx=(5, 10), fill=tk.X, expand=True)

# Mark Completed button
mark_completed_button = tk.Button(button_frame, text="Mark Completed", width=15, command=mark_completed, bg="black", fg="white", cursor="hand2")
mark_completed_button.pack(side=tk.LEFT, padx=(10, 5), fill=tk.X, expand=True)

# Clear List Box button
clear_button = tk.Button(button_frame, text="Clear Live Console", width=12, command=clear_listbox, bg="black", fg="white", cursor="hand2")
clear_button.pack(side=tk.LEFT, padx=(5, 10), fill=tk.X, expand=True)


# Create a label frame for the Listbox
listbox_frame = tk.LabelFrame(app, text="\n------------------------------------ Task Live Console ------------------------------------\n", bg="black", fg="white", borderwidth=2, relief="solid", highlightbackground="white")
listbox_frame.pack(pady=10)

# Listbox
listbox = tk.Listbox(listbox_frame, selectmode=tk.SINGLE, font=("Helvetica", 12), height=10, width=50, bg="black", fg="white")
listbox.pack(padx=10)

# Frame to hold "Load Tasks" and "Save Tasks" buttons horizontally at the bottom
footer_frame = tk.Frame(app, bg="black")
footer_frame.pack(side=tk.BOTTOM, pady=10)
footer_frame = tk.LabelFrame(app, text="\n--------------------------------------- File Actions ---------------------------------------\n", bg="black", fg="white", borderwidth=2, relief="solid", highlightbackground="white")
footer_frame.pack(pady=10)
load_button = tk.Button(footer_frame, text="Load Tasks", width=12, command=load_tasks, bg="black", fg="white", cursor="hand2")
load_button.pack(side=tk.LEFT, padx=(5, 10), fill=tk.X, expand=True)

save_button = tk.Button(footer_frame, text="Save Tasks", width=12, command=save_tasks, bg="black", fg="white", cursor="hand2")
save_button.pack(side=tk.LEFT, padx=(10, 5), fill=tk.X, expand=True)

# Clear All Tasks button
clear_all_button = tk.Button(footer_frame, text="Clear All Tasks", width=15, command=clear_all_tasks, bg="black", fg="white", cursor="hand2")
clear_all_button.pack(side=tk.LEFT, padx=(5, 10), fill=tk.X, expand=True)

# Load tasks on application startup
save_button.config(state='disabled')
clear_button.config(state='disabled')
remove_button.config(state='disabled')
mark_completed_button.config(state='disabled')
app.mainloop()

