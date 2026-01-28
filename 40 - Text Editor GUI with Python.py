import tkinter as tk
from tkinter import filedialog, messagebox

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Python Text Editor")
root.geometry("800x600")

file_path = None

# ---------------- Functions ----------------
def new_file():
    global file_path
    if text_area.get("1.0", tk.END).strip():
        if not messagebox.askyesno("New File", "Discard current text?"):
            return
    text_area.delete("1.0", tk.END)
    file_path = None
    root.title("Python Text Editor - New File")

def open_file():
    global file_path
    path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if path:
        file_path = path
        with open(path, "r", encoding="utf-8") as file:
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, file.read())
        root.title(f"Python Text Editor - {path}")

def save_file():
    global file_path
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get("1.0", tk.END))
    else:
        save_as()

def save_as():
    global file_path
    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if path:
        file_path = path
        save_file()
        root.title(f"Python Text Editor - {path}")

def update_status(event=None):
    text = text_area.get("1.0", tk.END)
    words = len(text.split())
    chars = len(text) - 1
    status_bar.config(text=f"Words: {words} | Characters: {chars}")

# ---------------- Menu Bar ----------------
menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# ---------------- Text Area ----------------
text_area = tk.Text(root, wrap="word", font=("Consolas", 12))
text_area.pack(expand=True, fill="both")

scroll = tk.Scrollbar(text_area)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
scroll.config(command=text_area.yview)
text_area.config(yscrollcommand=scroll.set)

# ---------------- Status Bar ----------------
status_bar = tk.Label(root, text="Words: 0 | Characters: 0", anchor="w")
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

text_area.bind("<KeyRelease>", update_status)

# ---------------- Shortcuts ----------------
root.bind("<Control-n>", lambda e: new_file())
root.bind("<Control-o>", lambda e: open_file())
root.bind("<Control-s>", lambda e: save_file())

root.mainloop()
