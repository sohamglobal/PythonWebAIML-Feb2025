import os

dnm=input('Enter directory name : ')
try:
    os.mkdir(dnm)
    print('directory created')
except:
    print('already present')