import json

kitoblar = [
    {"nomi": "Python dasturlash", "muallif": "Guido"},
    {"nomi": "Clean Code", "muallif": "Robert Martin  joncha"}
]

with open('kitoblar.json','w') as file:
    json.dump(kitoblar,file)
print('Saqlandi')
    
#for kitob in 