import src.loadmysql as lms
import src.transform as t
import src.scdtypes as scd
import src.loadsql as l

lms. load_csv_to_mysql("uscustomers", "us_customer_data 1.csv")
a=lms.extract_table(table_name='uscustomers')
e=t.transformations(a)
# print(e)

newa=lms.extract_table(table_name='scdtasks1')
b=scd.s1(e,newa)
c=scd.s2(b)
c.to_csv('scd_12.csv',index=False)
l.uploadtossms(c)

#e.to_csv('transformation.csv',index=False)
#l.uploadtossms(e)
# print("uploaded")
d=scd.s3(e,newa)
d.to_csv('scd3.csv',index=False)
l.uploadtossms(d)

