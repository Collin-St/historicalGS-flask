# historicalGS-flask
Flask API for historicalGoldSilver

This app provides a Flask API for https://github.com/Collin-St/historicalGoldSilver

# Run this code

From the terminal, clone this repo:
`https://github.com/Collin-St/historicalGS-flask.git && cd historicalGS-flask`

Provide config options for MySQL as done for https://github.com/Collin-St/historicalGoldSilver

Run Flask: `python3 app.py`

Navigate to an endpoint on http://localhost:8080/ following this format:
http://localhost:8080/commodity?commodity=gold&start=2019-5-09&end=2019-5-01
or 
http://localhost:8080/commodity?commodity=silver&start=2019-5-09&end=2019-5-01
