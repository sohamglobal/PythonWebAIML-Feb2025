#!C:\Users\praff\AppData\Local\Programs\Python\Python312\python
print('content-type:text/html')
print()

import cgi
import pymysql

reqobj=cgi.FieldStorage()
no=int(reqobj.getvalue("film_number"))

con=pymysql.connect(host='mysql-ethan-python-mysql.h.aivencloud.com',port=10413,user='praffull',password='AVNS_owESNvPFD5fnVDwuWUq',database='sharayudb')
curs=con.cursor()

curs.execute(f"delete from films where filmno={no}")
con.commit()

print('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7" crossorigin="anonymous">')
print("<body style='margin-top:45px'>")
print("<div class='container'>")
print(f"<h2 class='display-4'>Film deleted</h2><hr>")

print("<br><br><a href='index.html'>Home</a>")