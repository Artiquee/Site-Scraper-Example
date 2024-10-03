@echo off
setlocal

set /p INSTALL_METHOD="How would you like to install scraper Docker/Local [d/l]: "
move .example.env .env
set /p NEW_PROJECT_NAME="Enter the new PROJECT_NAME: "
powershell -Command "(gc .env) -replace '^PROJECT_NAME=.*', 'PROJECT_NAME=%NEW_PROJECT_NAME%' | Set-Content .env"

if "%INSTALL_METHOD%"=="d" (
    echo Installing via Docker...
    docker-compose up --build
) else if "%INSTALL_METHOD%"=="l" (
    echo Installing locally...
    python -m venv .venv
    call .venv\Scripts\activate
    pip install -r requirements.txt
    alembic init
) else (
    echo Invalid option selected.
)

endlocal
