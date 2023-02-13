from typing import List, Dict
from flask import Flask,jsonify, request
from flask_cors import CORS

import mysql.connector
import json

config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'testdb'
    }

app = Flask(__name__)
CORS(app)

# Route for fetch a data
@app.route('/api/get')
def favorite_colors() -> List[Dict]:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM testtable')
    results =cursor.fetchall()
    cursor.close()
    connection.close()
    return json.dumps(results)

# Route for add a data
@app.route('/api/insert', methods = ['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
      connection = mysql.connector.connect(**config)
      param = request.args
      val = (param.get('name'),param.get('age') , param.get('gender'), param.get('city'))
      cursor = connection.cursor(dictionary=True)
      sql = "INSERT INTO testtable (name, age, gender, city) VALUES (%s, %s, %s, %s)"
      cursor.execute(sql, val)
      connection.commit()
      cursor.close()
      return cursor


# Route for update a data
@app.route('/api/update/<id>', methods = ['GET', 'POST'])
def update_user(id):
      connection = mysql.connector.connect(**config)
      cursor = connection.cursor(dictionary=True)
      if request.method == 'POST':
        connection = mysql.connector.connect(**config)
        print(request.args.get('name'))
        param = request.args
        val = (param.get('name'),param.get('age') , param.get('gender'), param.get('city'),id)
        cursor = connection.cursor(dictionary=True)
        sql = "UPDATE testtable SET name=%s, age=%s, gender=%s, city=%s WHERE id =%s"
        cursor.execute(sql, val)
        connection.commit()
        cursor.close()
        return cursor
      sql = "SELECT * FROM testtable WHERE id = %s"
      cursor.execute(sql,[id])
      result = cursor.fetchone()
      return result

# Route for delete a data
@app.route('/api/delete/<id>', methods=['GET','POST','DELETE'])
def delete_user(id) -> List[Dict]:
    print("delete",id)
    if request.method == 'DELETE':
      connection = mysql.connector.connect(**config)
      cursor = connection.cursor(dictionary=True)
      sql = "DELETE FROM testtable WHERE id=%s"
      cursor.execute(sql,(id,))
      connection.commit()
      cursor.close()
      return json.dumps('delete')


# def index() -> str:
#     return json.dumps({'favorite_colors': favorite_colors()})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')