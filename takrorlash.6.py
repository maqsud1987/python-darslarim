# def katta_harf(matnlar):
#     yangi_matnlar=[]
#     for matn in yangi_matnlar:
#         yangi_matnlar.append(matnlar)
#     return yangi_matnlar

# matnlar = ["ali","vali","salim"]
# print(katta_harf(matnlar))

#============================================================

# def yigindi(a,b):
#     return a+b
# print(yigindi(3, 5))


#======== Sonning modulini qaytaruvchi funksiya =============

# def modul(son):
#    if son<0:
#        return -son
#    if son>0:
#        return son
 
# print(modul(-6))
        
#=====Son juft yoki toq ekanini qaytaruvchi funksiya yozing (True/False)=====

# def juft_toq(son):
#     if son%2==0:
#         return True
#     if son%2 !=0:
#         return False
    
    
# print(juft_toq(22))
# print(juft_toq(21))
# print(juft_toq(0))  

#===== 3 ta sonning o‘rtachasini qaytaruvchi funksiya yozing =============  

# def ortachasini_top(x,y,z):
#     return (x+y+z)/3
# print(ortachasini_top(3, 4, 5))
# print(ortachasini_top(-3, 4, 7))

#========== Sonning 10% ini qaytaruvchi funksiya yozing ================

# def foiz(son,foiz):
#     return son*foiz/100
# print(foiz(100,10))
# print(foiz(250,20))

#=========Sonning ildizini qaytaruvchi funksiya yozing============

# def ildiz(son):
#     if son<0:
#         return "Manfiysondan ildiz chiqmaydi"
#     if son==0:
#         return "0 dan ildiz chiqmaydi"
#     if son>0:
#         return son**(1/2)
# print(ildiz(100))
# print(ildiz(0))
# print(ildiz(-100))

#======== Son 5 ga bo‘linadimi tekshiruvchi funksiya yozing =======

# def beshga_bolinish(son):
#     if son%5==0:
#         return True

# print(beshga_bolinish(25))
# print(beshga_bolinish(-25))
# print(beshga_bolinish(0))
# print(beshga_bolinish(17))

#==== Son 3 va 7 ga bo‘linadimi tekshiruvchi funksiya yozing =====

# def uchga_yettiga_bolish(son):
#     return son%3==0 and son%7==0
    
    
# print(uchga_yettiga_bolish(21))
# print(uchga_yettiga_bolish(12))
# print(uchga_yettiga_bolish(63))

#====Yoshga qarab “Voyaga yetgan” yoki “Voyaga yetmagan” qaytaring=====

# def chegara(yosh):
#     if yosh<18:
#         return "Voyaga yetmagan"
#     else:
#         return "Voyaga yetgan"

# print(chegara(12))
# print(chegara(18))
# print(chegara(22))

#====== Baho (0–100) asosida harfli baho qaytaring (A/B/C/D/F) ======

# def oraliq_baho(ball):
#     if ball<0 or ball>100:
#         return "Noto'g'ri ko'rsatgich"
#     if 90<=ball<=100:
#         return "A"
#     if 80<=ball<90:
#         return "B"
#     if 70<=ball<80:
#         return "C"
#     if 0<=ball<70:
#         return "D"
#     if ball<0 or ball>100:
#         return "Noto'g'ri ko'rsatgich"
    
# print(oraliq_baho(22))
# print(oraliq_baho(96)) 
# print(oraliq_baho(-200))
# print(oraliq_baho(101))
# print(oraliq_baho(72))
# print(oraliq_baho(85))
# print(oraliq_baho(0.5))

#===Parol to‘g‘ri yoki noto‘g‘ri ekanini tekshiruvchi funksiya yozing====

# def parol_tekshir(parol):
#     if parol.lower()=="ona":
#         return True
#     else:
#         return False
    
# print(parol_tekshir("salom"))
# print(parol_tekshir("non"))
# print(parol_tekshir("Ona"))
# print(parol_tekshir("ona"))

#========= 2 ta son teng yoki teng emasligini qaytaring ===============

def taqqosla(x,y):
   
    if x==y:
        return "ular teng"
    else:
        return "teng emas"

print(taqqosla(3, 9))
print(taqqosla(3, 3))










   
    

        

    
