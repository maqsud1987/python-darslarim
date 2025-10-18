# if-elif-else KETMA-KETLIGI (elif - aks holda,agar)
# yosh = int(input("Yoshingizni kiriting >>>"))
# if yosh<=4:
#     print("Sizga kirish bepul")
# elif yosh<=12:
#     print("Sizga kirish 5 000 so'm")
# elif yosh<=35:
#         print("Sizga kirish 5 000 so'm")
# else:print("Sizga kirish bepul ")

#Yuqoridagi kodda qayta-qayta print yozmaslik uchun >>>

# yosh = int(input("Yoshingizni kiriting >>>"))
# if yosh<=4:
#     narx = "bepul"
# elif yosh<=12:
#     narx = 5000
# elif yosh<=35:
#     narx = 10000
# else:
#     narx = "bepul"
# print(f"Sizga kirish {narx} so'm")

# kun = input("Bugun qaysi kun ?>>>")
# if kun.lower() == "shanba" or kun.lower()=="yakshanba": 
#     print("Bugun cho'milishga boramiz")
# else:
#     print("Bugun ish kuni")
    
# kun = input("Bugun qaysi kun ?>>>")
# harorat = float(input("Harorat qanday ?"))
# if kun.lower() == "yakshanba" and harorat >= 40: 
#     print("Bugun cho'milishga boramiz")
# elif kun.lower() == "yakshanba" and harorat < 40:
#     print("Uyda dam olamiz")

# kun = input("Bugun qaysi kun ?>>>")
# harorat = float(input("Harorat qanday ?"))

# if (kun.lower() == "shanba" or kun.lower() =="yakshanba") and harorat >= 40: 
#     print("Bugun cho'milishga boramiz")
# elif (kun.lower() == "shanba" or kun.lower() =="yakshanba") and harorat < 40:
#     print("Uyda dam olamiz")

# narx = 15000 #Boshlang'ich narx 15000 so‘m deb belgilanmoqda.
# choy = True  #choy bor (True), salat yo‘q (False).
# salat = False
# if choy and salat:      #Bu shart bajarilmaydi, chunki salat yo‘q.
#     narx = narx +10000  #Agar choy va salat ikkalasi ham bo‘lsa, narxga 10000 qo‘shiladi.
                    
# elif choy or salat: 
#     narx = narx + 5000 #Aks holda, agar choy yoki salat bo‘lsa, narxga 5000 qo‘shiladi.
# print(f"Jami {narx} so'm") #Bu shart bajariladi (choy bor), narx endi 20000 bo‘ladi.

# Agar shartni o'zgartirsak
# narx = 15000 #Boshlang'ich narx 15000 so‘m deb belgilanmoqda.
# choy = True  #choy bor (True), salat bor (True).
# salat = True
# if choy and salat:      #Bu shart bajariladi
#     narx = narx +10000  #Agar choy va salat ikkalasi ham bo‘lsa, narxga 10000 qo‘shiladi.
                    
# elif choy or salat: 
#     narx = narx + 5000 
# print(f"Jami {narx} so'm") 

# narh = 15000 # mijoz 15 so'mga ovqat oldi
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
# #Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
# if choy:
#     narh = narh +3000
#     print("Mijoz choy oldi")
# if salat:
#     narh = narh +5000
#     print("Mijoz salat oldi")
# if non:
#     narh = narh +2000
#     print("Mijoz non oldi")
# if kompot:
#     narh = narh +6000
#     print("Mijoz kompot oldi")
# if assorti:
#     narh = narh +10000
#     print("Mijoz assorti oldi")
# print(f"Jani {narh} so'm")
# in operatori yordamida biz ro'yxatning tarkibida ma'lum bir element borligini tekshirishimiz mumkin.

# menu = ['osh','qazonkabob','shashlik','norin','somsa']   
# ovqat = input("Nima ovqat buyurtma berasiz ? >>>")
# if ovqat in menu:
#     print("Siz buyurtma qilgan ovqat menyuda bor")
# else:
#     print("Afsuski siz buyurtma qilgan ovqat menyuda bor")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Bizda {taom} bor")
#     else:
#         print(f"uzr bizda {taom} yo'q")
        
# uzb_mashinalar = ["cobalt","tico","matiz","nexia"]
# mashinalar =["cobalt","jiguli","matiz","nexia","changan"]
# for mashina in mashinalar:
#     if mashina in uzb_mashinalar:
#         print(f"{mashina}-O'zbekistonda ishlab chiqariladi")
#     else:
#         print(f"{mashina} - chet elda ishlab chiqariladi")
        
# print("Juft va toq sonlarni ajratish")       
# juft_sonlar = [0,2,4,6,8,10]
# sonlar = [0,2,5,3,7,8,10]
# for son in sonlar:
#     if son in juft_sonlar:
#         print(f"{son} - juft")
#     else:
#         print(f"{son} - toq")

# son = int(input("Iltimos,juft sonni kiriting>>> "))
# if son %2 == 0:
#     print("Rahmat")
# else:
#     print("Bu juft son emas")
    
# son = int(input("Iltimos,toq sonni kiriting>>> "))
# if son %2 == 1:
#     print("Rahmat")
# else:
#     print("Bu toq son emas")

# sonlar = [1, 4, 7, 8, 10, 15, 22]
# for son in sonlar:
#     if son %2 == 0:
#         print(f"{son} - juft")
#     else:
#         print(f"{son} -juft emas")
        
# a=int(input("Birinchi juft sonni kiriting >>>"))
# b=int(input("Ikkinchi juft sonni kiriting >>>"))
# if a %2 == 0  and  b %2 == 0:
#      print("Ikkalasiyam juft")
# if a %2 == 0:
#     print("Birinchisi juft")
# if b %2 == 0:
#     print("Ikkinchisi juft")
# else:
#     print("Ikkalasiyam toq")


# yosh  = int(input("Yoshingizni kiriting>>>"))

# if yosh<= 4  or  yosh>= 60:
#     narh = 0
# elif yosh <= 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Sizga kirish {narh}")

# x = float(input("Birinchi sonni kiritimg >>>"))
# y = float(input("Ikkinchi sonni kiriting >>>"))

# if x > y:
#     print("Birinchi son ikkinchisidan katta")
# elif x<y:
#     print("Ikkinchi son birinchisidan katta")
# else:
#     print("Ikkala son teng")
    
    
# mahsulotlar = ["tuz",'piyoz','daftar','ruchka','qalam','tuxum','non','pichoq','qoshiq']
# savat = ['piyoz','daftar','non','tuxum','un','choy']    
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"{mahsulot.title()} - Do'konimizda bor")
#     else:
#         print(f"{mahsulot.title()} - Do'konimizda yo'q")
    

# mahsulotlar  = []
# for n in range(5):
#     mahsulotlar.append(input(f"{n+1} - mahsulotni kiriting >>>"))
# print(f"Siz tanladingiz {mahsulotlar}")
# bor_mahsulotlar = ['un','non','kitob','ruchka','piyoz','shakar']
# for mahsulot in bor_mahsulotlar:
#     if mahsulot in mahsulotlar:
#         print(f" Bizda bor {mahsulot} bor")
#     else:
#         print(f" Bizda {mahsulot} yo'q")

# mahsulotlar = [input(f"{i+1}-mahsulotni kiriting: ") for i in range(5)]
# bor = ['un','non','kitob','ruchka','piyoz','shakar']

# for m in bor:
#     print(f"Bizda {m} bor" if m in mahsulotlar else f"Bizda {m} yo'q

# foydalanuvchilar = ['ruchka','kitob','daftar','stol','uy']
# login = input("Loginingizni kiriting>>>")
# if login in foydalanuvchilar:
#     print("Login band, boshqa login tanlang")
# else:
#     print("Xush kelibsiz")

# son  = int(input("Butun son kiriting >>>"))
# for n in range(2,11):
#     if not(son%n):
#     print(f"{n}")


son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni 10 gacha sonlardan {n} ga qoldiqsiz bo'linadi")    


    


    


    





























































    







































