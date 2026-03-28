#=====Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaring=====
# def kopaytma(*sonlar):
#     natija=1
#     for son in sonlar:
#         natija*=son
#     return natija
# print(kopaytma(15,20,10,1))

#====Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funksiya

# def talaba_info(ism,familiya,**maljumotlar):
#     maljumotlar['ismi']=ism
#     maljumotlar['familiyasi']=familiya
#     return maljumotlar
# print(talaba_info("Ali", "Salimov",t_joy="Buxoro",t_yil=1999))

import random as r
son = r.randint(1,5)
print(son)