#1---Berilgan ro'yxatdan juft sonni topuvchi dastur-----
# sonlar = [4, 31, 13, 11, 7] 
# juft_sonlar = []
# for son in sonlar:   
#     if son %2 ==0:
        
#         juft_sonlar.append(son/2)
        
# if len(juft_sonlar)==0:   20
#     print("Bu ro'yxatda juft son yo'q")
# else:
#     print(juft_sonlar)


#2------Foydalanuvchi kiritgan sonning kvadrati va kubini 
#   konsolga chiqaruvchi dastur -------------
# son = int(input("Sonni kiriting : "))
# a = son**2
# b = son**3
# print(f"Soz kiritgan son {son} uning kvadrati {a},kubi esa {b} ga teng")



#3-------Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, 
#  konsolga chiqaruvchi dastur -------------------------

# t_yil = int(input("Tug'ilgan yilingizni kiriting : "))
# yosh = 2026 - t_yil
# print(f"Siz {yosh} yoshdasiz")


#4-----Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning 
#yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur---------

# x=int(input("Birinchi sonni kiriting : >>>"))
# y=int(input("Ikkinchi sonni kiriting : >>>"))
# if y == 0:
#     print("0 ga bolish mumkinmas")
# else:
#     print(f"{x}-{y}={x-y}")
#     print(f"{x}+{y}={x+y}")
#     print(f"{x}*{y}={x*y}")
#     print(f"{x}/{y}={x/y}")


#-------------- TAKRORLASH --------------
sonlar = [13,111,3,1,11]
juft_sonlar=[]
for son in sonlar:
    if son%2==0:
        juft_sonlar.append(son)
        print(juft_sonlar)
    
else:
 print("no")#tok o'chdi

        





























