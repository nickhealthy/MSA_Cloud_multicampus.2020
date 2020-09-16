
import pandas as pd

table_df = pd.read_json('data/members.json')
table_df.info()


import pymysql
import sqlalchemy
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqldb://project:"+"project"+"@192.168.0.12:3306/project_db",encoding="utf-8")
conn = engine.connect()

table_df.to_sql(name='members', con=engine, if_exists='replace', index=True, \
              index_label='id')