from pathlib import Path

class FileModel:
    """
    Simple model representing the source folder.
    get_files() returns a list of Path objects or an error string.
    """
    def __init__(self, source):
        self.source = Path(source)

    def get_files(self):
        files = []

        if self.source.exists() and self.source.is_dir():
            for item in self.source.iterdir():
                if item.is_file():
                    files.append(item)

            if files:
                return files
            else:
                return f"In the folder '{self.source}' No files."
        else:
            return f"Folder '{self.source}' Not found or is not a directory."