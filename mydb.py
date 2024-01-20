# install Mysql on your system
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'dontBreakin1!',

)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE hirabooks")

print("All Done!")