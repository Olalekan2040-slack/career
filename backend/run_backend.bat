@echo off
cd /d "%~dp0"
title Career Assessment - Backend

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat

echo Installing/checking dependencies...
pip install -q -r requirements.txt

echo.
echo Starting FastAPI backend on http://localhost:8000 ...
uvicorn app.main:app --reload --port 8000
