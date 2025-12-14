# def mijoz_info(ism, familiya, tyil, tjoy, email='',tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz = {'ism':ism,
#              'familiya':familiya,
#              'tyil':tyil,
#              'yoshi':2020-tyil,
#              'tjoy':tjoy,
#              'email':email,
#              'telefon':tel}
#     return mijoz

# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar =[]
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob!='ha':
#         break

# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}," 
#           f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}")
    
# def kattasi(x,y,z):
#     max = x
#     if y>max:
#         max=y
#     if z>max:
#         max = z
#     return max
        
# kattasi(3, 7, 1)

# def uch_son_kixhigi(a, b, c):
#     min = c
#     if b<min:
#         min = b
#     if a<min:
#         min =a
        
#     return min
# uch_son_kixhigi(22, -5, 10)


# def aylana_info(radius):
#     aylana = {
#         'diametr':2*radius,
#         'uzunlik':2*3.14*radius,
#         'yuza':3.14*radius**2
#         }
#     return aylana
# aylana_info(2)

# savol: Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing 
#(tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat
# sonlar)


  
# def tub_sonlar_top(min, max): #Funksiya yaratildi, min va max argument oladi.
#     """Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya"""
#     tub_sonlar = [] # Bo‘sh ro‘yxat, keyinchalik tub sonlar shu yerga qo‘shiladi.
    
#     n = min  # Hisoblashni eng kichik sondan boshlaymiz.
    
#     while n <= max: #n maksimal qiymatga yetguncha tsikl davom etadi.
#         if n > 1:  # 1 tub son emas, 2 dan boshlab tekshiramiz.
#             tub = True # Avval sonni tub deb faraz qilamiz, keyin tekshiramiz.
#             x = 2  # Bo‘luvchini 2 dan boshlab tekshiramiz (1 ga bo‘lishning foydasi yo‘q).
#             while x < n: #x n dan kichik bo‘lguncha bo‘lishni tekshiramiz.
#                 if n % x == 0:# Agar qoldiqsiz bo‘linsa — bu tub emas.
#                     tub = False #  Agar bo‘linsa, son tub emas deb belgilaymiz.
#                     break  #Bo‘linib qolganda ortiqcha tekshirishning hojati yo‘q, 
#                     #tsikldan chiqamiz.
#                 x += 1 # Har gal x ni bitta oshirib boramiz.
#             if tub: #Agar tub hali ham True bo‘lsa, demak son tub.
#                 tub_sonlar.append(n) #Tub sonni ro‘yxatga qo‘shamiz.
#         n += 1 #n ni 1 ga oshiramiz → keyingi sonni tekshirish uchun.

#     return tub_sonlar  #Barcha tub sonlardan iborat ro‘yxatni qaytaramiz.

# # Tekshirish
# print(tub_sonlar_top(1, 20))  #1 dan 20 gacha bo‘lgan tub sonlarni chiqaradi.


# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     n = min
#     while n <= max:
#         if n > 1:
#             tub = True
#             x = 2
#             while x < n:
#                 if n % x == 0:
#                     tub = False
#                     break
#                 x += 1
#             if tub:
#                 tub_sonlar.append(n)
#         n += 1
#     return tub_sonlar

# print(tub_sonlar_top(1, 100))

# def bahola(ismlar):
#     baholar = {}
#     while ismlar: 
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting :")
#         baholar[ism]= int(baho)
#     return baholar
# talabalar = ['ali','vali','salim','hakim']
# baholar = bahola(talabalar)
# print(baholar)


# def summa(a,b):
#     return a+b

# res = summa(5, 6)
# print(res)



# nums1 = [4,8,1,10]

# min = nums1[0]
# for el in nums1:
#     if el<min:
#         min = el

# print(min)


#yuqoridagini funksiya orqali yozish 
def minimal(l):
    min_number = nums1[0]
    for el in nums1:
        if el< min_number:
            min_number = el
            
    return min_number
    
nums1 = [-3,25,2.2,2.25]
minimal(nums1)
































    
    