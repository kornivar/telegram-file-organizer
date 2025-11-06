import sys
from controller import FileSorterController
from view import CLIView, GUIView

def main():
    mode = "gui" if len(sys.argv) < 2 else sys.argv[1]

    if mode == "cli":
        view = CLIView()
        controller = FileSorterController(view)
        path = view.get_directory()
        controller.sort_files(path)
    else:
        controller = FileSorterController(None)
        view = GUIView(controller)
        controller.view = view
        view.run()

if __name__ == "__main__":
    main()
