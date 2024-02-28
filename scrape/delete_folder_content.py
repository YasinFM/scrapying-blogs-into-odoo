import os

def delete_folder_contents(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    try:
        # Iterate over each file/folder inside the specified folder
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                os.remove(item_path)  # Delete the file
            elif os.path.isdir(item_path):
                # If it's a directory, delete it recursively
                delete_folder_contents(item_path)
                os.rmdir(item_path)  # Then remove the empty directory
        print(f"All contents inside '{folder_path}' have been deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

folder_path = "html-files"
if __name__ == "__main__":
    delete_folder_contents(folder_path)
