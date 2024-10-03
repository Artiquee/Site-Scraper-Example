@echo off
setlocal

set /p INSTALL_METHOD="How would you like to install scraper Docker/Local [d/l]: "
move .example.env .env
set /p NEW_PROJECT_NAME="Enter the new PROJECT_NAME: "
powershell -Command "(gc .env) -replace '^PROJECT_NAME=.*', 'PROJECT_NAME=%NEW_PROJECT_NAME%' | Set-Content .env"

if "%INSTALL_METHOD%"=="d" (
    echo Installing via Docker...
    powershell -Command "(gc .env) -replace '^DB_HOST=.*', 'DB_HOST=db' | Set-Content .env"
    docker-compose up --build
) else if "%INSTALL_METHOD%"=="l" (
    echo Installing locally...
    python -m venv .venv
    call .venv\Scripts\activate
    pip install -r requirements.txt
    alembic init
    alembic upgrade head
    set /p START_SCRIPT="You want to run script now?[y/n]: "
    if "%START_SCRIPT%"=="y" (
        python main.py
    ) else if "%START_SCRIPT%"=="n" (
        echo "Ok, see you later)"
    ) else (
         echo Invalid option selected.
    )
) else (
    echo Invalid option selected.
)

endlocal
