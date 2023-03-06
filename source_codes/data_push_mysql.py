# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 14:34:33 2023

Database Project 1
"""

import mysql.connector as mysql
from mysql.connector import Error
import pandas as pd
import numpy as np


HOST= "*******"
PORT="3306"
DATABASE = "***"
USER = "******"
PASSWORD = "**********"

database_connect = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT)
print("connection status",database_connect.get_server_info())
print("------------------------------------------------------")
print()

_executor = database_connect.cursor()
result = _executor.execute("show tables;")
print("Tables Present in Database:",_executor.fetchall())
print("-------------------------------------------------")
print()

# Inserting into the above tables

## Inserting values into games
print("Inserting values into relation games.....\n")
games_csv_path ="./csv_files/games.csv"
games_df = pd.read_csv(games_csv_path)
games_df["gameDate"] = pd.to_datetime(games_df["gameDate"]).dt.date

try:
    for _index,row_value in games_df.iterrows():
        query = "INSERT INTO "+DATABASE+".games VALUES (%s,%s,%s,%s,%s,%s,%s)"
        _executor.execute(query,tuple(row_value))
        database_connect.commit()
    print("successfully inserted")
except  mysql.connector.Error as e:
    print(e)
    



## Inserting values into plays
print("Inserting values into relation plays.....\n")
plays_csv_path ="./csv_files/plays.csv"
plays_df = pd.read_csv(plays_csv_path)
plays_df = plays_df.where(pd.notnull(plays_df),None)
plays_df = plays_df.replace(np.nan,None,regex=True)
try:
    for _index,row_value in plays_df.iterrows():
        query = "INSERT INTO "+DATABASE+".plays VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        _executor.execute(query,tuple(row_value))
        database_connect.commit()
    print("successfully inserted")
except  Error as e:
    print(e)
    
## Inserting values into players
print("Inserting values into relation players.....\n")
players_csv_path ="./csv_files/players.csv"
players_df = pd.read_csv(players_csv_path)
players_df = players_df.where(pd.notnull(players_df),None)
players_df = players_df.replace(np.nan,None,regex=True)
players_df["birthDate"] = pd.to_datetime(players_df["birthDate"]).dt.date

try:
    for _index,row_value in players_df.iterrows():
        query = "INSERT INTO "+DATABASE+".players VALUES (%s,%s,%s,%s,%s,%s,%s)"
        _executor.execute(query,tuple(row_value))
        database_connect.commit()
    print("successfully inserted")
except  Error as e:
    print(e)

## Inserting values into Scouting
print("Inserting values into relation scouting.....\n")
scouting_csv_path ="./csv_files/pffScoutingData.csv"
scouting_df = pd.read_csv(scouting_csv_path)
scouting_df = scouting_df.where(pd.notnull(scouting_df),None)
scouting_df = scouting_df.replace(np.nan,None,regex=True)
query_list = []
query = "INSERT INTO "+DATABASE+".scouting VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

try:
    for _index,row_value in scouting_df.iterrows():
        query_list.append(tuple(row_value))
        if(len(query_list) == 200):
            _executor.executemany(query,query_list)
            database_connect.commit()
            query_list = []
    if(len(query_list) != 0):
        _executor.executemany(query,query_list)
        database_connect.commit()
        query_list = []
    print("successfully inserted")
except  Error as e:
    print(e)
    

## Inserting values into tracking_sample_week
print("Inserting values into relation tracking_sample_week.....\n")
tracking_sample_week_csv_path ="./csv_files/week2.csv"
tracking_sample_week_df = pd.read_csv(tracking_sample_week_csv_path)
tracking_sample_week_df = tracking_sample_week_df.where(pd.notnull(tracking_sample_week_df),None)
tracking_sample_week_df = tracking_sample_week_df.replace(np.nan,None,regex=True)
query_list = []
query = "INSERT INTO "+DATABASE+".tracking_sample_week VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
_row_value = None

try:
    for _index,row_value in tracking_sample_week_df.iterrows():
        _row_value = row_value
        query_list.append(tuple(row_value))
        if(len(query_list) == 300):
            _executor.executemany(query,query_list)
            database_connect.commit()
            query_list = []
    if(len(query_list) != 0):
        _executor.executemany(query,query_list)
        database_connect.commit()
        query_list = []
        
    print("successfully inserted")
except  Error as e:
    print(e)

    
    

_executor.close()
database_connect.close()