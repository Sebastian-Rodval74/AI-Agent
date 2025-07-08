import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    try:
        full_path = os.path.join(working_directory, directory) 
        full_path = os.path.abspath(full_path)

        if not full_path.startswith(os.path.abspath(working_directory)):
            return f'Error:"{directory}" is not a directory'
        if not os.path.exists(full_path) or not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'
        contents = []
        for item in os.listdir(full_path):
            item_path = os.path.join(full_path, item)
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            contents.append(f'- {item}: file_size={file_size} bytes, is_dir={is_dir}')

        return '\n'.join(contents)
    except Exception as e:
        return f'Error: {str(e)}'

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns a summary or snippet of each file's contents in the specified directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the directory to read files from.",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes the specified Python file in the given directory with optional arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python (.py) file to execute.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional argumentes to run the files.",
                items = types.Schema(
                    type=types.Type.STRING,
                    
                ),
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the provided content to the specified file path, overwriting any existing contents.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The full path of the file to write to.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The exact text content to write into the file.",
            ),
        },
    ),
)


