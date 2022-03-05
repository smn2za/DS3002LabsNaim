# Safya Naim, smn2za

# import necessary modules
import pandas as pd
import sqlite3 as sql3
import csv

# step 1: retrieve data (either remote or local)
# open CSV file (using pandas)
data = pd.read_csv('Tesla-dataset.csv')

# steps 2 and 3: convert to JSON and SQL + write SQL to database

# convert csv to json
data.to_json('Tesla-dataset.json')

# convert csv to SQL
# connect python to SQL Server
con = sql3.connect('Tesla-dataset.db')
cur = con.cursor()
# create empty table with column headings
cur.execute("""CREATE TABLE IF NOT EXISTS Tesladataset(
        DATE DATE PRIMARY KEY,
        OPEN FLOAT,
        HIGH FLOAT,
        LOW FLOAT,
        CLOSE FLOAT,
        ADJ CLOSE FLOAT,
        VOLUME INT);
""")
con.commit()
# turn Tesla-dataset.csv into list for filling table
with open('Tesla-dataset.csv', newline='') as f:
    reader = csv.reader(f)
    # skip the headers (date, open, etc)
    next(reader)
    TDS_list = list(reader)

# put list (list of lists?) into TDS table
TDS = TDS_list
cur.executemany("INSERT OR REPLACE INTO Tesladataset VALUES(?, ?, ?, ?, ?, ?, ?);", TDS)
con.commit()
