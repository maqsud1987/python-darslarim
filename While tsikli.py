# son = 1
# while son <=5:
#     print(son, end= ' ')
#     son +=1
# print("Dastur to'xtadi")


#  while end input

# print("Ixtiyoriy sonning kvadratini qaytaruvchi dastur")

# savol = "Istalgan sonni kiriting"
# savol += "(agar 'exit' deb kiritsangiz dastur tugaydi) : "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
        
# print("Dasttur to'xtadi")





# print("Ixtiyoriy so'zni bosh harflarga o'tkazib beruvchi dastur")

# savol = " Ixtiyoriy so'z kiriting"
# savol += "(agar 'stop' deb yozsangiz dastur to'xtaydi) : "
# qiymat = ' '
# while qiymat != 'stop':
#     qiymat = input(savol)
#     if qiymat != 'stop':
#         print(qiymat.upper())
        
# print("Dastur to'xtadi")



# print("Ismni qaytaruvchi dastur")

# savol = "Ismingizni kiriting "
# savol += "(agar 'bekor' deb yozsangiz dastur to'xtaydi): "
# qiymat = ' '
# while qiymat != 'bekor':
#     qiymat = input(savol)
#     qiymat != 'bekor'
#     print(f"Salom {qiymat.title()}")
    
# print("Dastur to'xtadi")



# ishora.

# print("Ixtiyoriy sonning kvadratini qaytaruvchi dastur")

# savol = "Istalgan sonni kiriting"
# savol += "(agar 'exit' deb kiritsangiz dastur tugaydi) : "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)

# print("Dastur to'xtadi")






# print("Kiritilgan so'z uzunligini ko'rsatuvchi dastur")

# savol = "Istalgan so'zni kiriting"
# savol += "(agar 'exit' deb kiritsangiz dastur tugaydi) : "

# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else: 
#         print(f"Siz kiritgan so'z '{qiymat.upper()}' uning uzunligi {len(qiymat)}")




# break while
   
#print("Istalgan so'zni kvadratini qaytaruvchi dastur")
    
# savol = "Istalgan sonni kiriting"
# savol += "(agar 'exit' deb kiritsangiz dastur tugaydi) : "

# while True:  #abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)
# print("Dastur to'xtadi")



# break  for

# sonlar = list(range(1,11)) # 1 dan 11 gacha sonlar ro'yxatini oldik
# for son in sonlar: # shu sonlar ichidagi har bir son uchun davom etadi
#     if son == 5: # son 5 ga teng bo'lganda 
#         break  # dastur to'xtaydi
#     print(f"{son} ning kvadrati {son**2} ga teng ") # 1,2,3,4 uchun ishlaydi
# print("Dastur to'xtadi")  # break bo'lganda ishlaydi
    
    
    
# CONTINUE  tsikl ichida bir qadam tashlab o'tadi

# print("Sonning kvadratini qaytaruvchi dastur")
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue  # 5 ni o'tkazib yuboradi
#     print(f"Siz kiritgan {son} ga teng, uning kvadrati {son**2} ga teng")

# print("Dastur to'xtadi")


# CONTINUE while

# son = 1 #Dastur boshida son degan o‘zgaruvchi 0 deb olinadi
# while son < 10: # “Agar son 10 dan kichik bo‘lsa, quyidagilarni qilaver” degani.
#     son += 1  # Har safar sonni 1 ga oshiradi (0 → 1 → 2 → 3 ...).
#     if son %2 !=0:  #“Agar son toq bo‘lsa” (masalan, 1, 3, 5 ...).
    
#         continue #“Toq bo‘lsa, pastdagini o‘tkazib yubor, boshidan boshlayver” degani.
#     else:  # “Agar toq bo‘lmasa (ya’ni juft bo‘lsa)” degani.
#         print(son, end=' ')  #Juft sonni ekranga chiqaradi.


#Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang.
# Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating


# kitoblar = [] 
# savol = "Sevimli kitobingizni kiriting (agar 'stop' deb yozsangiz dastur to'xtaydi): "

# while True:
#     qiymat = input(savol)
#     if qiymat.lower() == 'stop':
#         break
#     kitoblar.append(qiymat)

# print("\nSizning sevimli kitoblaringiz:")
# for kitob in kitoblar:
#     print(kitob,end=' ')


# savol = "Yoshingizni kiriting : "
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh  = int(qiymat)
    
#     if yosh <= 7:
#         narh = 2000
        
#     elif 7<yosh<18:
#         narh = 3000  
        
#     elif 18<yosh<65:
#         narh = 10000
    
#     else:
#         narh = 0
        
#     if narh == 0:
#         print("Sizga kirish bepul")
        
#     else:
             
#         print(f" Sizga kirish {narh} so'm")


# savol = "Haroratni kiriting : "
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     harorat  = int(qiymat)
    
#     if harorat<=0:
#         holat = 'Havo juda sovuq'
        
#     elif 0<=harorat<=20:
#         holat = 'Havo salqin'
        
#     elif 20<=harorat<=35:
#         holat = 'Havo iliq'
        
#     else:
#         holat = 'Havo juda issiq'
#     print(f"Bugungi havo {holat}")





    
        
   
  
        







   
   
    
    

    
    




































    
    