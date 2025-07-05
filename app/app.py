
from flask import Flask, render_template, request, jsonify
import subprocess
import time
import os
from pywinauto import Desktop
import re

app = Flask(__name__, template_folder='web/templates', static_folder='web/static')

gemini_process = None
gemini_window = None
OUTPUT_FILE = "gemini_output.txt"
# A variable to hold the previous length of the output file
prev_len = 0

def find_gemini_window(title_keyword="gemini"):
    windows = Desktop(backend="win32").windows()
    for win in windows:
        try:
            title = win.window_text()
            if title_keyword.lower() in title.lower() and win.class_name() == "ConsoleWindowClass":
                print(f"[+] Found Gemini window: '{title}' (Handle: {win.handle})")
                return win
        except Exception:
            pass
    return None

def launch_gemini():
    global gemini_process, gemini_window

    print("[*] Searching for existing Gemini window...")
    gemini_window = find_gemini_window()

    if gemini_window:
        print("[+] Found existing Gemini window. Skipping launch.")
        gemini_window.set_focus()
        return True

    print("[*] Launching Gemini CLI in new CMD window...")

    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    gemini_process = subprocess.Popen(
        ['cmd.exe', '/k', 'launch_gemini.bat'],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

    # --- Poll for Gemini Window ---
    start_time = time.time()
    timeout = 15  # Wait a maximum of 15 seconds for the window
    while time.time() - start_time < timeout:
        #global gemini_window
        gemini_window = find_gemini_window()
        if gemini_window:
            gemini_window.set_focus()
            print("[+] Gemini CLI launched and ready.")
            return True
        time.sleep(0.5) # Check every half second
    
    print("[!] Could not find Gemini window after waiting.")
    return False

def send_prompt_to_gemini(prompt: str):
    global gemini_window
    if gemini_window is None:
        print("[!] No Gemini window found. Attempting to relaunch...")
        if not launch_gemini():
            return "[!] Failed to launch or find Gemini window."
    
    try:
        gemini_window.set_focus()
        time.sleep(0.5)
        gemini_window.type_keys(prompt, with_spaces=True)
        gemini_window.type_keys("{ENTER}")
        print(f"[→] Prompt sent: {prompt}")
        return "Prompt sent successfully."
    except Exception as e:
        print(f"[!] Error sending prompt: {e}")
        # Attempt to recover
        gemini_window = None # Reset window object
        return "[!] Lost connection to Gemini window. Please try sending the prompt again."


def read_latest_output():
    global prev_len
    if not os.path.exists(OUTPUT_FILE):
        return ""

    try:
        with open(OUTPUT_FILE, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        if len(content) > prev_len:
            new_part = content[prev_len:]
            prev_len = len(content)
            return new_part
    except Exception as e:
        print(f"[!] Error reading output file: {e}")
    
    return ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_prompt', methods=['POST'])
def send_prompt():
    prompt = request.json.get('prompt')
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    send_prompt_to_gemini(prompt)
    
    # --- Start Polling for Response ---
    full_response = []
    start_time = time.time()
    timeout = 30  # Maximum wait time in seconds
    idle_threshold = 10  # Time in seconds to wait for more output before stopping

    last_output_time = time.time()

    while time.time() - start_time < timeout:
        new_output = read_latest_output()
        if new_output:
            full_response.append(new_output)
            last_output_time = time.time()  # Reset timer on new output
        
        # If no new output for a certain period, assume response is complete
        if time.time() - last_output_time > idle_threshold:
            print("[+] Idle threshold reached. Assuming response is complete.")
            break
        
        time.sleep(0.2)  # Polling interval

    # --- End Polling ---

    final_response = "\n".join(full_response).strip()

    marker = '[G✦'
    idx = final_response.rfind(marker)
    res = final_response[idx + len(marker):].strip()
    res = res.split("\n")
    unique = list(dict.fromkeys(res))
    unique_ = []
    for i, item in enumerate(unique[:-1]):
        if ("(esc to cancel" not in item.strip()) and \
           (item not in unique[i+1]):
            #ansi_stripped = re.sub(r'\x1b\[[0-9;]*[A-Za-z]', '', item)
            #osc_stripped = re.sub(r'\x1b\].*?\x07', '', ansi_stripped)
            unique_.append(item.strip())
    final_response = "\n".join(unique_).strip()

    print(final_response)
    return jsonify({'response': final_response or "No new output received."})

if __name__ == '__main__':
    if not launch_gemini():
        print("[!] Exiting: Could not start Gemini CLI.")
    else:
        app.run(debug=True, port=5000)
