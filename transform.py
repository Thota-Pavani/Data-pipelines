import pandas as pd
def transformations(df):
    df=df.drop_duplicates()
    df=df.sort_values(by='registration_date',ascending=True)
    df['customers_per_status'] = df.groupby('loyalty_status')['customer_id'].transform('count')
    return df
    
    