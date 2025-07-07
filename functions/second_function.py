import os

def write_file(working_directory, file_path, content):
    try:
        # Combine working_directory and file_path into a full path
        full_path = os.path.join(working_directory, file_path)
        full_path = os.path.abspath(full_path)

        # Validate that the full_path stays within the working_directory boundaries
        if not full_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Create the file if it doesn't exist and overwrite its contents
        with open(full_path, 'w') as file:
            file.write(content)

        # Return success message with the number of characters written
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        # Catch any errors and return them as a string prefixed with "Error:"
        return f'Error: {str(e)}'