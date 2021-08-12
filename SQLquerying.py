import pymysql
import json
from datetime import datetime, timedelta
import pandas as pd


#Anomaly values of Spo2 and heartbeat in bpms
spo2=98
bpm=85
try:
   #Connecting the SQL server to the python file
   connection = pymysql.connect(host="sql6.freesqldatabase.com", user="sql642993", passwd="4XUSttYXwW",database="sql6429938", autocommit=True )
   cursor = connection.cursor()

   #Selecting the last 10 values from the table
   retrive = ("SELECT * FROM (SELECT * FROM healthData ORDER BY Timestamp DESC LIMIT 10)Var1 ORDER BY Timestamp ASC;")
   cursor.execute(retrive)
   #Retrieving the data as rows
   rows = cursor.fetchall()
   #Forming proper structure of data in the form of JSON for charting
   inner_dict=[{'Timestamp':(rows[i][0] + timedelta(hours=5, minutes=50)).strftime("%b %d %H:%M"), 'SpO2':rows[i][1], 'bpm':rows[i][2]}
              for i,_ in enumerate(rows)]
   if not bool(inner_dict):
      dummy=pd.read_csv('dummy_data.csv')
      inner_dict=[{'Timestamp': dummy.iloc[i,0], 'SpO2': int(dummy.iloc[i,1]), 'bpm': int(dummy.iloc[i,2])} for i in range(dummy.shape[0])]
   dictionary={'data':inner_dict}
   #print(dictionary)


except pymysql.Error as e:
   dummy=pd.read_csv('dummy_data.csv')
   data_dict=[{'Timestamp': dummy.iloc[i,0], 'SpO2': int(dummy.iloc[i,1]), 'bpm': int(dummy.iloc[i,2])} for i in range(dummy.shape[0])]
   dictionary={'data':data_dict}
   #print(dictionary)

#print(dictionary)

def last_tendata():
   return dictionary

def check_anamoly():
   df=pd.DataFrame(dictionary)
   #Taking the dataframe that only has the anamoly values
   fd=df[(df['SpO2']<spo2) | (df['bpm']<bpm)]
   return fd


   


#cursor.close()
#connection.close()
