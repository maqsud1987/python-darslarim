# ======== TUB SONNI VA ORALIQDAGI TUB SONNI ANIQLOVCHI FUNKSIYA ==========

# # 1-qism  BU BIRINCHI FUNKSIYA  ----- BU ISHCI  -----

# def tub_sonmi(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#     return True

# # 2-qism IKKINCHI FUNKSIYA ---- BU ISHCHIGA BUYURADI ----

# def tub_son_oraliq(boshi,oxiri):
#     tub_sonlar = []
#     for son in range(boshi,oxiri+1):
#         if tub_sonmi(son): # oraliqdagi sonlarni 1-funksiyada tekshiradi
#             tub_sonlar.append(son)
            
#     return tub_sonlar
        
# print(tub_son_oraliq(5, 30))


# ======== JUFT SONNI ANIQLOVCHI FUNKSIYA ==========

# # 1-funksiya

# def juft_sonmi(n):
    
#     if n%2==0:
#         return True
#     return False

# # 2-funksiya

# def juft_son_oraliq(boshi,oxiri):
#     juft_sonlar = []
#     for n in range(boshi,oxiri+1):
#         if juft_sonmi(n):#Agar juft_sonmi(n) True qaytarsa, quyidagi blokni bajar
#              juft_sonlar.append(n)
        
#     return juft_sonlar

# print(juft_son_oraliq(-10, 15)) 

# ======= FIBONACCHI KETMA-KETLIGINI ANIQLOVCHI FUNKSIYA =========
# ======= FIBONACCHI KETMA-KETLIGI ========
# def fibonacci(n):
#     fibonaccilar = []
#     for x in range(n):
#         if x == 0:
#             fibonaccilar.append(0)
#         elif x == 1:
#             fibonaccilar.append(1)
#         else:
#             fibonaccilar.append(fibonaccilar[x-1] + fibonaccilar[x-2])
#     return fibonaccilar

# print(fibonacci(10))

            


def fibonacci(n):
    songacha = []
    for x in range(n):
        if x ==0:
            songacha.append(0)
        elif x==1:
            songacha.append(1)
        else:
            songacha.append(songacha[x-1]+songacha[x-2])
    return songacha
print(fibonacci(5))



































   
     


   
    
    
    
    
     
    
    
    

   
        
    



    









  


    
