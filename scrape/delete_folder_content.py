import os
import make_logs

def delete_folder_contents(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    try:
        # Iterate over each file inside the specified folder
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                os.remove(item_path)  # Delete the file
                #log = make_logs.log_type.DELETE_HTMLS
                #make_logs.log_type.DELETE_HTMLS(log)
        print(f"\nAll contents inside '{folder_path}' have been deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")



new_files_path = "html-files"
old_files_path = "html-files/old-html-files"
if __name__ == "__main__":
    delete_folder_contents(new_files_path)
    delete_folder_contents(old_files_path)
    

