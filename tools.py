import shutil
import subprocess
import os
from langsmith import traceable
@traceable
def create_vite_app(project_name: str, template: str = "react"):
    try:
        command = ['npm', 'create', 'vite@latest', project_name]
        if template:
            command += ['--template', template]
        
        print(f"Running command: {' '.join(command)}")
        subprocess.run(command, check=True)
        print("✅ Vite app created successfully.")
    
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in function create_vite_app: Command failed with exit code {e.returncode}")
    except Exception as e:
        print(f"❌ Unexpected error in function create_vite_app: {str(e)}")

@traceable
def run_command(command):
    try:
        result = os.system(command)
        return f"Command executed with exit code {result}"
    except Exception as e:
        return f"Error occurred while running command '{command}': {str(e)}"

@traceable
def make_directory(dir_name):
    try:
        os.mkdir(dir_name)
        return f"Directory '{dir_name}' created successfully"
    except Exception as e:
        return f"Error occurred while creating directory '{dir_name}': {str(e)}"


@traceable
def create_file(file_path, content=""):
    try:
        with open(file_path, "w") as file:
            file.write(content)
        return f"File '{file_path}' created successfully"
    except Exception as e:
        return f"Error occurred while creating file '{file_path}': {str(e)}"

@traceable
def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except Exception as e:
        return f"Error occurred while reading file '{file_path}': {str(e)}"

@traceable
def append_to_file(file_path, content):
    try:
        with open(file_path, "a") as file:
            file.write(content)
        return f"Content appended to '{file_path}' successfully"
    except Exception as e:
        return f"Error occurred while appending to file '{file_path}': {str(e)}"

@traceable
def delete_file(file_path):
    try:
        os.remove(file_path)
        return f"File '{file_path}' deleted successfully"
    except Exception as e:
        return f"Error occurred while deleting file '{file_path}': {str(e)}"

@traceable
def delete_directory(dir_path):
    try:
        shutil.rmtree(dir_path)
        return f"Directory '{dir_path}' deleted successfully"
    except Exception as e:
        return f"Error occurred while deleting directory '{dir_path}': {str(e)}"

@traceable
def list_files(dir_path):
    try:
        return os.listdir(dir_path)
    except Exception as e:
        return f"Error occurred while listing files in directory '{dir_path}': {str(e)}"

@traceable
def move_file(src_path, dest_path):
    try:
        shutil.move(src_path, dest_path)
        return f"Moved from '{src_path}' to '{dest_path}'"
    except Exception as e:
        return f"Error occurred while moving from '{src_path}' to '{dest_path}': {str(e)}"

@traceable
def path_exists(path):
    try:
        return os.path.exists(path)
    except Exception as e:
        return f"Error occurred while checking existence of path '{path}': {str(e)}"

@traceable
def rename_path(old_path, new_path):
    try:
        os.rename(old_path, new_path)
        return f"Renamed '{old_path}' to '{new_path}'"
    except Exception as e:
        return f"Error occurred while renaming '{old_path}' to '{new_path}': {str(e)}"

@traceable
def change_directory(directory_name):
    try:
        os.chdir(directory_name)
        return f"Directory changed: {directory_name}"
    except FileNotFoundError:
        return f"Directory not exists: {directory_name}"
    except Exception as e:
        return f"Error: {e}"

@traceable
def get_current_directory():
    try:
        current_dir = os.getcwd()
        return f"Current directory: {current_dir}"
    except Exception as e:
        return f"Error retrieving current directory: {str(e)}"
    

