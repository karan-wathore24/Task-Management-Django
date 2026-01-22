#!/bin/bash

# Install dependencies using Poetry
poetry install

# Navigate to the Django project directory
cd todo_list

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput
