import os
from google import genai
from google.genai import types

from functions.write_file import write_file
from functions.get_files_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python import run_python_file


def call_function(function_call_part, verbose=False):
    
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function_map = {
        "run_python_file": run_python_file,
        "get_files_info": get_files_info,
        "write_file": write_file,
        "get_file_content": get_file_content
    }

    function_call_part.args["working_directory"] = "./calculator"

    if function_call_part.name in function_map:
        function_result = function_map[function_call_part.name](**function_call_part.args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": function_result},
                )
            ],
        )
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )   