@echo off
setlocal
set "ROOT=%~dp0"
title Career Assessment Launcher

echo Starting backend (FastAPI)...
start "Career Assessment - Backend" "%ROOT%backend\run_backend.bat"

echo Starting frontend (Vite)...
start "Career Assessment - Frontend" "%ROOT%frontend\run_frontend.bat"

echo Waiting for the frontend to come up...
timeout /t 8 /nobreak > nul

start "" http://localhost:5173

echo.
echo Both servers are starting in their own windows.
echo Close those windows (or press Ctrl+C in each) to stop the app.
echo This launcher window can be closed now.
pause
