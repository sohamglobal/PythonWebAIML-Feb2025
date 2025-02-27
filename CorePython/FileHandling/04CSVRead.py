file=open("films.csv","r")

data=file.readline()
while data:
    #print(data)
    print(data.split(',')[0])
    data=file.readline()
    
file.close()