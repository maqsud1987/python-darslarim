#----------------------- 📌 FAYNI O'QISH ---------------------------

# with open("pi.txt") as file:
#     pi = file.read()

# print(pi)

# pi=pi.rstrip()
# pi=pi.replace("\n"," ")
# pi=float(pi)
     
# print(pi)
#==============================================================

# with open("pi.txt") as file:
#     for line in file:
#         print(line)

# =============================================================
    # 🟢 1 Matnnni qatorma-qator o'qish
    
filename = "data/talabalar.txt"
# with open(filename) as file:
#     for line in file:
#         print(line)
        
   # 🔴 2 Ro'yxatga joylasah --- readlines() --- yordamida(List qiladi)  
   
with open(filename) as file:
    talabalar = file.readlines()
print(talabalar)
    
   # 🟡 3 Matndagi bo'shliqni olib tashlash 

talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)   


# ------------------------  📌 FAYLGA YOZISH  -----------------------------

# faylnomi = 'new_file.txt'  #  bo'sh fayl

#     # ✔ Yangi faylga  yozish yoki eski faylni o'chirib qaytatdan yozish

# ism = 'Olimjon Hasanov'  
# tyil = 1994
# with open(faylnomi,'w') as file:   #'w'(write)-yozish,eskisini o'chirib ustiga yozadi
#     file.write(ism)
#     file.write(str(tyil))
    
#     # ✔ Agar qator tashlab yozamiz desak 
    
# faylnomi = 'new_file.txt'  # bo'sh fayl
# ism = 'Olimjon Hasanov'
# tyil = 1994

# with open(faylnomi,'w') as file:
#     file.write(ism+'\n')
#     file.write(str(tyil)+'\n')
    
#     # ✔ Agar qator tashlab yozamiz desak 
    
# with open(faylnomi,'a') as file:  # 'a'(append)-qo'shish,ustiga qo'shadi o'chirmaydi
#      file.write('Salim Halimov\n')
#      file.write('2000')
    
# # --------- 📌 FAYLDA OBYEKT SAQLASH(lug'at,class,o'zgaruvchi......) --------

# import pickle                # info.pkl  - fayl nomi

# talaba1 = {'ism': 'hasan', 'familiya': 'husanov', 'tyil': 2003, 'kurs': 2}
# talaba2 = {'ism': 'alijon', 'familiya': 'valiyev', 'tyil': 2004, 'kurs':1}
    
# with open('info.pkl','wb') as file:  #'wb'(write-binary)-ikkilik sanoq sistemasida yozish
#     pickle.dump(talaba1, file)
#     pickle.dump(talaba2, file)
    




