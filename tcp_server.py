from googletrans import Translator
import mysql.connector

translator = Translator()

#establishing the connection
conn = mysql.connector.connect(
   user='admin', password='12345', host='127.0.0.1', database='tweets')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

sql = "INSERT INTO tweets (texto) VALUES (%s)"

logfile = open("archivo.txt","r")

for x in logfile:
   print(x)
   tr = translator.translate(x).text
   cursor.execute(sql, (tr,))
   print(tr)
conn.commit()