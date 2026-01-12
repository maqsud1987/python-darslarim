#----Foydalanuvchidan istalgan son kiritishni so'rang. 
#----Agar son manfiy bo'lsa konsolga "Manfiy son", 
#----agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. ---#

son  = int(input("Sonni kiriting: "))

#--- variant_1 NATIJA OLISH -----
# if son<0:
#     print("Son manfiy")
# else:
#     print("Son musbat")
    
#--- variant_2 NATIJA OLISH -----
print("Son manfiy") if son<0 else print("Son musbat")


#sonning ildizini chiqaruvchi dastur
# son  = int(input("Sonni kiriting: "))

# print(son**(0.5)) if son > 0 else print("Bu son manfiy")

    

    