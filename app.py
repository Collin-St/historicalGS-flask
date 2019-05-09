from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from config import DB_CONFIG
import json
import numpy as np

app = Flask(__name__)
app.config['MYSQL_HOST'] = DB_CONFIG['host']
app.config['MYSQL_USER'] = DB_CONFIG['user']
app.config['MYSQL_PASSWORD'] = DB_CONFIG['password']
app.config['MYSQL_DB'] = DB_CONFIG['database']

mysql = MySQL(app)


@app.route('/commodity')
def commodity():
    commodity = request.args.get('commodity')
    start = request.args.get('start')
    end = request.args.get('end')

    cur = mysql.connection.cursor()

    json_res = []
    mean = 0
    varList = []

    if commodity == 'gold':
        cur.execute("""SELECT * FROM gold 
                    WHERE date(date) BETWEEN date(%s) AND date(%s)
                    ORDER BY date desc""", [end, start])
        headers = [x[0] for x in cur.description]
        val = cur.fetchall()
        for res in val:
            json_res.append(dict(zip(headers, res)))
            num = res[2].split(',')[0] + res[2].split(',')[1]
            mean = mean + float(num)
            varList.append(float(num))
        json_res.append(['mean', round(mean/len(val), 2)])
        json_res.append(['variance', np.var(varList)])
        return json.dumps(json_res)
    elif commodity == 'silver':
        cur.execute("""SELECT * FROM silver 
                    WHERE date(date) BETWEEN date(%s) AND date(%s)
                    ORDER BY date desc""", [end, start])
        headers = [x[0] for x in cur.description]
        val = cur.fetchall()
        for res in val:
            json_res.append(dict(zip(headers, res)))
            mean = mean + float(res[2])
            varList.append(float(res[2]))
        json_res.append(['mean', round(mean/len(val), 2)])
        json_res.append(['variance', np.var(varList)])
        return json.dumps(json_res)


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
