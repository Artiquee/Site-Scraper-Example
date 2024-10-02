#!/bin/sh

read -p "How would you like to install scraper Docker/Local [d/l]: " INSTALL_METHOD
mv example.env .env
read -p "Enter the new PROJECT_NAME: " NEW_PROJECT_NAME
sed -i.bak "s/^PROJECT_NAME=.*/PROJECT_NAME=${NEW_PROJECT_NAME}/" .env


if [ "$INSTALL_METHOD" = "d" ]; then
  echo "Installing via Docker..."
  sudo docker-compose up --build
elif [ "$INSTALL_METHOD" = "l" ]; then
  echo "Installing locally..."
  pip install -r requirements.txt
  alembic init
else
  echo "Invalid option selected."
fi
