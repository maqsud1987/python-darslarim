# akam  = {'ism':'umid','yosh': 41,'manzil':'buxoro'}
# print(f"Akam ismi {akam['ism'].title()},yoshi {akam['yosh']} da,"
#       f"turar joyi {akam['manzil'].title()}" )

# taomlar = {
#     'ali':'osh',
#     'vali':'shashlik',
#     'hasan':"lag'mon",
#     'husan':"mastava",
#     'olim':"somsa"
#     }
#taom = taomlar['ali']
#print(f"Alining sevimli taomi {taom}")

# python_izohli_lugati = {
#     'integer':"Butun son",
#     'float':"O'nlik son",
#     'string':"Matn",
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas ro'yxat"}
# soz  = input("Soz kiriting>>>")
# print(python_izohli_lugati.get(soz, "Bunday so'z lug'atda yo'q!"))

# python_izohli_lugati = {
#     'integer':"Butun son",
#     'float':"O'nlik son",
#     'string':"Matn",
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas ro'yxat"
# }

# soz = input("Soz kiriting>>>")
# print(python_izohli_lugati.get(soz, "Bunday so'z lug'atda yo'q!"))

# lugat = {
#     'apple': "olma",
#     'car': "mashina",
#     'book': "kitob",
#     # va hokazo
# }

# soz = input("So'z kiriting: ")
# print(lugat.get(soz, "Bunday so'z lug'atda yo'q!"))

# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }
# #print(talaba_0.items())
# for key,value in talaba_0.items():
#     print(f"kalit: {key.title()}")
#     print(f"qiymat: {value}\n")

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }
# for k,q in telefonlar.items():
#     print(f" {k.title()}ning telefoni {q}\n ")

# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }

#print(mahsulotlar.keys())

# print("Do'kondagi mahsulotlar :\n")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())



# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} - do'konimizda bor {mahsulotlar[mahsulot]} so'm")
#     else:
#         print(f"{mahsulot.title()}ni ham olib yaqinda olib kelamiz")
#     print()


# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

#python_words = {
#     'integer':'Butun son',
#     'float': "O'nlik son",
#     'boolean':"Mantiqiy qiymat",
#     'for':"Biror amalni qayta-qayta bajarish tsikli",
#     'if':'Shartlarni tekshirish operatori'}

# for key,value in sorted(python_words.items()):
#         print(f"{key.title()}-{value}")

# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'}
# # print("Davlatlar :")
# # for davlat in sorted(davlatlar.keys()):
# #     print(f"{davlat.upper()} ")
    
# # print("\nPoytaxtlari:")    
# # for poytaxt in sorted(davlatlar.values()):
# #     print(f"{poytaxt.title()}")

# davlat = input("Istalgan davlatingizni kiriting:").lower()
# poytaxt = davlatlar.get(davlat,"Bizning ro'yxatda bunday davlat yo'q")
# print(poytaxt)

# menu = {
#         'osh':20000,
#         "lag'mon":22000,
#         'non':4000,
#         'choy':5000,
#         'shashlik':12000,
#         'somsa':6000,
#         'tabaka':15000
#         }
# print("Ucta taom kiriting : ")
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1} - taom>>>"))
#     print(buyurtmalar)
# narsa = buyurtmalar.get(f"{n}, bizda yo'q")
# print(narsa)

# menu = {
#     'osh': 20000,
#     "lag'mon": 22000,
#     'non': 4000,
#     'choy': 5000,
#     'somsa': 6000,
#     'tabaka': 30000
# }

# print("Uchta taomni kiriting 👇")
# buyurtmalar = []

# for n in range(3): # 3 marta takrorlanuvchi tsikl yaratildi
#     taom = input(f"{n+1}-taom: ") # Har safar foydalanuvchidan taom nomi so‘raladi.
#     buyurtmalar.append(taom)  # kiritilgan taomlar buyurtmalarga qo'shiladi

# print("\nSizning buyurtmangiz:")
# for taom in buyurtmalar: # buyurtma qilingan har bir taom uchun
#     print(f"{taom.title()} — {menu.get(taom, 'bizda yo‘q')}") # bo'sa katta harf bilan chiqadi,bo'lmasa aksincha






    












































    
    


    











































