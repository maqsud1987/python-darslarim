# ========= Telefon kitobi funksiyasi yozing (qo‘shish/qidirish) ==========
# Telefon kitobi dictionary
telefon_kitob = {}

# Kontakt qo'shish funksiyasi
def tel_kitob():
    ism = input("Ismingizni kiriting: ")
    telefon = int(input("Telefon raqamini kiriting: "))
    telefon_kitob[ism] = telefon

# Dastur boshlanishi
print("========= Telefon Kitobiga Xush Kelibsiz ==========")

while True:
    # Foydalanuvchidan tanlov olish
    tanlov = input("1 - Kontakt qo'shish, 2 - Kontakt qidirish, 3 - Chiqish: ")

    # Kontakt qo'shish
    if tanlov == "1":
        tel_kitob()

    # Kontakt qidirish
    elif tanlov == "2":
        ism = input("Qaysi ismni qidiryapsiz? ")
        if ism in telefon_kitob:
            natija = telefon_kitob[ism]
        else:
            natija = "Bunday ism ro'yxatda yo'q"
        print(natija)

    # Chiqish
    elif tanlov == "3":
        print("Dasturdan chiqish...")
        break

    # Noto'g'ri tanlovni qayta so'rash
    else:
        print("Noto‘g‘ri tanlov. Iltimos, 1, 2 yoki 3 ni kiriting.")
                  
    
    
    
    
    


        
        

# print(tel_kitob())
# print(tel_kitob())  
# print(tel_kitob())







   
    


    
    
    
    
    
    

        
        
        
      
        
        
    
    



























    
    

    

        
