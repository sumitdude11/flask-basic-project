from flask import Flask, render_template, request
import mysql.connector
import numpy as np
from sklearn import linear_model
import pandas as pd
import sys

app = Flask(__name__)

@app.route('/')
def hello1():
    import csv
    print("jj")
    filename = "inter11.csv"
    print("no")
    fields = []
    rows = []

    with open(filename,'r',encoding="utf8") as csvfile:
        csvreader = csv.reader(csvfile)
        fields.append(next(csvreader))
        print("nope")
        for row2 in csvreader:
            if(int(row2[15]!=0)):
                rows.append(row2)
                conn = mysql.connector.connect(host="localhost", user="root", password="", db="thinkabout")

                cursor = conn.cursor()
                try:
                    query="select * from think WHERE NOT link_clicks=0 "
                    cursor.execute(query)
                    data=cursor.fetchall()
                    print(data[0],data[1],data[2],data[3],data[4])
                    print("\n")
                    conn.commit()
                except Exception as e:
                    conn.commit()
                    return(str(e))
        return render_template("page1.html",data=rows)




// this is used to insert data in a database
@app.route('/click')
def hello_world():
    import csv
    filename = "inter11.csv"
    fields = []
    rows = []

    with open(filename,'r',encoding="utf8") as csvfile:
        csvreader = csv.reader(csvfile)
        fields.append(next(csvreader))
        print("nope")
        for row2 in csvreader:
            if(int(row2[15]!=0)):
                print("ha")
                conn = mysql.connector.connect(host="localhost", user="root", password="", db="thinkabout")
                print("na")
                cursor = conn.cursor()
                cursor.execute(
                    "insert into think(date,link_clicks,spends,impressions,clicks) values('"+row2[0]+"','"+ row2[15] +"','"+ row2[12]+"','"+row2[13]+"',' "+row2[14]+"')")
                conn.commit()
        return render_template("index.html")

if __name__ == '__main__':
    app.run()
