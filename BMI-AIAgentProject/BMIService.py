# pip install flask-cors
from flask import Flask,request
from openai import OpenAI
from datetime import date
from flask_cors import CORS
from pymongo import MongoClient
import json

app=Flask(__name__)
CORS(app)

client=OpenAI(api_key="sk-proj-FeEsIER6uwNFMrsgvSsP8YhP9UVPgnNKW-FHGSJRA197BcU9HBi9YhjT-m7mjhKFbBgcvtT3BlbkFJYUS-GQWowXl30UTXYfpVgRVLtMf5Mbkb-z8Tqt81FtmLsqClf8LzB803oPRNzXfHX9yfU_if8A")

def chat_gpt(prompt):
    response=client.chat.completions.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content.strip()

@app.route('/bmi/suggest',methods=['POST'])
def suggest():
    nm=request.form.get("name")
    wt=request.form.get("weight")
    ht=request.form.get("height")
    today = date.today()
    #print(nm+" "+wt+" "+ht)
    prompt=f'''
    you are a fitness consultant. take data from the customer. 
    you received an enquiry on date {today} of 
    customer name is {nm} weight is {wt} kg and height is {ht} meters. 
    calculate bmi of the customer. generate diet & workout suggestions
    in two sentences to 
    improve bmi and maintain fitness. Return the information in JSON format 
    without code. the keys in JSON document will be visitdate, name, weight, height, 
    bmi, bmi_status, dietsuggestion, workoutsuggestion. use enquiry date as the value of 
    visitdate. bmi_status must be underweight, normal, overweight, obese
    ''' 
    response=chat_gpt(prompt)
    #MongoDB insert code
    client=MongoClient("mongodb+srv://sharayu:mongodb913@praffullcluster.jfybhkc.mongodb.net/?retryWrites=true&w=majority&appName=praffullcluster")
    db=client["spiderdb"]
    coll=db["bmidata"]
    dic=json.loads(response)
    coll.insert_one(dic)
    return response


app.run(host='0.0.0.0',port=5000,debug=True)
#app.run(debug=True)