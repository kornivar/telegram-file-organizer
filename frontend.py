import tkinter as tk
from tkinter import filedialog, messagebox

class ConsoleView:
    def ask_directory(self):
        return input("Enter the path to the Telegram folder: ")

    def show_message(self, message):
        print(f"[INFO] {message}")

    def show_result(self, result):
        print(f"Files moved: {result.get('moved', 0)}, missed: {result.get('skipped', 0)}")


class GUIView:
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
        # controller will call view.show_result/show_message
        self.controller.sort_files(self.selected_path)


        
    def show_message(self, message):
        messagebox.showinfo("Information", message)


    def show_result(self, result):
        messagebox.showinfo(
            "Result",
            f"Files moved: {result['moved']}, missed: {result['skipped']}"
        )

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    """
    Entry point when running `frontend.py` directly.

    Usage:
      python frontend.py            -> tries GUI, falls back to console on error
      python frontend.py gui|g      -> force GUI
      python frontend.py console|c  -> force console
    """
    import sys

    arg = sys.argv[1].lower() if len(sys.argv) > 1 else None

    # Import controller inside the guard to avoid circular import problems at module import time.
    try:
        from controller import FileController
    except Exception as e:
        print(f"[ERROR] Cannot import controller: {e}")
        raise

    if arg in ("console", "c"):
        FileController(view_type="console").run()
    else:
        # default: try GUI, fall back to console if GUI initialization fails
        try:
            FileController(view_type="gui").run()
        except Exception as e:
            print(f"[WARN] GUI failed ({e}), falling back to console mode.")
            FileController(view_type="console").run()
