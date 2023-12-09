#!/bin/bash

# Start command for flask app
poetry run flask --app src/app.py run &

# Wait for flask app to be ready to receive requests
while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5000/)" != "200" ]];
  do sleep 1;
done

# Run robot-framework tests
poetry run robot src/tests

status=$?

# Halt Flask-server on port 5000
kill $(lsof -t -i:5000)

exit $status
