# ismlar = [] # bo'sh ro'yxat yaratildi
# n = 1       # tsikl 1 dan boshlanadi
# while True:       # abadiy tsikl
#     savol = f"{n} - do'stingizni kiriting : "   # shunchaki matn
#     ism = input(savol) # ism o'zgaruvchiga matn savol qilib kiritildi
#     ismlar.append(ism)  # savolga qaytgan javob ismlarga qo'shildi
#     takrorlash = input("yana ism qo'shasizmi ? (ha/yo'q)") # yana savol 
#     n += 1 # tsiklga 1 qo'shib davom etadi 
#     if takrorlash.lower() != 'ha': # agar javob 'ha' bo'lmasa
#         break  # tsikl to'xtaydi
    
# print("Sizning do'stlaringiz: ") # tsikldan tashqari yozuv
# for ism in ismlar:  # to'ldirilgan ismlar ro'yxatdagi har bir ism uchun
    
#     print(ism.title()) 


# print("Do'stlaringiz yoshini saqlaymiz")
# dostlar = {}
# ishora =True
# while ishora:
#     ism = input("Do'tingizni ismini kiriting : ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting : ")
#     dostlar[ism] = int(yosh)
    
#     javob = input("Yana ma'lumot kiritasizmi?(ha/yo'q)")
#     if javob == 'yo\'q':
#         ishora = False
# print("Sizning do'stlaringiz :")
# for ism,yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")
    


# cars = ['nexia','lacetti','nexia','cobalt','jiguli','nexia']
# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)


# talabalar = ['hasan','husan','olim','botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ni baholang : ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = int(baho)
    

# print("\nBarcha talabalar baholandi!")
# print(baholangan_talabalar)

# mijozlar = ['maqsud','umid','shaxlo','oqila']
# xarid_summasi = {}
# while mijozlar:
#     mijoz = mijozlar.pop()
#     summa = input(f"{mijoz.title()} necha so'mlik xarid qildingiz : ")
#     print(f"{mijoz.title()} xaridini kiritdi")
#     xarid_summasi[mijoz] = int(summa)


# print("Barcha mijozlar xizmatdan foydalanishdi")
# print(xarid_summasi)

# jami = sum(xarid_summasi.values())
# print(f"Jami xarid summasi: {jami} so'm")



# foydalanuvchilar = []
# while True:
#     qiymat = input("Mahsulotni kiriting (exit = to‘xtash): ")
#     if qiymat == 'exit':
#         break
#     foydalanuvchilar.append(qiymat)
    
# print("Foydalunuvchilar ro'yxati : ")
# for foydalanuvchi in foydalanuvchilar:
    
#     print(foydalanuvchi.title())


# savat = []
# while True:
#     qiymat = input("Mahsulotni kiriting : ")
#     savat.append(qiymat)
#     javob = input("Yana mahsulot kiritasizmi (ha/yo'q)")
#     if javob == "yo'q":
#         break
    

# print("Siz kiritgan mahsulotlar : ")
# for mahsulot in savat:
    
#       print(f"{mahsulot.title()}")


# mahsulotlar = {}
# while True:
#     mahsulot = input("Mahsulotni kiriting : ")
#     if mahsulot == 'exit':
#         break
#     narx = input("Narxni kiriting : ")
    
#     mahsulotlar[mahsulot]= int(narx)
    
    
# for kalit,qiymat in mahsulotlar.items():
#     print(f"{kalit.title()} {qiymat} so'm")
    
# mahsulotlar = {} 
# while True: 
#     mahsulot = input("Mahsulot nomini kiriting: ") 
#     narh = int(input(f"{mahsulot.title()}ning narhini kiriting: ")) 
#     mahsulotlar[mahsulot] = narh 
    
#     javob = input("Yana mahsulot qo'shasizmi? (ha/yo'q): ") 
#     if javob.lower() != 'ha':
#         break

# print(mahsulotlar)



# print("Do‘stlaringiz ismi va ularning yoshini saqlaydigan dastur .")
# dostlar = {}
# while True:
#     ism = input("Do'stingiz ismini kiriting : ")
#     yosh = int(input("yoshini kiriting : "))
#     dostlar[ism]  = yosh
#     javob = input("yana ism kiritasizmi?(ha/yo'q)")
#     if javob.lower() != 'ha':
#         break
# for key,value in dostlar.items():
#     print(f"{key.title()} {value} yoshda")



# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}

# while buyurtmalar:
#     savol = buyurtmalar.pop()
#     if savol in mahsulotlar:
        
#         print(f"{savol.title()} {mahsulotlar[savol]} so'm")
#     else:
#         print(f"Bizda {savol.title()} yo'q")
        
 
        
buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")
    
    
    

    


    







    
        
   
  
        







   
   
    
    

    
    




































    
    