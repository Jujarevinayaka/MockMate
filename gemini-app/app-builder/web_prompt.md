> You are an exceptional and distinguished software engineer, known for designing high-end, production-ready web applications that are performant, user-friendly, and highly maintainable.
>
> Please build a **full-featured modern web application** in Python that replicates the following functionality:
>
> ---
>
> ### 💡 Core Functionality:
>
> 1. A user opens the web page and is presented with a **clean, responsive UI** where they can:
>
>    * Enter a natural language prompt
>    * Click a “Submit” button
> 2. On submit:
>
>    * The frontend sends the prompt to the backend.
>    * The backend starts a **background process** that runs the `gemini` CLI command in a shell.
>    * The prompt is sent to Gemini CLI as input.
>    * The response from the CLI is captured and returned to the frontend.
>    * The response is then displayed clearly on the page.
>    * If you want, use gemini_runner.py to interact with the gemini console.
>
> ---
>
> ### ⚙️ Backend:
>
> * Use **FastAPI** (preferred) or **Flask** for the backend.
> * Launch the `gemini` CLI process using `subprocess.Popen`, with:
>
>   * Proper `stdin`, `stdout`, and `stderr` pipes
>   * `shell=True` for **Windows compatibility**
> * Handle all possible errors:
>
>   * `gemini` not found
>   * Timeout
>   * Crashes or malformed output
> * Return appropriate HTTP responses (e.g., 500 on error, with JSON debug info).
> * Include a `requirements.txt`.
> * Optional: Add logging using Python's `logging` module.
>
> ---
>
> ### 🖼️ Frontend:
>
> * Build a **clean, modern, responsive** UI using HTML/CSS, optionally enhanced with:
>
>   * **Tailwind CSS** or **Bootstrap**
>   * **Vanilla JS** or **Alpine.js** for interactivity
> * The page should:
>
>   * Accept user input
>   * Show a **loading spinner** while waiting for response
>   * Display the response in a formatted text box
>   * Show error messages clearly if the CLI fails
> * If the CLI supports streaming output, support **live updating** of the response (optional).
>
> ---
>
> ### 🧾 Deliverables:
>
> * A complete project structured as:
>
>   ```
>   app/
>     ├── main.py               # FastAPI/Flask backend
>     ├── templates/
>     │     └── index.html      # Frontend UI
>     ├── static/               # CSS/JS assets
>     └── requirements.txt
>   ```
> * Clear instructions at the top of `main.py` on how to run the app (e.g. `uvicorn main:app --reload`)
> * Code should be modular, with comments where helpful, and ready for production extensions
> * Assume `gemini` CLI is installed and available in `PATH`
>