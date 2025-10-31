# .items()  - lug'at ichidagi barcha kalit-qiymat juftliklarini ko'rishimiz mumkin.

# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }
# #print(talaba_0.items()) #items()—lug‘atdagi kalit (key) va qiymat (value) juftliklarini birgalikda olish 
# for kalit,qiymat in talaba_0.items():
#         print(f"kalit : {kalit}")
#         print(f"Qiymat: {qiymat} \n")   

# birliklar = {
#     'kuch,f':'n',
#     'ish,a': 'j',
#     'quvvat,n':'w',
#     'vaqt,t':'s'
#     }

# for key,value in birliklar.items():
#     print(f"Nomi,Belgilanishi - {key.upper()}")
#     print(f"Birligi - {value.title()}\n")
    
# lug'atdagi kalit so'zlarni ko'rish talab qilinsa, .keys() metodidan foydalanishimiz mumkin.

# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }
# bozorlik = ['anor','uzum','baliq','piyoz','anjir']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#          print(f"{mahsulot.title()} {mahsulotlar[mahsulot]}")  #bu ifoda kalit orqali qiymatni olish degani

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos {buyum}ni ham olib keling")

# lug'atdagi qiymatlarni chiqarish talab qilinsa .values() metodidan foydalanishimiz mumkin.

#Amaliyot
# lugat = {
#     'pen':'ruchka',
#     'jump':'sakramoq',
#     'if':'agar',
#     'for':'ucun',
#     'room':'xona'
#     }
# for soz in sorted(lugat):
#     print(f"{soz.title()} - {lugat[soz]}")
    

#Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, 
#keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}
# for davlat in sorted(davlatlar):
#     print(f"Davlat :{davlat.title()}")
#     print(f"Poytaxt:{davlatlar[davlat].title()}\n")

davlat = input("Istalgan davlatingizni kiriting >>>")
if davlat in davlatlar:
    print(f"Siz kiritgan davlat {davlat.title()} uning poytaxti {davlatlar[davlat].title()}")
else:
    print(f"Siz kiritgan davlat {davlat.title()} bo'yicha ma'lumot bizda yo'q")



























































