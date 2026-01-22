#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install requirements from the main folder
pip install -r requirements.txt

# Move into the folder where manage.py lives
cd todo_list

# NOW run the commands
python manage.py collectstatic --no-input
python manage.py migrate