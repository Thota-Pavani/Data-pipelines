from pymongo import MongoClient
import configparser
import pandas as pd


def extract(data):
    config=configparser.ConfigParser()
    config.read(r'C:\Users\Lokesh\Documents\python\day6\config.config')

    url=config['lokesh']['url']

    client=MongoClient(url)

    db=client['firstdb']#database name

    collect=db[data]

    #collect2=db["project2"]

    doc=list(collect.find())
    #return doc1
    #doc2=list(collect2.find())

    df=pd.DataFrame(doc)
    umd.update_log(source='mongoDb',action='extracted the text data from database')
    
    return df
    
    #df2=pd.DataFrame(doc2)



