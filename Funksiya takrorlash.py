# def foydalanuvchi_info(ism,familiya,yosh):
#   print(f"{ism} {familiya} {yosh}")
    
# foydalanuvchi_info('Ali','Salimov', 37)

# def son_daraja(son):
#     print(f"{son} ning kvadrati {son**2},kubi esa {son **3} ")
   
    
# son_daraja(3)
    
# def juft_toq(son):
#     if son%2==0:
#         print(f"{son} - juft son ")
#     else:
#         print(f"{son} - toq son ")
        
# juft_toq(12)
# juft_toq(11)


# def katta_kichik(x,y):
#     if x<y:
#         return y
#     elif x>y:
#         return x
#     else:
#         return "Bu sonlar teng"
        
# print(katta_kichik(3, 5))
# print(katta_kichik(3, -5))
# print(katta_kichik(3, 3))

# def kichigini_top(x,y):
#     if x<y:
#         return x
#     elif y<x:
#         return y
#     return "ular teng"
# print(kichigini_top(5, 5))
# print(kichigini_top(-5, 5))
# print(kichigini_top(5,115))

# def ayirma_taqqosla(k,z):
#     if k>z:
#         return k-z
#     elif z>k:
#         return z-k
#     return 0

# print(ayirma_taqqosla(5, 5))
# print(ayirma_taqqosla(-5, 5))
# print(ayirma_taqqosla(5,115))



#-----Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan ------
#-----sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. -------
def bolinish_alomatlari(son):
    if son <2:
        return False
    for n in range(2,11):
        if son%n==0:
            return True
    print(f"{son} soni {n} ga bo'linadi")
        
        
    return False
    
bolinish_alomatlari(1)
bolinish_alomatlari(18)
bolinish_alomatlari(-10)



# def bolinish_alomatlari(son):
#     if son < 2:
#         return False
    
#     bolinadi = False
#     for n in range(2, 11):
#         if son % n == 0:
#             print(f"{son} soni {n} ga bo'linadi")
#             bolinadi = True  # bo‘linadigan son topildi
    
#     return bolinadi

# # Test
# bolinish_alomatlari(1)
# bolinish_alomatlari(18)
# bolinish_alomatlari(-10)






    
    



        


        
     

        
        
        