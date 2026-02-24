# def  juftmi(son):
#     if son%2==0:
#         return True
#     else:
#         return False
# print(juftmi(20))
# print(juftmi(21)) 
    
#========================================================

# def  juftmi(son):
#     return son%2==0
       
# print(juftmi(20))
# print(juftmi(21)) 

#========================================================

# def katta_va_juft(son):
#     return son>10 and son%2==0
  
    
# print(katta_va_juft(12))
# print(katta_va_juft(51))

#=========================================================

# def murakkab(son):
#     return son>0 and son%3==0 and son%2!=0
# print(murakkab(60))
# print(murakkab(-60))
# print(murakkab(15))

#=========================================================
# def kvadrat(son):
#     return son*son


# def juftmi(son):
#     return son%2==0


# def juft_va_kvadrat(son):
#     if juftmi(son):
#         return kvadrat(son)
#     else:
#         return 0


# print(juft_va_kvadrat(10))
# print(juft_va_kvadrat(11))

#===========================================================

# def juftmi(son):
#     return son%2==0

# def musbatmi(son):
#     return son>0

# def uchga_bolinadimi(son):
#     return son%3==0

# son = int(input("Sonni kiriting: "))

# print(f"Juftmi:{juftmi(son)}")
# print(f"Musbatmi:{musbatmi(son)}")
# print(f"Uchga bo'linadimi:{uchga_bolinadimi(son)}")

#===========================================================

def bahola(ball):
    if 90<=ball<=100:
        return "A+"
    if 80<=ball<90:
        return "A"
    if 70<=ball<80:
        return "B+"
    if 60<=ball<70:
        return "B"
    if 0<=ball<=60:
        return "C"
    else:
        return "Noto'gri ball"
    
ball = int(input("Balingizni kiriting: "))

print(bahola(ball))

    










    