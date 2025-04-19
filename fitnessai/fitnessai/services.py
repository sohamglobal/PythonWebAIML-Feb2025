import pymysql

class FitnessServices:
    def authenticate(self,userid,pswd):
        flag=False
        con=pymysql.connect(host='mysql-ethan-python-mysql.h.aivencloud.com',port=10413,user='praffull',password='AVNS_owESNvPFD5fnVDwuWUq',database='sharayudb')
        curs=con.cursor()
        qr=f"select * from users where userid='{userid}' and password='{pswd}'"
        curs.execute(qr)
        data=curs.fetchone()
        if data:
            flag=True
        else:
            flag=False
        
        return flag




    def addnewprofile(self, name, age, gender, height, weight, bmi, food,steps):
        flag=False
        con=pymysql.connect(host='mysql-ethan-python-mysql.h.aivencloud.com',port=10413,user='praffull',password='AVNS_owESNvPFD5fnVDwuWUq',database='sharayudb')
        curs=con.cursor()
        str=f"insert into fitness_profile(person_name,age,gender,height_cm,weight_kg,bmi,food_type,steps_per_day,recorded_on) values('{name}',{age},'{gender}',{height},{weight},{bmi},'{food}',{steps},curdate())"
        curs.execute(str)
        con.commit()
        curs.close()
        con.close()
        
        print(str)
        flag=True
        return flag

    def modifyprofile(self,profid,wtkg,steps):
        flag=False
        con=pymysql.connect(host='mysql-ethan-python-mysql.h.aivencloud.com',port=10413,user='praffull',password='AVNS_owESNvPFD5fnVDwuWUq',database='sharayudb')
        curs=con.cursor()
        qr=f"update fitness_profile set weight_kg={wtkg},steps_per_day={steps},recorded_on=curdate() where profileid={profid}"
        curs.execute(qr)
        qr=f"update fitness_profile set bmi=round(weight_kg/((height_cm/100)*(height_cm/100))) where profileid={profid}"
        curs.execute(qr)
        con.commit()
        con.close()
        flag=True
        return flag