# def kattasini_top(x,y,z):
#     """Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya """
#     eng_katta=x 
#     if y>x:
#         eng_katta=y 
#     if z>eng_katta:
#         eng_katta=z 
        
#     return eng_katta

# kattasini_top(6, -10, 78)

#IKKINCHI VARIANT
# def kattasi(x,y,z):
#     max = x
#     if y>=max:
#         max = y
#     if z>=max:
#         max = z
#     return max

# kattasi(10,20,-5)


        
# def aylana_info(radius):
#     """Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini,
#     diametrini, uzunligi va yuzini lug'at ko'rinishida qaytaruvchi funksiya"""
#     diametr = 2*radius
#     uzunligi = 2*3.14*radius
#     yuzi = 3.14*radius**2
    
#     info = {
#         'diametr':diametr,
#         'uzunlik':uzunligi,
#         'yuza':yuzi
#         }
#     return info

# natija = aylana_info(5)
# print(natija)


# def tub_sonlar(min,max):  
#     """Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya"""
#     tub_sonlar=[] # bo'sh list
#     n = min 
#     while n<=max:
#         if n>1:
#             tub =True
#             x = 2
#             while x<n:
#                 if n%x==0:
#                     tub = False
#                     break
#                 x +=1
#             if tub:
#                 tub_sonlar.append(n)
#         n +=1
#     return tub_sonlar
# print(tub_sonlar(1, 1000))

#---------- YUQORIDAGI KODNI IZOHLI YOZDIK------------

# def tub_sonlar(min, max):  
#     # Berilgan oraliqdagi (min dan max gacha) tub sonlarni topuvchi funksiya

#     tub_sonlar = []  
#     # Topilgan tub sonlarni saqlash uchun bo‘sh ro‘yxat (savat)

#     n = min  
#     # Tekshiruvni boshlash uchun n ga eng kichik sonni beramiz

#     while n <= max:
#         # n soni min dan max gacha ketma-ket tekshiriladi

#         if n > 1:
#             # 1 tub son emas, faqat 2 va undan katta sonlarni tekshiramiz

#             tub = True  
#             # Dastlab n sonini tub deb hisoblaymiz

#             x = 2  
#             # Bo‘luvchini 2 dan boshlaymiz (1 har doim bo‘ladi, kerak emas)

#             while x < n:
#                 # 2 dan n-1 gacha bo‘lgan bo‘luvchilarni tekshiramiz

#                 if n % x == 0:
#                     # Agar n soni x ga qoldiqsiz bo‘linsa

#                     tub = False  
#                     # Demak, bu son tub emas

#                     break  
#                     # Endi boshqa bo‘luvchini tekshirish shart emas

#                 x += 1  
#                 # Keyingi bo‘luvchiga o‘tamiz (2 → 3 → 4 → ...)

#             if tub:
#                 # Agar n hech qaysi songa bo‘linmagan bo‘lsa

#                 tub_sonlar.append(n)
#                 # n soni tub, uni ro‘yxatga qo‘shamiz

#         n += 1  
#         # Keyingi songa o‘tamiz (1 → 2 → 3 → ...)

#     return tub_sonlar  
#     # Barcha topilgan tub sonlar ro‘yxatini qaytaramiz


# print(tub_sonlar(1, 1000))
# # 1 dan 1000 gacha bo‘lgan barcha tub sonlarni ekranga chiqaradi



#------Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya----
# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)        
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar

# print(fibonacci(10))


#-------RO'YXATNI LUG'ATGA UZATUVCHI FUNKSIYA-------
# def bahola(ismlar):
#     baholar = {} 
#     while ismlar:
#         ism = ismlar.pop()  
#         baho = input(f"Talaba {ism.title()}ning bahosini qo'ying:  ")
#         baholar[ism]=int(baho)
#     return baholar

# talabalar = ['ali','vali','salim','halim']
# baholar = bahola(talabalar)
# print(baholar)
        
def katta_harf(matnlar):
    
    matn = input("Matnni kiriting: ")
    
    





                
            
        
            
        
        
        
    
    

   

    

       

        
    
    
        




    
    




































