from urllib import request
import json

ct=input('Enter city : ')

response=request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+ct+"&appid=5ea9269ece0f0c287803a5b69fca4d80")
data=response.read()
info=json.loads(data)
#print(info)
print('Weather Description : ',info['weather'][0]['description'])
k=info['main']['feels_like']
c = k - 273.15
print('Feels like : %.2f' %c)