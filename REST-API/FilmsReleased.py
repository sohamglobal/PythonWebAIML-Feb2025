from flask import Flask
from flask_restful import Resource,Api
import pymysql

app=Flask(__name__)
api=Api(app)

class FilmsSearch(Resource):
    def get(self,ryear):
        dic={}
        con=pymysql.connect(host='mysql-ethan-python-mysql.h.aivencloud.com',port=10413,user='praffull',password='AVNS_owESNvPFD5fnVDwuWUq',database='sharayudb')
        curs=con.cursor()
        curs.execute(f"select * from films where release_year={ryear}")
        data=curs.fetchall()
        if data:
            dic['films']=data
        else:
            dic['films']='not found'
        con.close()
        return dic

api.add_resource(FilmsSearch,"/films/year/<ryear>")
app.run(debug=True)
