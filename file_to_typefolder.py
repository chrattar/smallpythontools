import os
from tkinter import Tk, filedialog
import shutil

#Select the directory to sort files\
def select_directory():
    root = Tk()
    root.withdraw() # Hide the main window
    folder_path = filedialog.askdirectory(title="Select Directory")
    return folder_path

def organize_files(directory):
    extensions = {}

    for filename in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, filename)):
            continue

        #Extract the extension
        file_extension = os.path.splitext(filename)[1].lower()

        #Creation for folders with the file type doesn't already exist
        #Add the additional "_file" suffix to the folder.
        if file_extension not in extensions:
            extensions[file_extension] = os.path.join(directory, file_extension[1:]+ "_files")
            os.makedirs(extensions[file_extension], exist_ok=True)

        #Move File to Correct Folders:
        src = os.path.join(directory, filename)
        dst = os.path.join(extensions[file_extension], filename)
        shutil.move(src,dst)

    print("Files have been organzied sucessfully!")

if __name__=="__main__":
    directory = select_directory()
    if directory:
        organize_files(directory)
    
