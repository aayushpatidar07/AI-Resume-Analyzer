@echo off
REM ============================================================
REM AI Resume Analyzer & Job Matcher - Windows Startup Script
REM ============================================================

echo.
echo ============================================================
echo AI Resume Analyzer and Job Matcher
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from python.org
    echo.
    pause
    exit /b 1
)

echo [*] Python found: 
python --version
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo [*] Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo [OK] Virtual environment created
    echo.
)

REM Activate virtual environment
echo [*] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo [OK] Virtual environment activated
echo.

REM Check if dependencies are installed
echo [*] Checking dependencies...
pip list | findstr /i flask >nul 2>&1
if errorlevel 1 (
    echo [*] Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
    echo [OK] Dependencies installed
    echo.
) else (
    echo [OK] Dependencies already installed
    echo.
)

REM Check if uploads directory exists
if not exist "uploads" (
    echo [*] Creating uploads directory...
    mkdir uploads
    echo [OK] Uploads directory created
    echo.
)

REM Display startup information
echo ============================================================
echo STARTUP INFORMATION
echo ============================================================
echo.
echo [*] Application: AI Resume Analyzer & Job Matcher
echo [*] Server: http://127.0.0.1:5000
echo [*] Environment: Development
echo [*] Debug Mode: Enabled
echo.
echo [*] Press Ctrl+C to stop the server
echo.
echo ============================================================
echo.

REM Start the application
echo [*] Starting Flask server...
echo.
python app.py

REM If we get here, the application stopped
echo.
echo [!] Application stopped
pause
