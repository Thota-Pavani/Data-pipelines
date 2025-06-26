import pandas as pd
def s1(a,newa):
    updateda=a.merge(newa[['customer_id','email']],on='customer_id',how='left',suffixes=('','_new'))
    updateda['email']=updateda['email_new'].combine_first(updateda['email'])
    #print(updatedf)
    updateda.drop(columns=['email_new'],inplace=True)
    return updateda
def s2(a):
    b={
        "customer_id":3,
        "email":"mspavani@gmail.com"
    }
    c=a.loc[a['customer_id']==b['customer_id']].copy()
    c['email']=b['email']
    a=pd.concat([a,c],axis=0)
    return a     
def s3(a,newa):
    updateda=a.merge(newa[['customer_id','email']],on='customer_id',how='left',suffixes=('','_new'))
    return updateda