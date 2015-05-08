print ("Welcome to Pypet!")

cat = {
    'name': "Supertrooper",
    'hungry': True,
    'weight': 9.5,
    'age': 2,
    'photo': '(-o.o-)__',
}

mouse = {
    'name': 'Johnny Boy',
    'age': 5,
    'weight': 1.5,
    'hungry': False,
    'photo': '<:3 )~~~~'
}

pets = [cat, mouse]

print ('Hello ' + cat['name'] + ' and ' + mouse['name'])
print (cat['photo'])
print (mouse['photo'])
                                
def feed(pet):
 if pets['hungry'] == True:
    pets['hungry'] = False
    pets['weight'] = pets['weight'] + 1
 else:
    print ('The Pypet is not hungry!')

for pets in pets:
    feed(pets)
    print (pets)
    
