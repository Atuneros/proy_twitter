from googletrans import Translator
import mysql.connector
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json

translator = Translator()
analyser = SentimentIntensityAnalyzer()
#establishing the connection
conn = mysql.connector.connect(
   user='admin', password='12345', host='127.0.0.1', database='tweets')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

sql = "INSERT INTO tweets (texto, puntuacion) VALUES (%s, %s)"

logfile = open("archivo.txt","r")

for x in logfile:
   tr = translator.translate(x).text
   an = analyser.polarity_scores(tr)
   an = json.dumps(an)
   print(type(an))
   #sql = "INSERT INTO tweets (texto, puntuacion) VALUES ({tra},{ana})".format(tra=tr, ana=an)
   cursor.execute(sql, (tr,an,))
   print(tr, an)
conn.commit()