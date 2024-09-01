import mysql.connector

config = {
  'user': 'root',
  'password': '09102020',
  'host': '127.0.0.1',
  'database': 'basededatos_vamar',
  'raise_on_warnings': True
}

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
except mysql.connector.Error as err:
    print("Error de conexión: {}".format(err))
