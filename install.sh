#!/bin/sh

read -p "How would you like to install scraper Docker/Local [d/l]: " INSTALL_METHOD
mv .example.env .env
read -p "Enter the new PROJECT_NAME: " NEW_PROJECT_NAME
sed -i.bak "s/^PROJECT_NAME=.*/PROJECT_NAME=${NEW_PROJECT_NAME}/" .env


if [ "$INSTALL_METHOD" = "d" ]; then
  echo "Installing via Docker..."
  sed -i.bak "s/^DB_HOST=.*/DB_HOST=db/" .env
  sudo docker-compose up --build
elif [ "$INSTALL_METHOD" = "l" ]; then
  echo "Installing locally..."
  python -m venv .venv
  . .venv/bin/activate
  pip install -r requirements.txt
  echo "Scraper ready to use, edit .env file for your db creds"
  read -p "Are you change your .env?[y/n]: " ENV_CHANGED
  if [ "$ENV_CHANGED" = "y" ]; then
    alembic init
    alembic upgrade head
  elif [ "$ENV_CHANGED" = "n" ]; then
    echo "Ok, change later and start script manually"
  else
    echo "Invalid option selected."
  fi
  read -p "You want to run script now?[y/n]: " START_SCRIPT
  if [ "$START_SCRIPT" = "y" ]; then
    python main.py
  elif [ "$START_SCRIPT" = "n" ]; then
    echo "Ok, see you later)"
  else
    echo "Invalid option selected."
  fi
else
  echo "Invalid option selected."
fi
