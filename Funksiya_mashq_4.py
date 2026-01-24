#=========== FUNKSIYA ====================
# def salom_ber(ism):
#     print(f"Assalomu Alaykum,{ism}")
    
# salom_ber("Anvar")
# salom_ber("Olim")

# =========---TUG'ILGAN YILNI HISOBLOVCHI FUNKSIYA ---=============

# def t_yil_hisobla(ism,t_yil):
#     print(f"Salom,{ism.title()} siz {2026-t_yil} yoshdasiz")
# t_yil_hisobla('Ali',1987)    
# t_yil_hisobla( t_yil=1987,ism='Ali')


# =========---SONNING KVADRATI VA KUBINI HISOBLOVCHI FUNKSIYA ---=========

# def daraja_hisobla(son):
#     print(f"Siz kiritgan son {son} kvadrati {son**2},kubi {son**3}ga teng")
    
# daraja_hisobla(3)


# =========---SONNING KVADRATI VA KUBINI HISOBLOVCHI FUNKSIYA ---=========

# def juft_toq_aniqla(son):
#     if son%2==0:
#         print(f"{son} - juft son")
#     else:
#         print(f"{son} - toq son")
        
# juft_toq_aniqla(7)
# juft_toq_aniqla(8)


# =========---SONNING KVADRATI VA KUBINI HISOBLOVCHI FUNKSIYA ---=========

# def kattasini_top(x,y):
#     if x>y:
#         print(f"{x}>{y}")
#     elif x<y:
#         print(f"{x}<{y}")
#     else:
#         print(f"{x}={y}")
        
# kattasini_top(3, 7)
# kattasini_top(10, -100)
# kattasini_top(20, 20)


# ====FOYDALANUVCHIDAN IKKI SONNI OLIB KONSOLGA CHIQARUVCHI FUNKSIYA =====
def bolinish_alomatlar(son):

    for n in range(2,11):
        
        if son%n==0:
            print(f"{son}:{n}={son/n}")
        
bolinish_alomatlar(15)
bolinish_alomatlar(20)


        
        








    
    
    