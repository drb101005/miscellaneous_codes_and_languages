import tkinter as tk
from tkinter import messagebox, filedialog

# Creates the main application window
root = tk.Tk()
root.title("Tkinter Full Reference")
root.geometry("600x600")
root.configure(bg="lightgray")
root.resizable(True, True)

# Variables for widgets (used with Entry, Checkbutton, etc.)
str_var = tk.StringVar()
int_var = tk.IntVar()

# -------------------------------
# 🖼️ Label (visible text on screen)
label = tk.Label(root, text="This is a Label", bg="white", fg="black")
label.pack(pady=5)  # Appears at the top

# -------------------------------
# ✍️ Entry field (single-line text input)
entry = tk.Entry(root, textvariable=str_var)
entry.pack(pady=5)  # Below the label

# -------------------------------
# 📝 Text widget (multi-line text box)
text_box = tk.Text(root, height=4, width=30)
text_box.pack(pady=5)  # Below the entry

# -------------------------------
# 🔘 Button (click to show Entry text)
def on_button_click():
    messagebox.showinfo("Info", f"You entered: {entry.get()}")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=5)

# -------------------------------
# ✅ Checkbutton (toggle option)
check = tk.Checkbutton(root, text="Check me", variable=int_var)
check.pack()  # Below the button

# -------------------------------
# 🔘 Radiobuttons (select one from multiple options)
radio1 = tk.Radiobutton(root, text="Option 1", value=1, variable=int_var)
radio2 = tk.Radiobutton(root, text="Option 2", value=2, variable=int_var)
radio1.pack()
radio2.pack()

# -------------------------------
# 🎚️ Scale widget (slider)
scale = tk.Scale(root, from_=0, to=100, orient='horizontal')
scale.pack()  # Horizontal slider

# -------------------------------
# 📋 Listbox (selectable list of items)
listbox = tk.Listbox(root)
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.pack()  # Appears below slider

# -------------------------------
# 📜 Scrollbar (scrollable Text widget)
frame = tk.Frame(root)
frame.pack()

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

text_with_scroll = tk.Text(frame, yscrollcommand=scrollbar.set, height=5)
text_with_scroll.pack(side="left")
scrollbar.config(command=text_with_scroll.yview)

# -------------------------------
# 🔢 Spinbox (numeric input)
spin = tk.Spinbox(root, from_=1, to=10)
spin.pack()  # Allows number selection

# -------------------------------
# 🎨 Canvas (drawing area with shapes and text)
canvas = tk.Canvas(root, width=200, height=100, bg="white")
canvas.create_line(0, 0, 200, 100, fill="blue")         # Diagonal line
canvas.create_rectangle(50, 10, 150, 90, outline="red") # Rectangle
canvas.create_oval(70, 20, 130, 80, fill="green")       # Oval
canvas.create_text(100, 50, text="Canvas")              # Center text
canvas.pack(pady=10)

# -------------------------------
# 🍔 Menu bar (File > Open/Exit)
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open File", command=lambda: filedialog.askopenfilename())
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# -------------------------------
# ⌨️ Key binding (prints key pressed to console)
def on_keypress(event):
    print(f"Key pressed: {event.char}")

root.bind("<Key>", on_keypress)  # Any key logs to console

# ⏎ Return key on Entry field
def on_return(event):
    print("Enter key was pressed")

entry.bind("<Return>", on_return)

# -------------------------------
# 📋 Clipboard copy button
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(entry.get())
    messagebox.showinfo("Clipboard", "Text copied to clipboard!")

clipboard_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
clipboard_btn.pack(pady=5)

# -------------------------------
# 🪟 Toplevel window (opens a new window)
def open_new_window():
    top = tk.Toplevel(root)
    top.title("New Window")
    tk.Label(top, text="This is a new window").pack()

toplevel_btn = tk.Button(root, text="Open New Window", command=open_new_window)
toplevel_btn.pack(pady=5)

# -------------------------------
# ⏰ .after() method (delay action for 2 sec)
def say_hello():
    messagebox.showinfo("After", "This message appears after 2 seconds")

root.after(2000, say_hello)  # Triggers after window starts

# -------------------------------
# ▶️ Start the GUI application loop
root.mainloop()
