import os
from tkinter import Tk, filedialog
import shutil

def select_directory():
    root = Tk()
    root.withdraw()#sekrit hide main window, didnt know about this function
    folder_path = filedialog.askdirectory(title="Select Directory")
    return folder_path

def organize_files(directory):
    extensions = {}

    for filename in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, filename)):
            continue
        file_extension = os.path.splitext(filename)[1].lower() #get file xext

        if file_extension not in extensions:
            extensions[file_extension] = os.path.join(directory, file_extension[1:]+ "_files") # add _file ext and make folders for types 
            os.makedirs(extensions[file_extension], exist_ok=True)
        src = os.path.join(directory, filename)
        dst = os.path.join(extensions[file_extension], filename)
        shutil.move(src,dst) #mov files, src to dst

    print("Files have been organzied sucessfully!")

if __name__=="__main__":
    directory = select_directory()
    if directory:
        organize_files(directory)
    
