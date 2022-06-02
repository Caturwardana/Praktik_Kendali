# app.py
# KELOMPOK 1 ARM 2 (CATUR WARDANA, SANTI RAHAYU)
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import datetime, time

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1111'
app.config['MYSQL_DB'] = 'adc_potensio_reader'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/post', methods=["GET", "POST"])
def post():

    adc_potensio = (request.data)
    print(adc_potensio)
    
    cur = mysql.connection.cursor()
    for i in range(10):
        now = datetime.datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        time.sleep(3)
        adc_potensio = (request.data)
        status = "ON"

        cur.execute("INSERT INTO potensio (datetime, status, adc_potensio) VALUES (%s, %s, %s)", (date_time, status, adc_potensio))
        mysql.connection.commit()
    return ('', 204)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)