#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies from the root directory
pip install -r requirements.txt

# Move into the project directory where manage.py is located
cd todo_list

# Run your Django commands
python manage.py collectstatic --no-input
python manage.py migrate