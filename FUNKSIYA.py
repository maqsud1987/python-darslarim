# def programmer(word):
#     print("> " + word)
# programmer("Hello")
# programmer("How are you")
# programmer("Bye")

# def yigindi(a,b):
#     print(a+b)
# yigindi(3, 4)
# yigindi(10, 20)


# def max(a,b):
#     if a>b:
#         return a
#     else:
#         return b

# # r = max(10,20)
# # print(r)

# print(max(10, 20))



# def salom_ber(ism):
#     print(f"Salom {ism.title()}")
# salom_ber("ali")




# def toliq_ism(ism,familiya):
#     print(f"Foydalunvchi ismi : {ism.title()}\n"
#           f"Foydalabuvchi familiyasi : {familiya.title()}")
# toliq_ism('valijon', 'shamshiyev')


# def toliq_ism_yasa(ism,familiya):
#    return f"{ism.title()} {familiya.title()}"
   
# talaba = toliq_ism_yasa('olim','salimov')
# print(talaba)




# def toliq_ism_yasa(ism,familiya):
#     return f"{ism.title()} {familiya.title()}"

# talaba1 = toliq_ism_yasa('ali', 'shamshiyev')
# talaba2 = toliq_ism_yasa('vali', 'shamshiyev')

# print(f" Bugun darsga {talaba1} umuman kelmadi,lekin {talaba2} yaxshi qatnashdi.")



# def toliq_ism_yasa(ism,familiya,otasining_ismi =''):
#     """To'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {familiya} {otasining_ismi}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()


# talaba1 = toliq_ism_yasa('ali','eshmatovich','salimov')
# talaba2 = toliq_ism_yasa('ali','salimov')

# print(f"A'lochi o'quvchi {talaba1},ikkichisi esa {talaba2}")



# def avto_info(kompaniya,model,rangi,karobka,yili,narhi = None):
#    return {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'karobka':karobka,
#             'yili':yili,
#             'narh':narhi
#                         }
   

# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1,avto2]

# print("Onlayn bozordagi avtomoshinalar :")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#         print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")
#     else:
#         narh = 'nomalum'
#         print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")


# def avto_info(kompaniya,model,rangi,karobka,yili,narhi = None):
#     return { 'kompaniya':kompaniya,
#              'model':model,
#              'rang':rangi,
#              'karobka':karobka,
#              'yili':yili,
#              'narh':narhi}

# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2025)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)

# avtolar = [avto1, avto2]

# print("Onlayn bozordagi avtomoshinalar :")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#         print(f"{avto['rang']} {avto['model']} {avto['kompaniya']} narxi: {avto['narh']} ")
#     else:
#         narh = 'nomalum'
#         print(f"{avto['rang']} {avto['model']} narxi: {avto['narh']}")


def kitob_info(nomi, muallif, yil, narh=None):
    return {'nomi': nomi,
            'muallif': muallif,
            'yil': yil,
            'narh': narh
            }

# kitob1 = kitob_info('otgan kunlar', 'abdulla qodiriy', 1986)
# kitob2 = kitob_info('ikki eshik orasi', 'xudoyberdi toxtaboyev', 1992, 25000)

# kutubxona = [kitob1, kitob2]

# print("Kutubxonadagi kitoblar:")
# for kitob in kutubxona:
#     if kitob['narh']:
        
#         narh = kitob['narh']
#         print(f"Kitob nomi: {kitob['nomi'].capitalize()}. Muallif: {kitob['muallif'].title()}. Narhi: {kitob['narh']}")
#     else:
#         narh = 'nomalum'
#         print(f"Kitob nomi: {kitob['nomi'].capitalize()}. Muallif: {kitob['muallif'].title()}. Narhi: {kitob['narh']}")



# def oraliq(min,max):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# print(oraliq(0,10))
# print(oraliq(10,21))



def oraliq(min,max,qadam):
    sonlar = []
    while min<max:
        sonlar.append(min)
        min += qadam
    return sonlar
print(oraliq(0, 10, 2))
print(oraliq(10, 20, 3))



# def avto_info(kompaniya,model,rangi,karobka,yili,narhi = None):
    
#     return { 'kompaniya':kompaniya,
#              'model':model,
#              'rang':rangi,
#              'karobka':karobka,
#              'yili':yili,
#              'narh':narhi}

# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz. ")
# avtolar = [] #salondagi avtolar uchun bo'sh ro'yxat
# while True:  #tsikl yaratmoqchimiz
#     print("\nQuyidagi malumotlarni kiriting :",end=" ")
#     kompaniya  = input("Ishlab chiqaruvchi :")
#     model = input("Modeli : ")
#     rangi = input("rangi : ")
#     karobka = input("karobka : ")
#     yili = input("ishlab chiqarilgan yili : ")
#     narhi = input("narhi : ")
    
    
#     avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili,narhi))
    
#     javob = input("Yana avto qo'shasizmi ?  (yes/no): ")
#     if javob == 'no':
#         break
# print("\nSalonimizdagi avtolar :")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "nomalum"
#     print(f"{avto['model'].title()} {avto['rang'].title()}  narxi: {avto['narh']}")


def mijoz_info(ism, familiya, tyil, tjoy, email='',tel=None):
    """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    return{'ism':ism,
             'familiya':familiya,
             'tyil':tyil,
             'yoshi':2020-tyil,
             'tjoy':tjoy,
             'email':email,
             'telefon':tel}



print("Mijoz haqida ma'lumotlarni kiriting.")

mijozlar =[]

while True:
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    tyil = int(input("Tug'ilgan yili: "))
    tjoy = input("Tug'ilgan joyi: ")
    email = input("Email: ")
    telefon = input("Telefon raqami: ")
    
    mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
    
    javob = input("Davom etasizmi? (ha/yo'q)")
    
    
    
    if javob!='ha':
        break

print("Mijozlar:")
for mijoz in mijozlar:
    print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}," 
          f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}")









    










    
        
    
    
    

        
        



        
        
    



































    