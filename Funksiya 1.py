# ======== 4 ta son ichidan eng kattasini qaytaruvchi funksiya yozing ========

# def kattasini_top(x,y,z,t):
#     kattasi = x
#     if y>kattasi:
#         kattasi =y
#     if z>kattasi:
#         kattasi=z
#     if t>kattasi:
#         kattasi =t
#     return kattasi

# print(kattasini_top(1, 2, 3, 4))
# print(kattasini_top(0, 0, -200, 1))

# ========= 	Yil kabisa yilmi tekshiruvchi funksiya yozing ===========

# def tekshir(yil):
#     if yil%400==0: 
#         return "Kabisa yili"
#     elif  yil%100 ==0:
#         return "Kabisa yili emas"
#     elif  yil%4==0:
#         return "Kabisa yili"
#     else:
#         return "Kabisa yili emas"
    
# print(tekshir(2004))
# print(tekshir(2000)) 
# print(tekshir(2025))
# print(tekshir(2024))
# print(tekshir(2026))
# print(tekshir(2028))
# print(tekshir(1987))  

# =============== Oy raqamiga qarab faslni qaytaring =====================

# def fasl_aniqla(sana):
#     if 1>sana or 12<sana:
#         return False
#     elif 3<=sana<=5:
#         return "Bahor"
#     elif 6<=sana<=8:
#         return "Yoz"
#     elif 9<=sana<=11:
#         return "Kuz"
#     elif sana in (1,2,12):
#         return "Qish"
# print(fasl_aniqla(6))
# print(fasl_aniqla(10))
# print(fasl_aniqla(2))
# print(fasl_aniqla(4))
# print(fasl_aniqla(0))

#===== Hafta kuniga qarab dam olish kuni yoki ish kuni ekanini qaytaring ======
    
# def dam_olish_kuni(kun):
#     #if kun.lower()=="shanba" or kun.lower()=="yakshanba":
#     if kun.lower() in ("shanba","yakshanba"):
#         return "Bu kun dam olish kuni"
#     else:
#         return "Bugun ish kuni"
# print(dam_olish_kuni("dushanba"))   
# print(dam_olish_kuni("shanba")) 
# print(dam_olish_kuni("seshanba"))
# print(dam_olish_kuni("chorshanba"))
# print(dam_olish_kuni("yakshanba"))    

# ========== Son 2 xonali ekanini tekshiruvchi funksiya yozing =============

def ikki_xonalimi(son):
    if 10<=abs(son)<=99:
        return "Ikki xonali son"
    else:
        return "Ikki xonali son emas"
print(ikki_xonalimi(0))
print(ikki_xonalimi(15))
print(ikki_xonalimi(125))
print(ikki_xonalimi(-89))
        
    
    


