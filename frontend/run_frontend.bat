@echo off
cd /d "%~dp0"
title Career Assessment - Frontend

if not exist node_modules (
    echo Installing frontend dependencies, this may take a minute...
    call npm install
)

echo.
echo Starting Vite frontend on http://localhost:5173 ...
call npm run dev
