import os 
import subprocess
def run_python_file(working_directory, file_path):
    result_output = []
    try:
        full_path = os.path.join(working_directory, file_path)
        full_path = os.path.abspath(full_path)

        if not full_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(full_path):
            return f'Error: File "{file_path}" not found'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        result = subprocess.run(
            ['python', full_path],
            capture_output=True,
            text=True,
            timeout = 30,
            cwd=working_directory
        )

        output_produced = False

        if result.stdout.strip():
            result_output.append(f"STDOUT: \n{result.stdout}" )
            output_produced = True
        if result.stderr.strip():
            result_output.append(f"STDERR: \n{result.stderr}" )
            output_produced = True
        if result.returncode != 0:
            result_output.append (f'Process exited with code {result.returncode}')
        if not output_produced:
            result_output.append("No output produced")

        final_output = "\n".join(result_output)
        return final_output
    except subprocess.TimeoutExpired:
        return f'The script took to long and was terminated.'
    except Exception as e:
        return f'Error: executing Python file: {e}'
    