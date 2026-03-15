#====Foydalanuvchi ismi va yoshini so'rab,uning tug'ilgan yilini hisoblang=

# def foydalanuvchi_info(ism,yosh):
#     return f"Foydalanuvchining ismi {ism},{2026-yosh}-yilda tug'ilgan"
# print(foydalanuvchi_info("Ali", 27))

#======== Son olib, uning kvadrati va kubini konsolga chiqaruvchi =========

# def son_kv_kub(son):
#     return f"{son} ning kvadrati-{son**2},kubi-{son**3} "
# print(son_kv_kub(2))

# =============Son olib, son juft yoki toqligini aniqlang =================

# def juft_yoki_toq(son):
#     if son<0:
#         return "Bu manfiy son boshqa son kiriting"
#     if son%2==0:
#         return "Juft"
#     else:
#         return "Toq"
# print(juft_yoki_toq(12))
# print(juft_yoki_toq(11))
# print(juft_yoki_toq(2))
# print(juft_yoki_toq(0))
# print(juft_yoki_toq(-8))

# ============ Mini kalkulyator funksiyasi yozing (+, -, *, /) ==============
def mini_kalkulyator(a, b, amal):

    if amal == "+":
        return a + b
    elif amal == "-":
        return a - b
    elif amal == "*":
        return a * b
    elif amal == "/":
        if b != 0:
            return a / b
        else:
            return "0 ga bo‘lish mumkin emas"
    else:
        return "Noto‘g‘ri amal"


while True:

    a = int(input("1-sonni kiriting: "))
    b = int(input("2-sonni kiriting: "))
    amal = input("Amalni tanlang (+, -, *, /): ")

    print("Natija:", mini_kalkulyator(a, b, amal))

    chiqish = input("To'xtatish uchun 'stop' yozing, davom etish uchun Enter bosing: ")
    
    if chiqish == "stop":
        break
   
    


    
    
    
    
    
    

        
        
        
      
        
        
    
    



























    
    

    

        
