from flask import Flask
from flask_restful import Resource,Api
import pymysql

app=Flask(__name__)
api=Api(app)

class EmployeesInfo(Resource):
    def get(self):
        con=pymysql.connect(host='mysql-ethan-python-mysql.h.aivencloud.com',port=10413,user='praffull',password='AVNS_owESNvPFD5fnVDwuWUq',database='sharayudb')
        curs=con.cursor()
        curs.execute("select * from employees")
        data=curs.fetchall()
        dic={}
        dic['data']=data
        return dic


api.add_resource(EmployeesInfo,'/emp/all')
app.run(debug=True)
