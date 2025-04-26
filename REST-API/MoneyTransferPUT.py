from flask import Flask,request
import pymysql

app=Flask(__name__)

@app.route("/account/transfer",methods=['PUT'])
def transfermoney():
    fno=int(request.form.get("fromano"))
    tno=int(request.form.get("toano"))
    amt=float(request.form.get("amount"))
    det=request.form.get("details")
    dic={}
    try:
        con=pymysql.connect(host='mysql-ethan-python-mysql.h.aivencloud.com',port=10413,user='praffull',password='AVNS_owESNvPFD5fnVDwuWUq',database='sharayudb')
        curs=con.cursor()
        curs.execute(f"update accounts set balance=balance-{amt} where accno={fno}")
        curs.execute(f"update accounts set balance=balance+{amt} where accno={tno}")
        curs.execute(f"insert into transferlog(fromacc,toacc,amount,details,transdt) values({fno},{tno},{amt},'{det}',now())")
        con.commit()
        dic['message']="transfer successful"
        con.close()
    except:
        dic['message']="transfer failed"
    
    return dic

app.run(debug=True)