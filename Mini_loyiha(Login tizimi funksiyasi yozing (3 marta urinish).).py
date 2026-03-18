# ============ Login tizimi funksiyasi yozing (3 marta urinish) =============
def check_login(login,parol):
    
    haqiqiy_login = "Mustafo"
    haqiqiy_parol = "1a2b3c4d5"
    if login==haqiqiy_login and parol==haqiqiy_parol:
        natija = "Xush kelibsiz"
    else:
        natija = "Parol yoki login xato,qayta urinib ko'ring"
    return natija

urinishlar_soni=3
while urinishlar_soni>0:
    login=input("Loginingizni kiriting: ")
    parol=input("Parolingizni kiriting:")
    xulosa = check_login(login, parol)
    print(xulosa)
    if xulosa == "Xush kelibsiz":
        break
    else:
        urinishlar_soni -=1
    if urinishlar_soni == 0 and xulosa != "Xush kelibsiz":
        print("Tizim bloklandi 5 minutdan keyin qayta urinib ko'ring")
    


    
    