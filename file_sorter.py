import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

# Function to sort files based on user-defined types
def sort_files(source_directory, file_types):
    # Check if the source directory exists
    if not os.path.exists(source_directory):
        messagebox.showerror("Error", "The specified directory does not exist.")
        return

    # Create subdirectories for each file type
    for folder in file_types.keys():
        folder_path = os.path.join(source_directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to their respective folders
    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(source_directory, folder, filename))
                    moved = True
                    break
            if not moved:
                print(f"File type not recognized: {filename}")

    messagebox.showinfo("Success", "Files sorted successfully!")

# Function to select a directory and sort files
def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        # Get user-defined file types
        file_types = get_file_types()
        if file_types:
            sort_files(directory, file_types)

# Function to get user-defined file types
def get_file_types():
    file_types = {}
    while True:
        folder_name = simpledialog.askstring("Input", "Enter folder name for file type (or 'done' to finish):")
        if folder_name is None or folder_name.lower() == 'done':
            break
        extensions = simpledialog.askstring("Input", f"Enter file extensions for '{folder_name}' (comma-separated, e.g., .jpg,.png):")
        if extensions:
            ext_list = [ext.strip() for ext in extensions.split(',')]
            file_types[folder_name] = ext_list
    return file_types

# Create the main window
root = tk.Tk()
root.title("User -Defined File Sorter")
root.geometry("300x150")

# Create a label
label = tk.Label(root, text="Select a directory to sort files:")
label.pack(pady=20)

# Create a button to select the directory
button = tk.Button(root, text="Select Directory", command=select_directory)
button.pack(pady=10)

# Start the GUI event loop
root.mainloop()