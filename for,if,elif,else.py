#----Foydalanuvchidan istalgan son kiritishni so'rang. 
#----Agar son manfiy bo'lsa konsolga "Manfiy son", 
#----agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. ---#

# son  = int(input("Sonni kiriting: "))

#--- variant_1 NATIJA OLISH -----
# if son<0:
#     print("Son manfiy")
# else:
#     print("Son musbat")
    
#--- variant_2 NATIJA OLISH -----
#print("Son manfiy") if son<0 else print("Son musbat")




# #sonning ildizini chiqaruvchi dastur
# son  = float(input("Sonni kiriting: "))
# print(son**(0.5)) if son > 0 else print("Bu son manfiy")


    
#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi 
#juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" 
#degan xabarni chiqaring.

# son = int(input("Juft sonni kiriting : "))
# print("Bu juft son") if son%2 ==0  else  print("Bu toq son")



#Foydalanuvchi yoshini so'rab,muzeyga kirish uchun chipta narhini hisoblovchi dastur

# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <=0 or yosh>100:
#     print("Siz yoshingizni xato kiritdingiz,iltimos qayta kiriting")
# else:
#     if 0<yosh<=4 or yosh>60:
#         narh = 0

#     elif 4<yosh<18:
#         narh = 10000
        
#     elif 18<=yosh<60:
#         narh = 20000
        
#     print(f"Sizga kirish {narh} so'm")



#-------Foydalanuvchidan ikita son kiritishni so'rang, 
# sonlarni solishtiring va ularning teng yoki katta/kichikligi 
# haqida xabarni chiqaring ---------------------------#

# x = float(input("Birinchi sonni kiriting :"))
# y = float(input("Ikkinchi sonni kiriting :"))

# if x>y:
#     print(f"{x}>{y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}={y}")



mahsulotlar = ['ruchka','kitob','olma','nok','qalam','non','piyoz','choy','un','suv']
savat = []
print("5 ta mahsulotmi kiriting: ")
for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni kiriting : "))
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print("Mahsulot do'konimizda bor")
        else:
            print("Mahsulot do'konimizda yo'q")
    
    






















    