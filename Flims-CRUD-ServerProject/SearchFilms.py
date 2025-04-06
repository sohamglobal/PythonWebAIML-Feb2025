#!C:\Users\praff\AppData\Local\Programs\Python\Python312\python
print('content-type:text/html')
print()

import cgi
import pymysql

reqobj=cgi.FieldStorage()
gn=reqobj.getvalue("genre")

con=pymysql.connect(host='mysql-ethan-python-mysql.h.aivencloud.com',port=10413,user='praffull',password='AVNS_owESNvPFD5fnVDwuWUq',database='sharayudb')
curs=con.cursor()

curs.execute(f"select * from films where genre='{gn}'")
data=curs.fetchall()

print('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7" crossorigin="anonymous">')
print("<body style='margin-top:45px'>")
print("<div class='container'>")
print(f"<h2 class='display-4'>Search Result for {gn}</h2><hr>")

print("<table class='table table-bordered table-hover'>")
print("<tr>")
print("<th>Number")
print("<th>Name")
print("<th>Year")
print("<th>Language")
print("<th>Genre")
print("<th>Rating")
print("</tr>")


for film in data:
    print("<tr>")
    print("<td>",film[0])
    print("<td>",film[1])
    print("<td>",film[2])
    print("<td>",film[3])
    print("<td>",film[4])
    print("<td>",film[5])
    print("</tr>")


print("</table>")

con.close()

print("<br><br><a href='index.html'>Home</a>")