# ========-- SEVIMLI KITOBNI FOYDALANUVCHIDAN OLUVCHI DASTUR -=========

# savol= "Sevimli kitobingizni kiriting(agar to'xtatmoqchi bo'lsangiz 'exit' deb yozing): "
# sevimli_kitoblar = []
# while True:
#     qiymat = input(savol)
#     if qiymat.lower()=="exit":
#         print("Dastur to'xtadi")
#         break
    
#     sevimli_kitoblar.append(qiymat)
# for kitob in sevimli_kitoblar:    
    
#      print(f"Sizning sevimli kitoblar - {kitob}")


# ========-- FOYDALANUVCHI YOSHINI OLIB NARX CHIQARADIGAN DASTUR -=========


# while True:
#     qiymat = input("Yoshingizni kiriting(to'xtatish uchun 'exit' yoki 'quit' deb yozing): ")
#     if qiymat.lower() in ['exit','quit']:
#         print("Dastur to'xtadi")
#         break
      
#     yosh = int(qiymat)
#     if yosh<=7:
#         narx = 3000
#     elif 7<yosh<=18:
#         narx=5000
#     else:
#         narx=1000
        
#     print(f"Sizga kirish {narx} so'm")


#========-- BU KODDAGI XATONI TOPDIK --=========

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == "exit":
        print("Dastur to'xtadi")
        break
    yosh = int(qiymat)
        
    if yosh<0:
        print("Siz manfiy son kiritdingiz,qayta kiriting :")
        continue
    
   
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
        
        

        



        
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    

    