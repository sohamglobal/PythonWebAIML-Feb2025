#pip install pymysql
#pip install cryptography
#pip install waitress
#pip install flask-cors
from flask import Flask
from flask_restful import Resource,Api
import pymysql
from waitress import serve
from flask_cors import CORS

app=Flask(__name__)
api=Api(app)
CORS(app)

class AccountInfo(Resource):
    def get(self,ano):
        dic={}
        con=pymysql.connect(host='mysql-ethan-python-mysql.h.aivencloud.com',port=10413,user='praffull',password='AVNS_owESNvPFD5fnVDwuWUq',database='sharayudb')
        curs=con.cursor()
        curs.execute(f"select accnm,balance from accounts where accno={ano}")
        data=curs.fetchone()
        if data:
            dic['name']=data[0]
            dic['balance']=data[1]
        else:
            dic['name']='not found'
            dic['balance']=0.0
        con.close()
        return dic

api.add_resource(AccountInfo,'/account/search/<ano>')
serve(app,port=5009)



