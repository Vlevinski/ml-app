from sqlalchemy import create_engine
import pandas as pd

# db_engine
db_str = 'mysql+pymysql://mysql_user:mysql_password@mysql_host/mysql_db'
db_eng = create_engine(db_str)

# csv to sql DB
ml_data = pd.read_csv('ml_data.csv')
ml_data.to_sql('db_table_name', db_eng, if_exists='append', index = False, chunksize = 10000)

# read ml_data from sql_db
df = pd.read_sql('SELECT * FROM table_name', con=db_eng)