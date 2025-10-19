#   Lug'atlar bilan ishlash

#cars_0 = {'model':'ferrari','rang':'qizil'}
# print(cars_0['model'])
# print(cars_0['rang'])

#en_uz = {'apple':'olma',"phonr":"telefon",'book':'kitob'}
# print(en_uz['apple'])

#mevalar ={'olma' :1000,'telefon':10000,'kitob':5000}
#print(f" olma {mevalar['olma']} som")

#talaba = {'ism':'eshmat','familiya':'toshmatov','yosh':23}
# 
# yangi kalit so'z qo'shish 

# talaba['kurs'] = 4
# talaba['fakultet'] = "AKT"
# print(talaba)

# talaba_1  = {}
# talaba_1['ism']='Ibodullo'
# talaba_1['familiya']='Ibodullayev'
# talaba_1['kurs']=4
# talaba_1['yosh']= 24

# print(talaba_1)

#  .get - lug‘atdan kalit orqali qiymatni olish uchun ishlatiladi
# telefonlar  = {
#     'Ali':'redmi',
#     'Vali':'samsung',
#     'Salim':'nokia',
#     'Halim':'fly'
    
#     }

# print(telefonlar.get('Hasan','Bunday ism yoq'))

# otam = {'ism':'Ali','t_yil':1960,'manzil':'Toshkent'}
# akam = {'ism':'Zohid','t_yil':1981,'manzil':'Toshkent'}
# print(f"Mening otam {otam['ism']},{otam['t_yil']} - yil,{otam['manzil']}da tug'olgan")

# taom = {'otam':'osh',"akam":'manti','singlim':'chuchvara'}
# print(f"Mening dadamning ismi {otam['ism']},ular {taom['otam']}ni yaxshi ko'radilar ")

# lugat = {
#     'float':'onli son',
#     'integer':'butun son',
#     'string':'matn',
#     'if':'agar',
#     'else':'aks holda',
#     'print':'chop etish'
#     }

# soz = input("Biron soz kiriting :")
# #for n  in soz:
# if soz in lugat:
        
#      print(lugat[soz])
# else:
#     print("Bunday so'z bu ligatta yo'q")

lugat = {
    'float':'onli son',
    'integer':'butun son',
    'string':'matn',
    'if':'agar',
    'else':'aks holda',
    'print':'chop etish'
    }

soz = input("Biron soz kiriting :")
print(lugat.get(soz,"Bunday soz mavjud emas"))
    


    


    


    





























































    







































