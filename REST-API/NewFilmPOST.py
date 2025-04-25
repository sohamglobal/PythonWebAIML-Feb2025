from flask import Flask,request
import pymysql

app=Flask(__name__)

@app.route('/film/add',methods=['POST'])
def addnewfilm():
    fnm=request.form.get("filmnm")
    ryr=int(request.form.get("year"))
    ln=request.form.get("lang")
    gn=request.form.get("genre")
    rt=float(request.form.get("rating"))
    dic={}
    try:
        con=pymysql.connect(host='mysql-ethan-python-mysql.h.aivencloud.com',port=10413,user='praffull',password='AVNS_owESNvPFD5fnVDwuWUq',database='sharayudb')
        curs=con.cursor()
        curs.execute(f"insert into films(film_name,release_year,language,genre,imdb_rating) values ('{fnm}',{ryr},'{ln}','{gn}',{rt})")
        con.commit()
        con.close()
        dic['status']='success'
    except:
        dic['status']='failed'
    return dic

app.run(debug=True)