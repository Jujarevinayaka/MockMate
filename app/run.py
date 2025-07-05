import subprocess
import time
import sys
import os
from pywinauto import Desktop

gemini_process = None
gemini_window = None
OUTPUT_FILE = "gemini_output.txt"

def find_gemini_window(title_keyword="gemini"):
    windows = Desktop(backend="win32").windows()
    for win in windows:
        try:
            title = win.window_text()
            if title_keyword.lower() in title.lower() and win.class_name() == "ConsoleWindowClass":
                print(f"[+] Found Gemini window: '{title}' (Handle: {win.handle})")
                return win.handle, win
        except Exception:
            pass
    return None, None

def launch_gemini():
    global gemini_process, gemini_window

    print("[*] Launching Gemini CLI in new CMD window...")

    # Clean previous output file
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    # Create command with redirection
    gemini_process = subprocess.Popen(
        ['cmd.exe', '/k', 'launch_gemini.bat'],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

    time.sleep(2)  # Wait for CMD to show

    _, gemini_window = find_gemini_window()
    if gemini_window:
        gemini_window.set_focus()
        print("[+] Gemini CLI launched and ready.")
        return True
    else:
        print("[!] Could not find Gemini window.")
        return False

def send_prompt_to_gemini(prompt: str):
    if gemini_window is None:
        print("[!] No Gemini window found.")
        return
    gemini_window.set_focus()
    time.sleep(0.3)
    gemini_window.type_keys(prompt, with_spaces=True)
    gemini_window.type_keys("{ENTER}")
    print("[→] Prompt sent.")

def read_latest_output(prev_len=0):
    if not os.path.exists(OUTPUT_FILE):
        return "", prev_len

    with open(OUTPUT_FILE, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    if len(content) > prev_len:
        new_part = content[prev_len:]
        return new_part.strip(), len(content)
    return "", prev_len

def main():
    if not launch_gemini():
        sys.exit(1)

    print(">>> Type prompts below to send to Gemini CLI.")
    print(">>> Output will be captured from 'gemini_output.txt'.\n")

    prev_len = 0
    try:
        while True:
            prompt = input("You: ")
            send_prompt_to_gemini(prompt)
            print("[...] Waiting for Gemini response...\n")

            time.sleep(3)  # Let Gemini generate output

            new_output, prev_len = read_latest_output(prev_len)
            if new_output:
                print("[📤] Gemini Response:\n" + "-" * 50)
                print(new_output)
                print("-" * 50)
            else:
                print("[!] No new output yet.")

    except KeyboardInterrupt:
        print("\n[!] Exiting.")
        sys.exit(0)

if __name__ == "__main__":
    main()
