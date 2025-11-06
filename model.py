print("Hello Model") 
print("Hello Model") 
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