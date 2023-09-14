.SILENT: start-jobs install-dependencies kill-existing-jobs

start-jobs: install-dependencies kill-existing-jobs
	echo "Starting new jobs:"
	pm2 start ./main.py --cron "* * * * *" --name fetch-weather-data-job --no-autorestart
	
install-dependencies: requirements.txt
	echo "Installing dependencies:"
	pip install -r requirements.txt

kill-existing-jobs:
	echo "Killing existing jobs:"
	pm2 delete fetch-weather-data-job | echo "Existing job fetch-weather-data-job could not be found"
