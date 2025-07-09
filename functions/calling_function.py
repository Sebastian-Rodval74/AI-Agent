from functions.get_files_info import get_files_info
from functions.new_function import get_file_content
from functions.run_python import run_python_file
from functions.second_function import write_file
from google.genai import types

def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    if verbose == True:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    args = function_call_part.args or {}
    copied_args = args.copy()
    copied_args['working_directory'] = "./calculator"


    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    function_to_call = function_map[function_name]
    function_result = function_to_call(**copied_args)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )

