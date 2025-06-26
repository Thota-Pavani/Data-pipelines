import configparser
import urllib.parse
from sqlalchemy import create_engine
import pandas as pd
def extract_table(table_name:str):
    config = configparser.ConfigParser()
    config.read(r'C:\Users\Dell\Desktop\mysqltasks\config.ini')
 
    username = config['mysql']['username']
    password = config['mysql']['password']
    host     = config['mysql']['host']
    database = config['mysql']['database']
    driver   = config['mysql']['driver']
 
    encoded_password = urllib.parse.quote_plus(password)
 
    connection_string = f"mysql+{driver}://{username}:{encoded_password}@{host}/{database}"
    engine = create_engine(connection_string)
   
    # to load csv to mysql
    #orders=pd.read_csv("us_customers_data 1.csv")
    #orders.to_sql(name="orders",con=engine,if_exists='replace',index=False)
 
    #fetch orders table from MYSQLDB
    fetch_table = pd.read_sql_table(table_name,con=engine)
    return fetch_table
 
    #return fetch_table
#import configparser
#import urllib.parse
#from sqlalchemy import create_engine
#import pandas as pd

def load_csv_to_mysql(table_name: str, csv_path: str):
    # Read database configuration
    config = configparser.ConfigParser()
    config.read(r'C:\Users\Dell\Desktop\mysqltasks\config.ini')
 
    username = config['mysql']['username']
    password = config['mysql']['password']
    host     = config['mysql']['host']
    database = config['mysql']['database']
    driver   = config['mysql']['driver']
 
    encoded_password = urllib.parse.quote_plus(password)
 
    # MySQL connection string
    connection_string = f"mysql+{driver}://{username}:{encoded_password}@{host}/{database}"
    engine = create_engine(connection_string)

    # Load CSV into DataFrame
    df = pd.read_csv(csv_path)

    # Load DataFrame into MySQL table
    df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

    print(f"✅ Data loaded successfully into `{table_name}` table.")



