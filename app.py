
from flask import Flask, render_template, request, jsonify
import subprocess
import time
import os
from pywinauto import Desktop
import re

class GeminiCLIApp:
    def __init__(self):
        self.app = Flask(__name__, template_folder='web/templates', static_folder='web/static')
        self.gemini_process = None
        self.gemini_window = None
        self.OUTPUT_FILE = "G:\Projects\GeminiCLI\MockMate\\app\gemini_output.txt"
        self.prev_len = 0
        self._register_routes()

    def _register_routes(self):
        self.app.route('/')(self.index)
        self.app.route('/send_prompt', methods=['POST'])(self.send_prompt)

    def find_gemini_window(self, title_keyword="gemini"):
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

    def launch_gemini(self):
        print("[*] Searching for existing Gemini window...")
        self.gemini_window = self.find_gemini_window()

        if self.gemini_window:
            print("[+] Found existing Gemini window. Skipping launch.")
            self.gemini_window.set_focus()
            return True

        print("[*] Launching Gemini CLI in new CMD window...")

        if os.path.exists(self.OUTPUT_FILE):
            os.remove(self.OUTPUT_FILE)

        self.gemini_process = subprocess.Popen(
            ['cmd.exe', '/k', 'launch_gemini.bat'],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )

        start_time = time.time()
        timeout = 15
        while time.time() - start_time < timeout:
            self.gemini_window = self.find_gemini_window()
            if self.gemini_window:
                self.gemini_window.set_focus()
                print("[+] Gemini CLI launched and ready.")
                return True
            time.sleep(0.5)
        
        print("[!] Could not find Gemini window after waiting.")
        return False

    def send_prompt_to_gemini(self, prompt: str):
        if self.gemini_window is None:
            print("[!] No Gemini window found. Attempting to relaunch...")
            if not self.launch_gemini():
                return "[!] Failed to launch or find Gemini window."
        
        try:
            self.gemini_window.set_focus()
            time.sleep(0.5)
            self.gemini_window.type_keys(prompt, with_spaces=True)
            self.gemini_window.type_keys("{ENTER}")
            print(f"[→] Prompt sent: {prompt}")
            return "Prompt sent successfully."
        except Exception as e:
            print(f"[!] Error sending prompt: {e}")
            self.gemini_window = None
            return "[!] Lost connection to Gemini window. Please try sending the prompt again."

    def read_latest_output(self):
        try:
            with open(self.OUTPUT_FILE, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            if len(content) > self.prev_len:
                new_part = content[self.prev_len:]
                self.prev_len = len(content)
                return new_part
        except Exception as e:
            print(f"[!] Error reading output file: {e}")
        
        return ""

    def index(self):
        return render_template('index.html')

    def send_prompt(self):
        prompt = request.json.get('prompt')
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400

        instruction = f"INSTRUCTION: you must write your response for the 'USER INPUT' into the file {self.OUTPUT_FILE}. "\
                      "If the user inputs a file path, read the file, follow the instructions, then write the response "\
                      f"into the file {self.OUTPUT_FILE}. Do not write the contents of the intput file into the {self.OUTPUT_FILE}, "\
                      "you must write only your response ; USER INPUT: "
        if os.path.exists(self.OUTPUT_FILE):
            os.remove(self.OUTPUT_FILE)
        self.send_prompt_to_gemini(instruction + prompt)
        
        file_created = False
        start_time = time.time()
        timeout = 30  # Increased timeout
        idle_threshold = 10 # Increased idle threshold

        last_output_time = time.time()

        while time.time() - start_time < timeout:
            if not os.path.exists(self.OUTPUT_FILE):
                continue

            file_created = True
            new_output = self.read_latest_output()
            if new_output:
                last_output_time = time.time()
            
            if time.time() - last_output_time > idle_threshold:
                print("[+] Idle threshold reached. Assuming response is complete.")
                break
            
            time.sleep(0.2)

        if not file_created:
            return jsonify({'error': 'Gemini output file was not created.'}), 500

        time.sleep(1) # Add a small delay before final read
        with open(self.OUTPUT_FILE, "r", encoding="utf-8", errors="ignore") as f: final_response = f.read()
        print(f"[Backend] Final response read from file: {final_response[:200]}...") # Log first 200 chars
        response_data = {'response': final_response or "No new output received."}
        print(f"[Backend] Sending JSON response: {response_data}")
        return jsonify(response_data)

    def run(self):
        if not self.launch_gemini():
            print("[!] Exiting: Could not start Gemini CLI.")
        else:
            self.app.run(debug=True, port=5000)

if __name__ == '__main__':
    app_instance = GeminiCLIApp()
    app_instance.run()
