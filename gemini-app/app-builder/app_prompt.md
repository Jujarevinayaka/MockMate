> You are an exceptional and distinguished software engineer, known for writing clean, simple, and highly optimized code.
>
> Please write a **Python script** that does the following:
>
> 1. Prompts the user to input a message via `input()`.
> 2. Launches a **background process** that runs the `gemini` CLI (assume it's installed and accessible via PATH).
> 3. Sends the user's input to the Gemini CLI as if it were entered interactively (simulate an interactive prompt).
> 4. Captures the full output from the Gemini CLI.
> 5. Returns and prints the output clearly back to the user.
>
> ### Requirements:
>
> * Must be **cross-platform**: fully compatible with **Windows**, **Linux**, and **macOS**.
> * Use only **standard Python libraries** (e.g., `subprocess`, `sys`, `os`, etc.).
> * Use `subprocess.Popen` with `stdin`, `stdout`, and `stderr` redirection to communicate with the Gemini CLI.
> * Handle all possible **error scenarios**, such as:
>
>   * Gemini CLI not found
>   * CLI crashes or exits unexpectedly
>   * Timeouts
>   * Invalid input
> * Provide **clear error messages and debug output** to help trace any issue.
> * The script should be simple, well-structured, and **easy to understand and debug**.
> * Comment the code only where necessary — focus on clarity and elegance.
>
> Output only the **final Python script in a single file**, ready to run.

---

Let me know if you'd like to test or validate the Gemini CLI behavior within Python after you receive the code.
