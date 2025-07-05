import subprocess
import sys
import os

def call_gemini_cli(user_input: str, timeout: int = 60) -> tuple[str, str]:
    """
    Launches the Gemini CLI as a background process, sends the user's input,
    and captures the full output.

    Args:
        user_input: The message to send to the Gemini CLI.
        timeout: The maximum time in seconds to wait for the process to complete.

    Returns:
        A tuple containing the standard output and standard error from the CLI.
    """
    command = "gemini --model gemini-2.5-flash"
    
    creationflags = 0
    if sys.platform == "win32":
        creationflags = subprocess.CREATE_NO_WINDOW

    try:
        process = subprocess.Popen(
            command,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',
            creationflags=creationflags,
            start_new_session=(sys.platform != "win32")
        )

        stdout, stderr = process.communicate(input=user_input + "\n", timeout=timeout)

        return stdout, stderr

    except FileNotFoundError:
        error_message = (
            "Error: The 'gemini' command was not found.\n"
            "Please ensure the Gemini CLI is installed and that its location is included in your system's PATH environment variable."
        )
        return "", error_message
    
    except subprocess.TimeoutExpired:
        process.kill()
        stdout, stderr = process.communicate()
        timeout_error = f"Error: The command timed out after {timeout} seconds.\n"
        if stderr:
            timeout_error += f"Captured stderr before timeout:\n{stderr}"
        return stdout, timeout_error

    except Exception as e:
        return "", f"An unexpected error occurred: {e}"

