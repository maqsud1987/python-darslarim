# def qosh(a,b):
#     return a+b

# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))

# print(qosh(a, b))

#=========================================================

# def qosh(a,b):
#     return a+b

# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))

# c = qosh(a, b) 

# if c>10:
#     print("katta")
# else:
#     print("kichik")

#=========================================================

# royxat = [2,4,8,-12]
# def sonlar(royxat):
#     eng_katta = royxat[0]
#     for i in royxat:
#         if i > eng_katta:
#             eng_katta = i
#     return eng_katta
    
# natija = sonlar(royxat)
# print(natija)

#=========================================================

# def foydalanuvchilar(ism, familiya, t_yil, t_joy,email="",tel=""):
#     mijoz = {
#         "ism":ism,
#         "familiya":familiya,
#         "t_yil": t_yil,
#         "yoshi":2026 - int(t_yil),
#         "t_joy":t_joy,
#         "email":email,
#         "telefon":tel, 
#           }
#     return mijoz


# mijozlar = []
# while True:
#     ism = input("Ismingizni kiriting: ")
#     familiya = input("Familiyanangiz: ")
#     t_yil = int(input("Tug'ilgan yilingiz:"))
#     t_joy = input("Tupg'ilgan joyingiz: ")
#     email = input("imail: ")
#     telefon = input("Telefon: ")
    
#     mijozlar.append(foydalanuvchilar(ism, familiya, t_yil, t_joy,email,telefon))
#     davom = input("davom etasizmi(ha/yoq) ?")
#     if davom!="ha":
#         break
# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}," 
#           f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}")
    
#===========================================================    

# def kattasini_top(x,y,z):
#     eng_katta = x
#     if y>x:
#         eng_katta=y
#     if z>y:
#         eng_katta=z
#     return eng_katta

# print(kattasini_top(3, 5, -100))

#=============================================================

def tub_son(son):
    if son<=1:
        return False
    for n in range(2,son):
        if son%n==0:
            return False
        
    return True
    


def tub_son_oraliq(x,y):
    tub_sonlar = []
    for z in range(x,y+1):
        if tub_son(z):
            tub_sonlar.append(z)
        
    return tub_sonlar
        
print(tub_son_oraliq(2, 15))
        
           
        
        
    
        
    
    
    
    
    
    
    
    
    
    
    
                        

        