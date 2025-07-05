

import subprocess
import sys
import threading
import os

def run_gemini_in_background(user_input: str, timeout: int = 60) -> tuple[str, str]:
    """
    Launches the Gemini CLI as a background process, sends the user's input,
    and captures the full output.

    Args:
        user_input: The message to send to the Gemini CLI.
        timeout: The maximum time in seconds to wait for the process to complete.

    Returns:
        A tuple containing the standard output and standard error from the CLI.
    """
    # Ensure the command is cross-platform compatible
    command = ["gemini"]
    
    # For Windows, we might need to specify the shell if 'gemini' is a .bat or .cmd file
    # However, for a direct executable in PATH, this is generally not needed.
    # The creationflags are used to prevent the console window from appearing on Windows.
    creationflags = 0
    if sys.platform == "win32":
        creationflags = subprocess.CREATE_NO_WINDOW

    try:
        # Using subprocess.Popen to have fine-grained control over the process
        process = subprocess.Popen(
            command,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,  # Work with text streams (str) instead of bytes
            encoding='utf-8',
            creationflags=creationflags,
            # start_new_session=True is useful on Unix-like systems to prevent signals
            # from the parent from affecting the child.
            start_new_session=(sys.platform != "win32")
        )

        # Communicate with the process: send input and read output.
        # .communicate() is a safe way to handle this without deadlocks.
        # We add a newline to simulate pressing Enter after typing the command.
        stdout, stderr = process.communicate(input=user_input + "\n", timeout=timeout)

        return stdout, stderr

    except FileNotFoundError:
        error_message = (
            "Error: The 'gemini' command was not found.\n"
            "Please ensure the Gemini CLI is installed and that its location is included in your system's PATH environment variable."
        )
        return "", error_message
    
    except subprocess.TimeoutExpired:
        # If the process times out, we should terminate it to clean up.
        process.kill()
        # Even after killing, we should communicate() to get any buffered output.
        stdout, stderr = process.communicate()
        timeout_error = f"Error: The command timed out after {timeout} seconds.\n"
        if stderr:
            timeout_error += f"Captured stderr before timeout:\n{stderr}"
        return stdout, timeout_error

    except Exception as e:
        # Catch any other unexpected exceptions
        return "", f"An unexpected error occurred: {e}"

def main():
    """
    Main function to drive the script. Prompts the user for input,
    runs the Gemini CLI, and prints the results.
    """
    print("Gemini CLI Interactive Python Runner")
    print("------------------------------------")
    
    try:
        # Prompt the user for their message
        user_message = input("Please enter your message to send to Gemini:\n> ")

        if not user_message.strip():
            print("\nError: Input cannot be empty.")
            return

        print("\n... Sending to Gemini CLI ...\n")

        # Run the background process
        stdout, stderr = run_gemini_in_background(user_message)

        # Print the captured output
        print("--- Gemini CLI Output ---")
        if stdout:
            print(stdout.strip())
        
        if stderr:
            print("\n--- Errors / Debug Info ---")
            print(stderr.strip())
        
        print("\n--------------------------")

    except (KeyboardInterrupt, EOFError):
        print("\n\nOperation cancelled by user. Exiting.")
    except Exception as e:
        print(f"\nA critical error occurred in the main loop: {e}")

if __name__ == "__main__":
    main()

