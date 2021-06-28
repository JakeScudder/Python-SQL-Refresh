import mysql.connector

config = {
  "user": "root",
  "password": "",
  "host": "localhost",
  "database": "python_sql_refresh"
}

db = mysql.connector.connect(**config)
cursor = db.cursor()