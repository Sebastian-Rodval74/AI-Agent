import os 

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