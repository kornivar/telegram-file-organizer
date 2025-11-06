import shutil
from pathlib import Path
from model import FileModel
from frontend import ConsoleView, GUIView

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

        # Model returned an error message.
        if isinstance(files, str):
            self.view.show_message(files)
            return files

        # Empty list
        if not files:
            msg = f"In the folder '{path}' There are no files to sort."
            self.view.show_message(msg)
            return msg

        moved = 0
        skipped = 0

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

            try:
                shutil.move(str(file), str(target_dir / file.name))
                moved += 1
            except Exception as e:
                skipped += 1
                self.view.show_message(f"Error moving {file.name}: {e}")
                continue

        result = {'moved': moved, 'skipped': skipped}
        self.view.show_result(result)
        return result

    def run(self):
        if self.view_type == "console":
            path = self.view.ask_directory()
            return self.sort_files(path)
        else:
            self.view.run()
            return None