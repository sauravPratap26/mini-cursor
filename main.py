from openai import OpenAI
from dotenv import load_dotenv

import os

import json

from langsmith.wrappers import wrap_openai

from langsmith import Client

from tools import (
    make_directory,
    delete_directory,
    change_directory,
    create_file,
    read_file,
    append_to_file,
    delete_file,
    list_files,
    move_file,
    path_exists,
    rename_path,
    create_vite_app,
    run_command,
    get_current_directory
)


available_tools = {
    "make_directory": make_directory,
    "delete_directory":delete_directory,
    "change_directory":change_directory,
    "create_file":create_file,
    "read_file":read_file,
    "append_to_file":append_to_file,
    "delete_file":delete_file,
    "list_files":list_files,
    "move_file":move_file,
    "path_exists":path_exists,
    "rename_path":rename_path,
    "create_vite_app": create_vite_app,
    "run_command": run_command,
    "get_current_directory":get_current_directory
}

SYSTEM_MESSAGE=""""
you can put your prompt over here
"""

def main():
    load_dotenv()
    clientPrompt = Client(api_key=os.environ.get("LANGSMITH_API_KEY"))
    prompt = clientPrompt.pull_prompt("minicursor", include_model=False)
    client = wrap_openai(OpenAI(
    api_key=os.environ.get("GKEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    ))

    messages = [
    {"role": "system", "content": f"""{prompt.messages[0].prompt.template}"""},
]


    while True:
        query = input("You: ")
        if not query.strip():
            break

        messages.append({"role": "user", "content": query})

        while True:
            res = client.chat.completions.create(
                model="gemini-2.0-flash",
                messages=messages,
                response_format={"type": "json_object"},
            )

            parsed_output = json.loads(res.choices[0].message.content)
            messages.append({"role": "assistant", "content": json.dumps(parsed_output)})
            step = parsed_output.get("step")

            if step == "output":
                print(f"\n{parsed_output.get("content")}\n")
                break
            elif step == "plan" or step == "verify" or step =="observe":
                print(f"{parsed_output["content"]}\n")
                continue
            elif step == "action":
                inp1 = parsed_output.get("first_input", "null")
                inp2 = parsed_output.get("second_input", "null")
                func = parsed_output.get("function")
                print(f"\n{inp1}\n{inp2}\n{func}\n")
                output =""
                if func in available_tools:
                    if (inp1 == None or inp1 == "null") and (inp2 == None or inp2 == "null"):
                        output = available_tools[func]()
                    elif (inp2 == None or inp2 =="null"):
                        output = available_tools[func](inp1)
                    elif (inp1 == None or inp1 == "null"):
                        output = available_tools[func](inp2)
                    else:
                        output = available_tools[func](inp1, inp2)

                messages.append({
                    "role": "assistant",
                    "content": json.dumps({"step": "observe", "content": output}),
                })
                continue
            else:
                messages.append(
                    {
                        "role": "assistant",
                        "content": json.dumps(
                            {
                                "step": "observe",
                                "content": f"Tool not exists: {func}",
                            }
                        ),
                    }
                )
                continue


if __name__ == "__main__":
    main()
