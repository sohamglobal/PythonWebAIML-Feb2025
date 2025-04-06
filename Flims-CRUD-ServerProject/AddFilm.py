#!C:\Users\praff\AppData\Local\Programs\Python\Python312\python
print('content-type:text/html')
print()

import cgi
import pymysql

reqobj=cgi.FieldStorage()
nm=reqobj.getvalue("film_name")
yr=int(reqobj.getvalue("release_year"))
ln=reqobj.getvalue("language")
gn=reqobj.getvalue("genre")
rt=float(reqobj.getvalue("imdb_rating"))

#print(nm+str(yr)+ln+gn+str(rt))
print('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7" crossorigin="anonymous">')
print("<body style='margin-top:45px'>")
print("<div class='container'>")

try:
    con=pymysql.connect(host='mysql-ethan-python-mysql.h.aivencloud.com',port=10413,user='praffull',password='AVNS_owESNvPFD5fnVDwuWUq',database='sharayudb')
    curs=con.cursor()
    curs.execute(f"insert into films(film_name,release_year,language,genre,imdb_rating) values('{nm}',{yr},'{ln}','{gn}',{rt}) ")
    con.commit()
    print('<h2 class="display-4">New film added to the database</h2>')
    con.close()
except:
    print('operation failed')

print("<br><br><a href='index.html'>Home</a>")