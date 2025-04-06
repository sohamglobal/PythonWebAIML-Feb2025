#!C:\Users\praff\AppData\Local\Programs\Python\Python312\python
print('content-type:text/html')
print()

import cgi
import pymysql

reqobj=cgi.FieldStorage()
no=int(reqobj.getvalue("film_number"))
rt=float(reqobj.getvalue("new_rating"))

con=pymysql.connect(host='mysql-ethan-python-mysql.h.aivencloud.com',port=10413,user='praffull',password='AVNS_owESNvPFD5fnVDwuWUq',database='sharayudb')
curs=con.cursor()

curs.execute(f"update films set imdb_rating={rt} where filmno={no}")
con.commit()
con.close()

print('update done')