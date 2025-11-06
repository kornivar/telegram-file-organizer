import shutil
from pathlib import Path
from model import FileModel
from view import ConsoleView, GUIView

class FileController:
    def __init__(self, view_type="console"):
        self.view_type = view_type

        if view_type == "console":
            self.view = ConsoleView()
        else:
            self.view = GUIView(self)

    def sort_files(self, path=None):
        if not path:
            path = self.view.ask_directory()

        model = FileModel(path)
        files = model.get_files()

        #  Not found or is not a directory.
        if isinstance(files, str):
            # The model returned an error message.
            if self.view_type == "console":
                self.view.show_message(files)
            else:
                self.view.show_message(files)
            return files

        else:
            # If the list is empty
            if not files:
                msg = f"In the folder '{path}' There are no files to sort."
                if self.view_type == "console":
                    self.view.show_message(msg)
                else:
                    self.view.show_message(msg)
                return msg
            else:
                # Sorting and moving files
                for file in files:
                    ext = file.suffix.lower()

                    if ext in ['.jpg', '.png', '.jpeg']:
                        target_dir = Path(path) / "Images"
                    elif ext in ['.mp4', '.avi', '.mov']:
                        target_dir = Path(path) / "Videos"
                    elif ext in ['.pdf', '.docx', '.txt']:
                        target_dir = Path(path) / "Documents"
                    else:
                        target_dir = Path(path) / "Others"

                    target_dir.mkdir(exist_ok=True)

                    # Attempt to move file
                    try:
                        shutil.move(str(file), str(target_dir / file.name))
                    except Exception as e:
                        error_message = f"Error during movement {file.name}: {e}"
                        if self.view_type == "console":
                            self.view.show_message(error_message)
                        else:
                            self.view.show_message(error_message)
                        return error_message

                success_message = f"Files from '{path}' Successfully sorted!"
                if self.view_type == "console":
                    self.view.show_message(success_message)
                else:
                    self.view.show_message(success_message)
                return success_message

    def run(self):
        if self.view_type == "console":
            path = self.view.ask_directory()
            result = self.sort_files(path)
            return result
        else:
            self.view.run()
            return None