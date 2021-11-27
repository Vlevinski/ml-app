import sqlite3
import pandas as pd

# db connection
db = sqlite3.connect('ml_data.db')
c = db.cursor()

# csv to sqlite
ml_data = pd.read_csv('ml_data.csv')
ml_data.to_sql('ml_data', db, if_exists='append', index = False, chunksize = 10000)