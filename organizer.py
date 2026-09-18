Python


import os
import shutil
from datetime import datetime

# Path to the directory you want to clean up
TARGET_DIR = os.path.expanduser("~/Downloads")
LOG_FILE = "cleanup_log.txt"

# File type mappings
EXTENSIONS = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Archives": [".zip", ".tar", ".gz", ".7z"],
    "Executables": [".exe", ".msi", ".dmg"]
}

def organize_folder():
    if not os.path.exists(TARGET_DIR):
        print(f"Target directory {TARGET_DIR} does not exist.")
        return

    with open(LOG_FILE, "a") as log:
        log.write(f"\n--- Run Started: {datetime.now()} ---\n")
        
        for filename in os.listdir(TARGET_DIR):
            file_path = os.path.join(TARGET_DIR, filename)
            
            if os.path.isfile(file_path) and filename != LOG_FILE:
                ext = os.path.splitext(filename)[1].lower()
                moved = False
                
                for folder_name, ext_list in EXTENSIONS.items():
                    if ext in ext_list:
                        dest_folder = os.path.join(TARGET_DIR, folder_name)
                        os.makedirs(dest_folder, exist_ok=True)
                        shutil.move(file_path, os.path.join(dest_folder, filename))
                        log.write(f"Moved: {filename} -> {folder_name}/\n")
                        moved = True
                        break
                
                if not moved and ext != "":
                    dest_folder = os.path.join(TARGET_DIR, "Other")
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    log.write(f"Moved: {filename} -> Other/\n")

if __name__ == "__main__":
    organize_folder()
    print("Cleanup complete! Check cleanup_log.txt for details.")
