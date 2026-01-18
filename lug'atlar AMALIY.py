# dost = {'ism':'Eshmatov Toshmat','t_yil':1992,'manzil':'kogon'}
# print(f"Mening do'stim {dost['ism']},{dost['t_yil']}-yilda {dost['manzil'].title()}da tug'ilgan.")

# python_izohli_lugati = {
#     'if':'agar',
#     'for':'uchun',
#     'else':'aksholda',
#     'in':'ichida',
#     'string':'matn',
#     'integer':'son'
#     }

# soz = input("So'zni kiriting: ").lower()

# qiymat = python_izohli_lugati.get(soz,"Bu lug'atda bunday so'z yo'q")
# print(qiymat)

# #--- shu lkodni if,else yordamida yoki get() siz yozish --------
# soz = input("So'zni kiriting: ").lower()

# if soz in python_izohli_lugati:
#     print(f"{soz.title()} so'zining  ma'nosi - {python_izohli_lugati[soz]}")
# else:
#     print("Bu lug'atda bunday so'z yo'q")


#--KALIT VA QIYMATNI ALIFBO KETMA-KETLIGIDA CHIQARISH -----

# python_izohli_lugati = {
#     'if':'agar',
#     'for':'uchun',
#     'else':'aksholda',
#     'in':'ichida',
#     'string':'matn',
#     'integer':'son'
#     }
# print("Lug'at kaliti")
# for k in sorted(python_izohli_lugati.keys()):
#     print(k.title())
    
# print("Lug'at qiymati")    
# for v in sorted(python_izohli_lugati.values()):
#     print(v.title())


#---DAVLATLAR VA POYTAXTLARINI ALIFBO KETMA-KETLIGIDA CHIQARISH-----

# poytaxlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'  }
#             
# print("Davlatlar :")
# for k in sorted(poytaxlar.keys()):
#     print(k.title())
    
# print()
   
# print("Poytaxtlari:")    
# for v in sorted(poytaxlar.values()):
#     print(v.title())

#--agar davlat ham poytaxt ham birdaniga chiqarilsa ----

# for k,v in sorted(poytaxlar.items()):  
#     print(f"{k.title()} - {v.title()}")
    


#---ISTALGAN DAVLAT POYTAXTINI CHIQAROVCHI DASTUR -----

# poytaxlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'  }


# #-------- get orqali -------------------

# # savol  = input("Istalgan davlatni kiriting : >>>").lower()

# # poytaxt  = poytaxlar.get(savol,"Bunday davlat bizning ro'yxatda yo'q")
# # print(poytaxt)

# #--------- if va else orqali ------------


# savol  = input("Istalgan davlatni kiriting : >>>").lower()
# if savol in poytaxlar:
#     print(f"{savol.title()}ning poytaxti - {poytaxlar[savol].title()}")
# else:
#     print("Bunday davlat bizning ro'yxatda yo'q")


#--------=== RESTORAN  MENUSI LUG'ATI DASTURI ===-----------    

menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }

print(' 3 ta taomni kiriting: ')
for n in range(3):
    taom = input(f"{n+1} - taomni kiriting: >>>").lower()
    if taom in menu:
        print(f"{taom.title()} bor,narhi - {menu[taom]} so'm")
    else:
        print(f"Uzr,bizning menuda {taom.title()} yo'q")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
