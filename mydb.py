import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='89674523e'
)

cursorObj = dataBase.cursor()
cursorObj.execute("CREATE DATABASE crm_db")

print('Done!')

