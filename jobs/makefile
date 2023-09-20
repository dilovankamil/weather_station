.SILENT: start-jobs install-dependencies

start-jobs: install-dependencies
	echo "Starting new jobs:"
	pm2 start ./main.py --cron "* * * * *" --name fetch-weather-data-job --no-autorestart
	
install-dependencies: requirements.txt
	echo "Installing dependencies:"
	pip install -r requirements.txt
