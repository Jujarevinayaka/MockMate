
# How to run:
# 1. Install dependencies: pip install -r requirements.txt
# 2. Run the app: uvicorn main:app --reload --port 8001

from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.services.gemini_service import call_gemini_cli
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent # This should point to the MockMate root
PROMPT_BANK_DIR = BASE_DIR / "app" / "support" / "prompt-bank"
JDS_DIR = BASE_DIR / "app" / "support" / "jds"
RESUME_DIR = BASE_DIR / "app" / "support" / "resume"

templates = Jinja2Templates(directory=BASE_DIR / "app" / "templates")
app.mount("/static", StaticFiles(directory=BASE_DIR / "app" / "static"), name="static")

def _read_file_content(file_path: Path) -> str:
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    return file_path.read_text(encoding="utf-8")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/run-gemini", response_class=JSONResponse)
async def run_gemini(prompt: str = Form(...)):
    try:
        logger.info(f"Received prompt: {prompt}")
        
        stdout, stderr = call_gemini_cli(prompt)

        if stderr:
            logger.error(f"Gemini CLI failed with error: {stderr}")
            return JSONResponse(status_code=500, content={"error": stderr})

        logger.info(f"Gemini CLI output: {stdout}")
        return JSONResponse(content={"response": stdout})

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/interview/job-fit-analyzer", response_class=JSONResponse)
async def run_job_fit_analyzer(
    jd_filename: str = Form("Google.md"),
    resume_filename: str = Form("Resume.md")
):
    try:
        prompt_content = _read_file_content(PROMPT_BANK_DIR / "01_JFA.txt")
        jd_content = _read_file_content(JDS_DIR / jd_filename)
        resume_content = _read_file_content(RESUME_DIR / resume_filename)

        full_prompt = (
            f"{prompt_content}\n\n"
            f"Job Description:\n{jd_content}\n\n"
            f"Resume:\n{resume_content}"
        )
        logger.info(f"Sending prompt to Gemini CLI for JFA.")
        stdout, stderr = call_gemini_cli(full_prompt)

        if stderr:
            logger.error(f"Gemini CLI failed for JFA with error: {stderr}")
            raise HTTPException(status_code=500, detail=stderr)

        logger.info(f"Gemini CLI output for JFA: {stdout}")
        return JSONResponse(content={"response": stdout})

    except FileNotFoundError as e:
        logger.error(f"File not found error: {e}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"An unexpected error occurred during JFA: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/interview/hiring-manager", response_class=JSONResponse)
async def run_hiring_manager(
    jd_filename: str = Form("Google.md"),
    resume_filename: str = Form("Resume.md")
):
    try:
        prompt_content = _read_file_content(PROMPT_BANK_DIR / "02_HM.txt")
        jd_content = _read_file_content(JDS_DIR / jd_filename)
        resume_content = _read_file_content(RESUME_DIR / resume_filename)

        full_prompt = (
            f"{prompt_content}\n\n"
            f"Job Description:\n{jd_content}\n\n"
            f"Resume:\n{resume_content}"
        )
        logger.info(f"Sending prompt to Gemini CLI for HM.")
        stdout, stderr = call_gemini_cli(full_prompt)

        if stderr:
            logger.error(f"Gemini CLI failed for HM with error: {stderr}")
            raise HTTPException(status_code=500, detail=stderr)

        logger.info(f"Gemini CLI output for HM: {stdout}")
        return JSONResponse(content={"response": stdout})

    except FileNotFoundError as e:
        logger.error(f"File not found error: {e}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"An unexpected error occurred during HM: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/interview/product-manager", response_class=JSONResponse)
async def run_product_manager(
    jd_filename: str = Form("Google.md"),
    resume_filename: str = Form("Resume.md")
):
    try:
        prompt_content = _read_file_content(PROMPT_BANK_DIR / "03_PM.txt")
        jd_content = _read_file_content(JDS_DIR / jd_filename)
        resume_content = _read_file_content(RESUME_DIR / resume_filename)

        full_prompt = (
            f"{prompt_content}\n\n"
            f"Job Description:\n{jd_content}\n\n"
            f"Resume:\n{resume_content}"
        )
        logger.info(f"Sending prompt to Gemini CLI for PM.")
        stdout, stderr = call_gemini_cli(full_prompt)

        if stderr:
            logger.error(f"Gemini CLI failed for PM with error: {stderr}")
            raise HTTPException(status_code=500, detail=stderr)

        logger.info(f"Gemini CLI output for PM: {stdout}")
        return JSONResponse(content={"response": stdout})

    except FileNotFoundError as e:
        logger.error(f"File not found error: {e}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"An unexpected error occurred during PM: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/interview/technical-lead", response_class=JSONResponse)
async def run_technical_lead(
    jd_filename: str = Form("Google.md"),
    resume_filename: str = Form("Resume.md")
):
    try:
        prompt_content = _read_file_content(PROMPT_BANK_DIR / "03_TL.txt")
        jd_content = _read_file_content(JDS_DIR / jd_filename)
        resume_content = _read_file_content(RESUME_DIR / resume_filename)

        full_prompt = (
            f"{prompt_content}\n\n"
            f"Job Description:\n{jd_content}\n\n"
            f"Resume:\n{resume_content}"
        )
        logger.info(f"Sending prompt to Gemini CLI for TL.")
        stdout, stderr = call_gemini_cli(full_prompt)

        if stderr:
            logger.error(f"Gemini CLI failed for TL with error: {stderr}")
            raise HTTPException(status_code=500, detail=stderr)

        logger.info(f"Gemini CLI output for TL: {stdout}")
        return JSONResponse(content={"response": stdout})

    except FileNotFoundError as e:
        logger.error(f"File not found error: {e}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"An unexpected error occurred during TL: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/interview/technical-product-manager", response_class=JSONResponse)
async def run_technical_product_manager(
    jd_filename: str = Form("Google.md"),
    resume_filename: str = Form("Resume.md")
):
    try:
        prompt_content = _read_file_content(PROMPT_BANK_DIR / "04_TPM.txt")
        jd_content = _read_file_content(JDS_DIR / jd_filename)
        resume_content = _read_file_content(RESUME_DIR / resume_filename)

        full_prompt = (
            f"{prompt_content}\n\n"
            f"Job Description:\n{jd_content}\n\n"
            f"Resume:\n{resume_content}"
        )
        logger.info(f"Sending prompt to Gemini CLI for TPM.")
        stdout, stderr = call_gemini_cli(full_prompt)

        if stderr:
            logger.error(f"Gemini CLI failed for TPM with error: {stderr}")
            raise HTTPException(status_code=500, detail=stderr)

        logger.info(f"Gemini CLI output for TPM: {stdout}")
        return JSONResponse(content={"response": stdout})

    except FileNotFoundError as e:
        logger.error(f"File not found error: {e}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"An unexpected error occurred during TPM: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/interview/managerial", response_class=JSONResponse)
async def run_managerial(
    jd_filename: str = Form("Google.md"),
    resume_filename: str = Form("Resume.md")
):
    try:
        prompt_content = _read_file_content(PROMPT_BANK_DIR / "05_Man.txt")
        jd_content = _read_file_content(JDS_DIR / jd_filename)
        resume_content = _read_file_content(RESUME_DIR / resume_filename)

        full_prompt = (
            f"{prompt_content}\n\n"
            f"Job Description:\n{jd_content}\n\n"
            f"Resume:\n{resume_content}"
        )
        logger.info(f"Sending prompt to Gemini CLI for Managerial.")
        stdout, stderr = call_gemini_cli(full_prompt)

        if stderr:
            logger.error(f"Gemini CLI failed for Managerial with error: {stderr}")
            raise HTTPException(status_code=500, detail=stderr)

        logger.info(f"Gemini CLI output for Managerial: {stdout}")
        return JSONResponse(content={"response": stdout})

    except FileNotFoundError as e:
        logger.error(f"File not found error: {e}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"An unexpected error occurred during Managerial: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/interview/hr", response_class=JSONResponse)
async def run_hr(
    jd_filename: str = Form("Google.md"),
    resume_filename: str = Form("Resume.md")
):
    try:
        prompt_content = _read_file_content(PROMPT_BANK_DIR / "06_HR.txt")
        jd_content = _read_file_content(JDS_DIR / jd_filename)
        resume_content = _read_file_content(RESUME_DIR / resume_filename)

        full_prompt = (
            f"{prompt_content}\n\n"
            f"Job Description:\n{jd_content}\n\n"
            f"Resume:\n{resume_content}"
        )
        logger.info(f"Sending prompt to Gemini CLI for HR.")
        stdout, stderr = call_gemini_cli(full_prompt)

        if stderr:
            logger.error(f"Gemini CLI failed for HR with error: {stderr}")
            raise HTTPException(status_code=500, detail=stderr)

        logger.info(f"Gemini CLI output for HR: {stdout}")
        return JSONResponse(content={"response": stdout})

    except FileNotFoundError as e:
        logger.error(f"File not found error: {e}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"An unexpected error occurred during HR: {e}")
        raise HTTPException(status_code=500, detail=str(e))
