#call a local Flask REST API
from urllib import request
import json

no=input('Enter account number : ')

response=request.urlopen("http://127.0.0.1:5009/account/search/"+no)
data=response.read()
info=json.loads(data)
print(info)
print('-'*30)
print('Name : ',info['name'])
print('Balance : ',info['balance'])
