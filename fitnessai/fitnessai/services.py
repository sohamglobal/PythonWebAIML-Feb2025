import pymysql

class FitnessServices:
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

