# Mini Cursor Project

This project uses the UV package manager. Follow the instructions below to set up UV and install the required packages.

## Setup UV

1.  Install UV:

    ```bash
    pip install uv
    ```

2.  Use UV to create a virtual environment:

    ```bash
    uv venv
    ```

3.  Activate the virtual environment:

    ```bash
    source .venv/bin/activate
    ```

## Install Packages

Install the required packages using the following command:

```bash
uv add -r requirements.txt
```

## Langchain and Tracing

This project uses Langchain. If you do not want to use Langchain or any tracing app, you can remove the `traceable` function and write your own system prompts locally. Alternatively, you can save your prompts in Langsmith.
## Run the Application

To run the application, use the following command:

```bash
uv run main.py
```## OpenAI or Gemini Key

This application supports both OpenAI and Gemini. You can use either an OpenAI API key or a Gemini API key. Select the models accordingly based on the key you are using.

```
Create a `.env` file in the root directory of the project. Add the necessary environment variables to this file. You can refer to the `.env.example` file for the required variables and their format.

Example:

OKEY=YOUR_OPENAI_API_KEY
GKEY=YOUR_GEMINI_API_KEY


**Note:** The `SauravPortfolio` and `ticTac` projects were generated using this project itself.