#!/bin/bash
set -e

cd src/open_survey_tool/

# run migration
python3 manage.py migrate
echo "Migration successful"

python3 manage.py loaddata surveys/fixtures/example.json
echo "Fixture loading successful"

python3 manage.py runserver 0.0.0.0:8000
