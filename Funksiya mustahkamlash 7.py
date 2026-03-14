# =================== Sonni teskari yozib qaytaring =====================
# def sonning_teskarisi(son):
#     teskarisi=0
#     while son>0:
#         raqam = son%10
#         teskarisi=teskarisi*10+raqam
#         son=son//10
#     return teskarisi

# print(sonning_teskarisi(12345))

# ===================== 	Son palindrome ekanini tekshiring =================
# def palindrome(son):
#     son=abs(son)
#     teskarisi = 0
#     asl_son=son
    
#     while son>0:
#         raqam=son%10
#         teskarisi=teskarisi*10+raqam
#         son=son//10
#     if asl_son == teskarisi:
#         return True
#     else:
#         return False
            
# print(palindrome(-1331))
# print(palindrome(101))
# print(palindrome(112))

# ============= Sonning raqamlari ko‘paytmasini qaytaring ================
# def raqamlar_kopaytmasi(son):
    
#     kopaytma=1
#     while son>0:
#         raqam = son%10
#         kopaytma*=raqam
#         son=son//10
#     return kopaytma

# print(raqamlar_kopaytmasi(1234))

# =========== N gacha bo‘lgan tub sonlarni list qilib qaytaring =========
# def oraliq_tub_sonlar(son):
#     if son<0:
#         return "Tub emas"
    
#     for n in range(2,son):
        
#         if son%n==0:
#             return "Tub emas"
        
#     return "Tub"
# print(oraliq_tub_sonlar(10))
# print(oraliq_tub_sonlar(7))
# print(oraliq_tub_sonlar(11))
# print(oraliq_tub_sonlar(2))

# ============= 2 ta listni birlashtirib takrorsiz qaytaring =============
# royxat_1 = [1,3,8,9,2,4]
# royxat_2 = [3,7,4,5,6,2]
# def ikki_list(royxat_1,royxat_2):
#     natija = []
#     for son_1 in royxat_1:
#         if son_1 not in natija:
#             natija.append(son_1)
#     for son_2 in royxat_2:
#         if son_2 not in natija:
#             natija.append(son_2)
#     return natija

# print(ikki_list(royxat_1, royxat_2))


# royxat_1 = [1, 3, 8, 9, 2, 4]
# royxat_2 = [3, 7, 4, 5, 6, 2]

# natija = list(set(royxat_1 + royxat_2))

# print(natija)

sonlar = [1, 2, 2, 3, 4, 4, 5]
print(set(sonlar))
    
    
    
    

        
        
        
      
        
        
    
    



























    
    

    

        
