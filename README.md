# open-survey-tool

The **sagsderpolizei.de** is a survey tool with special focus on privacy and anonymity of participants. It is designed
to provide feedback to government authorities and other government institutions without them being able to track who has
provided the feedback.

## Project origin

The project started at the UpdateDeutschland 48h-Sprint.

## Dev setup

1. Mark `src/open_survey_tool` as source root in Pycharm
1. `cd src/ && python -m venv venv`
1. `source venv/bin/activate`
1. `pip install -r src/requirements-dev.txt`
1. `docker-compose up -d`
1. In `src/open_survey_tool` run `python manage.py migrate`