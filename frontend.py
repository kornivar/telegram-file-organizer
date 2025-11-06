import tkinter as tk
from tkinter import filedialog, messagebox

class CLIView:
    
    """Console view."""

    def get_directory(self):
        return input("Enter the path to the Telegram folder: ")

    def show_message(self, message):
        print(f"[INFO] {message}")

    def show_result(self, result):
        print(f"Files moved: {result['moved']}, missed: {result['skipped']}")


class GUIView:

    """Graphical representation with Tkinter."""

    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Telegram File Sorter")

        tk.Label(self.root, text="Select the Telegram folder").pack(pady=10)
        tk.Button(self.root, text="Select folder", command=self.choose_folder).pack(pady=5)
        tk.Button(self.root, text="Sort", command=self.sort_files).pack(pady=5)

        self.path_label = tk.Label(self.root, text="")
        self.path_label.pack(pady=5)

        self.selected_path = None


    def choose_folder(self):
        path = filedialog.askdirectory()
        if path:
            self.selected_path = path
            self.path_label.config(text=f"Folder: {path}")


    def sort_files(self):
        if not self.selected_path:
            messagebox.showwarning("Error", "Select folder!")
            return
        self.controller.sort_files(self.selected_path)


        
    def show_message(self, message):
        messagebox.showinfo("Information", message)