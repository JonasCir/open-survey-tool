#!/bin/bash
set -e

cd src/open_survey_tool/

# run migration
python3 manage.py migrate
echo "Migration successful"

cd open_survey_tool/

uwsgi --ini uwsgi.ini
