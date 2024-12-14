import os

def rename_files(directory):
    """Renames files in a directory sequentially.

    Args:
        directory: The directory path.
    """

    file_list = os.listdir(directory)
    file_list.sort()  # Sort files alphabetically

    for i, file_name in enumerate(file_list):
        source = os.path.join(directory, file_name)
        destination = os.path.join(directory, f"{i+1}.jpg")  # Replace .jpg with your desired extension
        os.rename(source, destination)

# Replace 'TEST' with the actual directory name
directory_path = "/home/ashwathama/Documents/GitHub/agritech/On-tree mature coconut fruit detection.v1i.multiclass/valid"

rename_files(directory_path)