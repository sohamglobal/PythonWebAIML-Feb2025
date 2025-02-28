import json

laptop={
    "brand":"dell",
    "model":"latitude 5490",
    "color":"black",
    "ram":"16 gb",
    "ssd":"512 gb",
    "processor":"intel i5 8 gen",
    "touchscreen":"yes",
    "price":79000.00
}
file=open("mylaptop.json","w")
json.dump(laptop,file)
file.close()
print('laptop data stored in a json file')