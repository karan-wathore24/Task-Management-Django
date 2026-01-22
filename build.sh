#!/usr/bin/env bash
# Exit on error
set -o errexit

# 1. Install dependencies from the root directory
pip install -r requirements.txt

# 2. Go into the folder where manage.py is located
cd todo_list

# 3. Run the Django commands from inside that folder
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate