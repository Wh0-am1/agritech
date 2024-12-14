import os

def rename_files(directory):
    """Renames image files in a directory sequentially, starting from 1.

    Args:
        directory: The directory path.
    """
    
    # Get the list of image files (filter out directories) and sort them alphabetically
    try:
        file_list = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        file_list.sort()

        if not file_list:
            print("No files found in the directory.")
            return

        for i, file_name in enumerate(file_list):
            # Check the file extension
            extension = os.path.splitext(file_name)[1].lower()  # Ensure the extension is in lowercase
            
            # Proceed only if it's an image file (you can add more extensions if needed)
            if extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']:
                source = os.path.join(directory, file_name)
                destination = os.path.join(directory, f"{i+1}{extension}")  # Rename to 1.jpg, 2.png, etc.
                
                # Debug output to verify before renaming
                print(f"Attempting to rename: {source} -> {destination}")
                
                try:
                    os.rename(source, destination)
                    print(f"Renamed successfully: {source} -> {destination}")
                except Exception as e:
                    print(f"Error renaming {source} -> {destination}: {e}")
            else:
                print(f"Skipping non-image file: {file_name}")  # Debug print for non-image files

    except Exception as e:
        print(f"Error accessing directory {directory}: {e}")

# Replace with your actual directory path
directory_path = "/home/ashwathama/Documents/GitHub/agritech/Custom Dataset/Tender"
rename_files(directory_path)
