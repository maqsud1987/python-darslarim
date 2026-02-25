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
    if ball < 0 or ball > 100:
        return "Noto'gri ball"
    elif ball >= 90:
        return "A+"
    elif ball >= 80:
        return "A"
    elif ball >= 70:
        return "B+"
    elif ball >= 60:
        return "B"
    else:
        return "C"
     
ball = int(input("Balingizni kiriting: "))

print(bahola(ball))

    










    