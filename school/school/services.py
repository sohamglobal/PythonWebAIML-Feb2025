import pymysql

class DataOperations:
    def serachaccountnumber(self,no):
        con=pymysql.connect(host='mysql-ethan-python-mysql.h.aivencloud.com',port=10413,user='praffull',password='AVNS_owESNvPFD5fnVDwuWUq',database='sharayudb')
        curs=con.cursor()
        curs.execute(f"select accnm,balance from accounts where accno={no}")
        data=curs.fetchone()
        con.close()
        dic={}
        if data:
            dic["name"]=data[0]
            dic["balance"]=data[1]
        else:
            dic["name"]="Not found"
            dic["balance"]="NA"

        return dic
    
    def collectallemps(self):
        con=pymysql.connect(host='mysql-ethan-python-mysql.h.aivencloud.com',port=10413,user='praffull',password='AVNS_owESNvPFD5fnVDwuWUq',database='sharayudb')
        curs=con.cursor()
        curs.execute("select * from employees")
        data=curs.fetchall()
        con.close()
        return data
