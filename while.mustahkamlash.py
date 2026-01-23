# ============ FOYDALANUVCHIDAN BUYURTMA OLUVCHI DASTUR ============
# savat = []
# n=1
# while True:
#     savol = f"{n} - buyutmani kiriting: "
#     mahsulot = input(savol)
#     savat.append(mahsulot)
#     takrorlash = input("Yana mahsulot kiritasizmi (ha/yo'q): ")
#     if takrorlash.lower()!= "ha":
#         break
#     n += 1
# print("Siz buyurgan mahsulotlar:")    
# for mahsulot_1 in savat:
#     print(mahsulot_1.title())
    
# ============ BUYURTMANI SOLISHTIRISH ===============
    
# mahsulotlar = ['olma','nok','anor','olcha','sabzi']    
# savat = []
# n=1
# while True:
#     savol = f"{n} - buyutmani kiriting: "
#     mahsulot = input(savol)
#     savat.append(mahsulot)
#     takrorlash = input("Yana mahsulot kiritasizmi (ha/yo'q): ")
#     if takrorlash.lower()!= "ha":
#         break
#     n += 1
    
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"{mahsulot} bor")
#     else:
#         print(f"{mahsulot} yo'q ")

# ========== MAHSULOTNI LUG'AT KO'RINISHIDA OLISH ============

# mahsulot = {}
# n=1
# while True:
#     key = input(f"{n}-mahsulotni kiriting: ")
#     value = int(input("Narxini kiriting :"))
#     mahsulot[key]=value
#     takrorlash = input("Yana mahsulot kiritasizmi (ha/yo'q): ")
#     if takrorlash.lower()!= "ha":
#        break
#     n+=1
    
# for key,value in mahsulot.items():
#     print(f"{key.title()} ning narxi {value} so'm")

# ============================================================================
# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000} 
# print("Bizda quyidagi mahsulotlar bor: ") 
# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narx = mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()} - {narx} so'm")
#     else:
#         print(f"Bizda {buyurtma} yo'q ")

# ================= QO'SHIMCHA MASHQ =========================================

savat = []
n=1
while True:
    mahsulot = input(f"{n}-mahsulotni kiriting: ")
    savat.append(mahsulot)
    n+=1
    takrorlash= input("Yana mahsulot kiritasizmi(ha/yo'q): ")
    if takrorlash != "ha":
        break
   
print("Siz kiritgan mahsulotlar: ")
for  mahsulot in savat:
    print(mahsulot.title())
    

    
    
    