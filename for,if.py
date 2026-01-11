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
#1
# sonlar = [13,21,13,2221,111,3,131,11]
# juft_sonlar=[]
# for son in sonlar:
#     if son%2==0:
#         juft_sonlar.append(son*2)
        
# if len(juft_sonlar)==0:
#    print("Bu ro'yxatda juft son yo'q")
# else:
#     print(f"Bu ro'yxatda {juft_sonlar} juf ")
   
#2
# son = int(input("Sonni kiriting: >>>"))
# print(f"Siz kiritgan son {son},uning kvadrati {son**2},kubi esa {son**3} ga teng ")

        
#3
# yosh = int(input("Yoshingizni kiriting : "))
# t_yil = 2026 - yosh
# print(f"Siz {t_yil}-yilda tug'ilgansiz")   


#4
# son_1 = int(input("Birinchi sonni kiriting: "))        
# son_2 = int(input("Ikkinchi sonni kiriting: "))
# if son_2 ==0:
#         print(" 0 ga bo'lish mumkin emas ")
# else:
#         print(f"{son_1} + {son_2} = {son_1+son_2}")
#         print(f"{son_1} - {son_2} = {son_1-son_2}")
#         print(f"{son_1} . {son_2} = {son_1*son_2}")
#         print(f"{son_1} : {son_2} = {son_1/son_2}")

# davlatlar = ['aqsh','turkmaniston','rossiya','angliya','xitoy']

# son = list(range(120,1200,2))
# print(son[0:10])

# taomlar = ['osh','manti','somsa','shurchoy','dimlama']
# nonushta = taomlar[:]

# del nonushta[:3]
# del nonushta [-1]
# nonushta.append('sut')
# nonushta.append('sir')
# print(taomlar)
# print(nonushta)


# ismlar = ['ali','vali','salim','karim','olim']
# for ism in ismlar:
#     print(f"Salom {ism.title()} qlaysan")
    
#     print(f"Kod {len(ismlar)} marta takrorlandi")



# toq_sonlar = list(range(11,100,2,))
# for son in toq_sonlar:
#     print(f"{son}**3= {son**3}")


# s_kinolar = []
# for n in range(5):
#     s_kinolar.append(input(f"{n+1} - kinongizni kiriting: "))
       
# print(s_kinolar)



# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())


# ism = input("Ismingizni kiriting : ")
# if ism.lower() =='admin':
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz {ism.title()}")



# x = int(input("Birinchi sonni kiriting: "))
# y = int(input("Ikkinchi sonni kiriting: "))
# if x>y:
#     print("Birinchi son katta")
    
# elif x<y:
        
#     print("Ikkinchi son katta")
        
# else:
#     print("Ikkala son teng")




























