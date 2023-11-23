#!/bin/bash
# starts postgren on fresher laptop:
# start-pg.sh &
# käynnistetään Flask-palvelin taustalle

#poetry run python3 src/index.py &
poetry run flask --app src/app.py run &

# odetetaan, että palvelin on valmiina ottamaan vastaan pyyntöjä
while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5000/)" != "200" ]];
  do sleep 1;
done

# suoritetaan testit
poetry run robot src/tests

status=$?

# pysäytetään Flask-palvelin portissa 5000
kill $(lsof -t -i:5000)

exit $status

# shuts down postgre on fresher laptop
# kill $(ps x|grep pgsql/bin/postgres|grep -v grep|awk '{print $1}')