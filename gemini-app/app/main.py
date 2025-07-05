
# How to run:
# 1. Install dependencies: pip install -r requirements.txt
# 2. Run the app: uvicorn main:app --reload --port 8001

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/run-gemini", response_class=JSONResponse)
async def run_gemini(prompt: str = Form(...)):
    try:
        logger.info(f"Received prompt: {prompt}")
        
        # Command to run the gemini runner
        command = ["python", "../gemini_runner.py", prompt]

        # Start the subprocess
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True  # Use shell=True for Windows compatibility
        )

        # Communicate with the subprocess (no input needed now)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            logger.error(f"Gemini CLI failed with error: {stderr}")
            return JSONResponse(status_code=500, content={"error": stderr})

        logger.info(f"Gemini CLI output: {stdout}")
        return JSONResponse(content={"response": stdout})

    except FileNotFoundError:
        logger.error("gemini_runner.py not found.")
        return JSONResponse(status_code=500, content={"error": "Gemini runner script not found."})
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})
