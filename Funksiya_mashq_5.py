# =========== FUNKSIYADAN ODDIY QIYMAT QAYTARISH ===============
# def salom_ber(ism,familiya):
#     return f"Salom,{ism} {familiya}"

# a=salom_ber("Ali","Aliyev")
# print(a)

# ================== IXTIYORIY ARGUMENTLAR =================
# def ism_familiya(ism,familiya,otasi =''):
#     return f"{ism} {familiya} {otasi}"

# talaba1 = ism_familiya('Ali', 'Salimov')
# talaba2 = ism_familiya('Salim', 'Hamroyev','Eshmatovich')
# print(talaba1)
# print(talaba2)

# ========== FUNKSIYADAN LUG'AT QAYTARISH =====================

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto={'kompaniya':kompaniya, # 'kompaniya':'GM',
#             'model':model,         # 'model': 'Malibu',
#             'rang':rangi,          # 'rang' = 'Qora',
#             'korobka':korobka,     # 'karobka' = 'Avtomat',
#             'yil':yili,            # 'yil' = 2018, 
#             'narh':narhi }         #  'narh' = None
#     return avto

# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)

# print("Onlayn bozordagi mashinalar:")
# avtolar = [avto1,avto2]
# for avto in avtolar:
#     if avto['narh']:
#         narh =  avto['narh']
#     else:
#         narh = "No'malum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

# ============== FUNKSIYADAN RO'YXAT QAYTARISH ================  

# def oraliq(min,max):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min+=1
#     return sonlar
# n=oraliq(1, 11)
# print(n)

# ===========yuqoridagi funksiyani qadam tashlab hisoblaymiz ===========
# def oraliq(min,max,qadam):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min+=qadam
#     return sonlar
# n=oraliq(1, 11,2)
# print(n)

# ================= AMALIYOT ==========================

def mijoz_info(ism, familiya, tyil, tjoy, email='',tel=None):
    """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    mijoz = {'ism':ism,
             'familiya':familiya,
             'tyil':tyil,
             'yoshi':2020-tyil,
             'tjoy':tjoy,
             'email':email,
             'telefon':tel}
    return mijoz
n = mijoz_info('ali', 'salimov', 1988, 'buxoro')
print(n)
    









  


    
