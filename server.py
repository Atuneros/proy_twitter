from __future__ import print_function
import findspark
findspark.init()
import pyspark
sc = pyspark.SparkContext(appName="SERVER")
from pyspark.sql.session import SparkSession
spark = SparkSession(sc)

f = open("archivo.txt","w")
f.write("")
f.close()

import re
import unicodedata
from operator import add
import sys
from googletrans import Translator
import mysql.connector
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

conn = mysql.connector.connect(
   user='admin', password='12345', host='127.0.0.1', database='tweets')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()
sql = "INSERT INTO tweets (texto) VALUES (%s)"
# Create a local StreamingContext with two working thread and batch interval of 1 second
#sc = SparkContext("local[2]", "NetworkWordCount")
sc.setLogLevel("ERROR")
ssc = StreamingContext(sc, 5)

translator = Translator()

def bbdd(si):
    f = open("archivo.txt","a+")
    for x in si:
        f.write(x+"\n")
    f.close()
    

def vader(sentence):
    analyser = SentimentIntensityAnalyzer()
    sentence.foreach(lambda x : print(x, analyser.polarity_scores(x)))
    si = sentence.map(lambda x : x).collect()
    bbdd(si)

# We need to create the checkpoint
ssc.checkpoint("checkpoint")

# Create a DStream that will connect to hostname:port, like localhost:9999
lines = ssc.socketTextStream("localhost", 10002)

lines.foreachRDD(vader)

# Print the first ten elements of each RDD generated in this DStream to the console
lines.pprint()

ssc.start()             # Start the computation
ssc.awaitTermination()  # Wait for the computation to terminate
conn.commit()