from flask import Flask,request
import pymysql

app=Flask(__name__)

@app.route("/account/close",methods=['DELETE'])
def delaccount():
    no=int(request.form.get("ano"))
    dic={}
    try:
        con=pymysql.connect(host='mysql-ethan-python-mysql.h.aivencloud.com',port=10413,user='praffull',password='AVNS_owESNvPFD5fnVDwuWUq',database='sharayudb')
        curs=con.cursor()
        curs.execute(f"delete from accounts where accno={no}")
        con.commit()
        dic['message']="delete successful"
        con.close()
    except:
        dic['message']="delete failed"
    
    return dic

app.run(debug=True)