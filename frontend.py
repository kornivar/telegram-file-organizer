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
