name=input('Enter film name : ')
year=input('Enter year : ')
lang=input('Enter language : ')
genre=input('Enter genre : ')
rating=input('Enter IMDBrating : ')

file=open("films.csv","a")
file.write(f'{name},{year},{lang},{genre},{rating}\n')
file.close()