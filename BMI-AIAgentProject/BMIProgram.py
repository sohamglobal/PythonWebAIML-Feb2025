from openai import OpenAI
from datetime import date

client=OpenAI(api_key="sk-proj-FeEsIER6uwNFMrsgvSsP8YhP9UVPgnNKW-FHGSJRA197BcU9HBi9YhjT-m7mjhKFbBgcvtT3BlbkFJYUS-GQWowXl30UTXYfpVgRVLtMf5Mbkb-z8Tqt81FtmLsqClf8LzB803oPRNzXfHX9yfU_if8A")

def chat_gpt(prompt):
    response=client.chat.completions.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content.strip()

nm=input('Enter name : ')
wt=input('Enter weight in kg : ')
ht=input('Enter height in meters : ')
today = date.today()

prompt=f'''
you are a fitness consultant. take data from the customer. 
you received an enquiry on date {today} of 
customer name is {nm} weight is {wt} kg and height is {ht} meters. 
calculate bmi of the customer. generate diet & workout suggestions
in two sentences to 
improve bmi and maintain fitness. Return the information in JSON format 
without code. the keys in JSON document will be visitdate, name, weight, height, 
bmi, bmi_status, dietsuggestion, workoutsuggestion. use enquiry date as the value of 
visitdate
''' 
response=chat_gpt(prompt)
print(response)
