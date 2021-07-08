import pymysql
import json
from datetime import datetime, timedelta
import pandas as pd

#Connecting the SQL server to the python file
connection = pymysql.connect(host="sql6.freesqldatabase.com", user="sql6422421", passwd="9su1EKKgZE",database="sql6422421", autocommit=True )
cursor = connection.cursor()

#Anomaly values of Spo2 and heartbeat in bpms
spo2=98
bpm=85


def last_tendata():
   #Selecting the last 10 values from the table
   retrive = ("SELECT * FROM (SELECT * FROM healthData ORDER BY Timestamp DESC LIMIT 10)Var1 ORDER BY Timestamp ASC;")
   cursor.execute(retrive)
   #Retrieving the data as rows
   rows = cursor.fetchall()
   #Forming proper structure of data in the form of JSON for charting
   inner_dict=[{'Timestamp':(rows[i][0] + timedelta(hours=5, minutes=50)).strftime("%b %d %H:%M"), 'SpO2':rows[i][1], 'bpm':rows[i][2]}
              for i,_ in enumerate(rows)]
   dictionary={'data':inner_dict}
   return dictionary

def check_anamoly():
   #Retirving all the data values
   retrive = ("SELECT * FROM healthData;")
   cursor.execute(retrive)
   rows = cursor.fetchall()
   #Forming proper structure of data in the form of dictionary followed by dataframe
   dict_=[{'Timestamp':(rows[i][0] + timedelta(hours=5, minutes=50)).strftime("%b %d %H:%M"), 'SpO2':rows[i][1], 'bpm':rows[i][2]}
              for i,_ in enumerate(rows)]
   df=pd.DataFrame(dict_)
   #Taking the dataframe that only has the anamoly values
   fd=df[(df['SpO2']<spo2) | (df['bpm']<bpm)]
   return fd

#cursor.close()
#connection.close()
