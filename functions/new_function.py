import os

def get_file_content(working_directory, file_path):
    try:
        # Combine working_directory and file_path into a full path
        full_path = os.path.join(working_directory, file_path)
        full_path = os.path.abspath(full_path)

        # Validate that the full_path stays within the working_directory boundaries
        if not full_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Check if the path exists and is a file
        if not os.path.exists(full_path) or not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read the file content
        with open(full_path, 'r') as file:
            content = file.read()

        # Truncate the content if it exceeds 10000 characters
        if len(content) > 10000:
            content = content[:10000] + f'\n[...File "{file_path}" truncated at 10000 characters]'

        return content

    except Exception as e:
        # Catch any errors and return them as a string prefixed with "Error:"
        return f'Error: {str(e)}'