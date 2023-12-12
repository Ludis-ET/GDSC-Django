import os
import shutil
from datetime import datetime, timedelta

def list_files(directory="../"):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def is_recently_modified_or_created(file_path):
    current_time = datetime.now()
    file_stat = os.stat(file_path)
    time_diff = current_time.timestamp() - max(file_stat.st_mtime, file_stat.st_ctime)
    return time_diff < 24 * 3600

def update_file(file_path):
    with open(file_path, 'a') as f:
        f.write('\nUpdated at: ' + str(datetime.now()))

def create_last_24hours_folder():
    folder_name = "last_24hours"
    folder_path = os.path.join(os.getcwd(), folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def move_file_to_last_24hours(file_path):
    destination_folder = os.path.join(os.getcwd(), "last_24hours", os.path.basename(file_path))
    shutil.move(file_path, destination_folder)

def main():
    files = list_files()

    recent_files = [file for file in files if is_recently_modified_or_created(file)]

    if not recent_files:
        print("No recently modified or created files found.")
        return

    create_last_24hours_folder()

    for file in recent_files:
        file_path = os.path.join(os.getcwd(), file)
        update_file(file_path)
        move_file_to_last_24hours(file_path)

    print("Files updated and moved to 'last_24hours' folder.")

print(list_files())
