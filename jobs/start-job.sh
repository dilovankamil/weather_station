#!/bin/sh
pm2 delete fetch-weather-data-job

pm2 start ./main.py --interpreter ./venv/bin/python --cron "* * * * *" --name fetch-weather-data-job --no-autorestart
