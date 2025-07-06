# MockMate - Gemini CLI Interview Simulator

MockMate is a web-based application that provides an interactive interface to simulate various job interview scenarios using the Gemini Command Line Interface (CLI). It allows users to practice for interviews by providing job descriptions and resumes, and then interacting with an AI acting as different interviewers (e.g., HR, Hiring Manager, Technical Lead, Product Manager).

## Features

*   **Interactive Web Interface**: A user-friendly web UI for sending prompts and receiving responses from the Gemini CLI.
*   **Interview Role Simulation**: Gemini can act as different interviewers (Job Fit Analyzer, Hiring Manager, Product Manager, Technical Lead, Technical Product Manager, Managerial Interviewer, HR Interviewer) based on predefined prompt files.
*   **Dynamic Prompting**: The application dynamically sends user inputs and specific instructions to the Gemini CLI, ensuring responses are tailored and captured.
*   **Real-time Output Display**: Responses from Gemini are streamed and displayed in the web interface as they are generated.
*   **Configurable Interview Scenarios**: Easily switch between different interview types by leveraging a "prompt bank" of detailed role definitions.

## How It Works

MockMate consists of a Flask backend, a web frontend, and integrates with the Gemini CLI:

1.  **Flask Backend (`app.py`)**:
    *   Manages the web server and API endpoints.
    *   Launches and connects to the Gemini CLI in a separate console window using `pywinauto`.
    *   Constructs specific instructions for Gemini to write its output to a designated file (`gemini_output.txt`).
    *   Reads Gemini's responses from `gemini_output.txt` and sends them to the web frontend.
2.  **Web Frontend (`web/templates/index.html`, `web/static/css/style.css`, `web/static/js/script.js`)**:
    *   Provides the user interface for inputting prompts and displaying chat messages.
    *   Uses JavaScript to send user prompts to the Flask backend and update the chat interface with Gemini's responses.
    *   Styled with Tailwind CSS for a modern look.
3.  **Gemini CLI Integration**:
    *   The `launch_gemini.bat` script is used to start the Gemini CLI with specific model and output redirection parameters.
    *   Gemini processes the instructions and user prompts, writing its responses to `gemini_output.txt`.
4.  **Prompt Bank (`support/prompt-bank/`)**:
    *   Contains individual `.txt` files, each defining a specific interviewer role with detailed instructions, constraints, and output formats.
    *   A `meta.txt` file orchestrates the sequence and flow of these interview simulations.

## Setup and Installation

To set up and run MockMate, follow these steps:

1.  **Prerequisites**:
    *   Python 3.x
    *   Flask
    *   pywinauto
    *   Gemini CLI (ensure it's installed and accessible from your command line)
    *   Node.js and npm (for Tailwind CSS, though it's already compiled in `style.css`)

2.  **Clone the Repository**:
    ```bash
    git clone <repository_url>
    cd MockMate/app
    ```

3.  **Install Python Dependencies**:
    ```bash
    pip install Flask pywinauto
    ```

4.  **Ensure Gemini CLI is Configured**:
    Make sure your Gemini CLI is correctly installed and authenticated. The `launch_gemini.bat` script expects the `gemini` command to be available in your system's PATH.

## Usage

1.  **Start the Application**:
    Navigate to the `app` directory in your terminal and run:
    ```bash
    python app.py
    ```
    This will launch the Flask server and attempt to start the Gemini CLI.

2.  **Access the Web Interface**:
    Open your web browser and go to `http://127.0.0.1:5000/`.

3.  **Start an Interview Simulation**:
    The application will guide you to provide a job description and your resume (e.g., by referencing the sample files in `support/jds/` and `support/resume/`). Gemini will then begin the interview simulation based on the `meta.txt` and individual prompt files.

4.  **Interact with Gemini**:
    Type your responses into the input field and press "Send". Gemini will provide feedback and ask follow-up questions according to the active interviewer role.

## File Structure

```
MockMate/app/
├── app.py                  # Flask backend application
├── gemini_output.txt       # Temporary file for Gemini CLI output
├── launch_gemini.bat       # Batch script to launch Gemini CLI
├── support/
│   ├── jds/
│   │   └── Google.md       # Sample Job Description
│   ├── prompt-bank/
│   │   ├── 01_JFA.txt      # Job Fit Analyzer prompt
│   │   ├── 02_HM.txt       # Hiring Manager prompt
│   │   ├── 03_PM.txt      # Product Manager prompt
│   │   ├── 03_TL.txt       # Technical Lead prompt
│   │   ├── 04_TPM.txt      # Technical Product Manager prompt
│   │   ├── 05_Man.txt      # Managerial Interviewer prompt
│   │   ├── 06_HR.txt       # HR Interviewer prompt
│   │   └── meta.txt        # Meta-prompt for orchestrating interviews
│   └── resume/
│       └── Resume.md       # Sample Resume
└── web/
    ├── static/
    │   ├── css/
    │   │   └── style.css   # Custom CSS for the web UI
    │   └── js/
    │       └── script.js   # Frontend JavaScript for interactivity
    └── templates/
        └── index.html      # Main HTML template for the web UI
```