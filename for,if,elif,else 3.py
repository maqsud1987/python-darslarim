# mahsulotlar = ['ruchka','kitob','olma','nok','qalam','non','piyoz','choy','un','suv']
# savat = []
# print("5 ta mahsulotmi kiriting: ")
# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulotni kiriting : ").lower())
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print("Mahsulot do'konimizda bor")
#     else:
#         print("Mahsulot do'konimizda yo'q")  
    



# mahsulotlar = ['ruchka','kitob','olma','nok','qalam','non','piyoz','choy','un','suv']
# bor_mahsulotlar = []
# mavjud_emas = []

# print("5 ta mahsulotmi kiriting: ")
# for n in range(5):
#     mahsulot = input(f"{n+1}-mahsulotni kiriting : ").lower()
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# print(f"Do'konimizda bor mahsulotlar-{bor_mahsulotlar}")
# print(f"Bular {mavjud_emas} yo'q")       



# foydalanuvchilar = ['Salim','Olim','Halim','Nozim','Karim']
# login = input("login kiriting : >>>").title()
# if login in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
    
# else:
#     print("Xush kelibsiz, foydalanuvchi!")
    


# son = int(input("Butun son kiriting: >>>")) 
# for n in range(2,11):
#     if son%n==0:
#         print(f"Siz kiritgan son {son} bu son 10 gacha sonlardan {n} ga bo'linadi")



#------- Amalkiyot:berilgan koddan xatolikni topish --------
#1

# son = int(input("Juft son kiriting: "))
# if son%2==0:
#     print("Rahmat!")
# else:
#     print("Bu son juft emas")


#2

# yosh = int(input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0
# elif 4<yosh <= 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")


#3

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")


#4

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []

# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: ").lower())


# for mahsulot in savat:
#      if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#      else:
#         print(f"Do'konimizda {mahsulot} yo'q")
 
# print("Savatingiz bo'sh")   


#5

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qoshing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print("Do'konimizda quyidagi mahsulotlar yo'q:")
for mahsulot in mavjud_emas:
  print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    




















      

   


    







 














    