# Day 36 of python with programming paglu🎀

# What we'll Learn:
# Access folders using os

# Move files with shutil

# Detect file types by extension

# Sort files into folders (Images, Docs, Videos, etc.)


# File Sorter

import os
import shutil

# 📁 Folder to clean
source_folder = "E:/YourMessyFolder"  # <-- change this

# 📁 Folder types
file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Docs": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"],
}

# 🚀 Go through each file
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file)[1].lower()

        moved = False
        for folder, extensions in file_types.items():
            if file_ext in extensions:
                folder_path = os.path.join(source_folder, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, file))
                moved = True
                break

        if not moved:
            others_folder = os.path.join(source_folder, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, file))

print("✅ All files have been sorted!")


# # Delete Empty Folders

# for item in os.listdir(source_folder):
#     item_path = os.path.join(source_folder, item)
#     if os.path.isdir(item_path) and not os.listdir(item_path):
#         os.rmdir(item_path)
#         print(f"🧹 Deleted empty folder: {item}")
