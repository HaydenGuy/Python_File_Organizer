#!/usr/bin/python3.10

import os
import sys

# Define a function to organize files in a directory based on their extensions
def file_organizer(directory):
    # Get a list of filenames in the directory and sort them
    files_list = [f for f in os.listdir(
        directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Define tuples of file extensions for different categories
    images = ('.jpg', '.png')
    text = ('.pdf', '.txt')
    video = ('.mp4', '.avi')
    production = ('.ai', '.ps', '.ae')

    for file in files_list:
        # Skip the script file itself to avoid unintended self-move
        if file == os.path.basename(__file__):
            continue

        # Split the filename and extension
        filename, extension = os.path.splitext(file)

        '''
            Organize files into corresponding directories based on their extensions
            Create the directory if it doesn't exist in the target directory
            Construct the target file path in the directory
            Rename (move) the file to the directory
        '''
        if extension in images:
            images_dir = os.path.join(directory, 'Images')
            if not os.path.exists(images_dir):
                os.mkdir(images_dir)
            target_file_path = os.path.join(images_dir, file)
            os.rename(os.path.join(directory, file), target_file_path)

        elif extension in text:
            documents_dir = os.path.join(directory, 'Documents')
            if not os.path.exists(documents_dir):
                os.mkdir(documents_dir)
            target_file_path = os.path.join(documents_dir, file)
            os.rename(os.path.join(directory, file), target_file_path)

        elif extension in video:
            videos_dir = os.path.join(directory, 'Videos')
            if not os.path.exists(videos_dir):
                os.mkdir(videos_dir)
            target_file_path = os.path.join(videos_dir, file)
            os.rename(os.path.join(directory, file), target_file_path)

        elif extension in production:
            production_dir = os.path.join(directory, 'Production')
            if not os.path.exists(production_dir):
                os.mkdir(production_dir)
            target_file_path = os.path.join(production_dir, file)
            os.rename(os.path.join(directory, file), target_file_path)


# Check if the script is run as the main program
if __name__ == "__main__":
    # Check if a target directory is provided as a command-line argument
    if len(sys.argv) > 1:
        target_directory = sys.argv[1]
    else:
        # If no directory is provided, use the current working directory
        target_directory = os.getcwd()

file_organizer(target_directory)