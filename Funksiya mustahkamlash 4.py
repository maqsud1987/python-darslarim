#===Matn katta harf bilan boshlanadimi tekshiruvchi funksiya yozing===

# def katta_harf_bormi(matn):
#     if matn[0].isupper():
#         return True
#     else:
#         return False
# print(katta_harf_bormi("Ona"))
# print(katta_harf_bormi("Ota"))
# print(katta_harf_bormi("salom"))
    
# ======= 1 dan N gacha yig‘indini qaytaruvchi funksiya yozing ===========

# def yigindi(n):
#    return sum(range(1,n+1))
# print(yigindi(3))

# ------- for bilan --------

# def gacha_yigindini_top(n):
#     yigindi=0
#     for x in range(1,n+1):
#         yigindi+=x
#     return yigindi
# print(gacha_yigindini_top(3))

# =========== 1 dan N gacha ko‘paytmani (faktorial) qaytaring =============

# def gacha_kopaytmani_top(n):
#     son =1
#     for k in range(1,n+1):
#         son = son*k
#     return son
        
# print(gacha_kopaytmani_top(3))

# ========= Sonning bo‘luvchilarini list ko‘rinishida qaytaring ==========

# def boluvchilarini_top(a):
#     boluvchilar = []
#     for n in range(1,a+1):
#         if a%n==0:
#             boluvchilar.append(n)
#     return boluvchilar
    
# print(boluvchilarini_top(10))
    
# # ========= 1 dan N gacha sonlar ichidagi juft sonni qaytaring =========

# def juft_son(son):
#     juft_sonlar = []
#     for n in range(2,son+1):
#         if n%2==0:
#             juft_sonlar.append(n)
#     return juft_sonlar
# print(juft_son(20))

# ============ Son tub ekanini tekshiruvchi funksiya yozing ==============

def tub_son_aniqla(son):
    
    for x in range(2,son+1):
        if son%x==0:
            return "Tub emas"
        
    return "tub"
        
print(tub_son_aniqla(2))        
print(tub_son_aniqla(521))
print(tub_son_aniqla(8))
print(tub_son_aniqla(3))
print(tub_son_aniqla(13))  
    
    

    

        
