$INSTALL_METHOD = Read-Host "How would you like to install scraper Docker/Local [d/l]"
Copy-Item example.env .env
$NEW_PROJECT_NAME = Read-Host "Enter the new PROJECT_NAME"
(Get-Content .env) -replace '^(PROJECT_NAME=).*', "`$1$NEW_PROJECT_NAME" | Set-Content .env

if ($INSTALL_METHOD -eq "d") {
    Write-Host "Installing via Docker..."
    docker-compose up --build
} elseif ($INSTALL_METHOD -eq "l") {
    Write-Host "Installing locally..."
    pip install -r requirements.txt
    alembic init
} else {
    Write-Host "Invalid option selected."
}
