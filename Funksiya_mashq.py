# def ism_yosh_top(ism,yil):
#     """Foydalanuvchi ismi va yoshini so'rab, 
#     uning tug'ilgan yilini hisoblaydigan funksiya """
#     yosh = 2025 - yil
#     print(f"Foydalanuvchining isi {ism.title()},{yosh} yoshda")
    
# ism_yosh_top('mustafo', 1986)


# def son_kv_top(son):
#     """Foydalanuvchidan son olib, uning kvadrati 
#     va kubini konsolga chiqaruvchi funksiya"""
#     print(f"{son} ning kvadrati {son**2} ga,kubi esa {son**3} ga teng")

# son_kv_top(5)


# def ikki_barobar(son):
#     """Berilgan sonning 2 barobarini qaytaradi"""
#     return son * 2


# son = int(input("Sonni kiriting: "))
# natija = ikki_barobar(son)
# print("Natija:", natija)


# def uch_barobar(son):
#     """Foydalanuvchidan bitta son qabul qilib
#     shu sonning 3 barobarini hisoblovchi funksiya"""
#     return son*3

# son  = int(input("Sonni kiriting : "))
# natija = uch_barobar(son)
# print(f"{son} ning 3 barobari,{natija}")

# def juft_toq_top(son):
#     """Foydalanuvchidan son olib, son juft 
#     yoki toqligini konsolga chiqaruvchi funksiya """
#     if son%2==0:
#         return "bu son juft"
#     else:
#         return "bu son toq"
        
        
# son  = int(input("Sonni kiriting : "))
# natija = juft_toq_top(son)
# print(f"Siz {son} sonini kiritdingiz,{natija}")   

# def k_top(a,b):
#     """Foydalanuvchidan ikkita son olib, ulardan kattasini,
#     agar sonlar teng bo'lsa "Sonlar teng" degan xabarni konsolga chiqaruvchi funksiya"""
#     if a>b:
#         return f"{a} > {b}"
#     elif a <b:
#         return f"{b} > {a}"
#     else:
#         return f"{a} = {b}"
    
# a = int(input("Birinch sonni kiriting : "))
# b = int(input("Ikkinchi sonni kiriting : "))
# #natija = k_top(a,b)
# print(k_top(a, b)) 



# def son_daraja_top(a,b):
#     return f"{a} ning {b}-darajasi, {a**b} ga teng"
# a = int(input("Sonni kiriting : "))
# b = int(input("Darajasini kiriting : ")) 
# print(son_daraja_top(a, b))   


# bu kichik loyihani CHATJPT yordamida real loyihaga o'tkazib ko'rdik
# import tkinter as tk
# from tkinter import messagebox

# def son_daraja_top():
#     try:
#         a = int(entry_a.get())
#         b = int(entry_b.get())
#         natija = f"{a} ning {b}-darajasi, {a**b} ga teng"
#         label_natija.config(text=natija)
#     except ValueError:
#         messagebox.showerror("Xatolik", "Iltimos, son kiriting!")

# # Asosiy oynani yaratish
# root = tk.Tk()
# root.title("Sonning darajasini topish")
# root.geometry("400x200")

# # Kirish uchun entry va label
# label_a = tk.Label(root, text="Sonni kiriting:")
# label_a.pack(pady=5)
# entry_a = tk.Entry(root)
# entry_a.pack(pady=5)

# label_b = tk.Label(root, text="Qanday darajaga ko'tarmoqchis:")
# label_b.pack(pady=5)
# entry_b = tk.Entry(root)
# entry_b.pack(pady=5)

# # Hisoblash tugmasi
# btn_hisobla = tk.Button(root, text="Hisoblash", command=son_daraja_top)
# btn_hisobla.pack(pady=10)

# # Natija ko‘rsatiladigan label
# label_natija = tk.Label(root, text="", font=("Arial", 12))
# label_natija.pack(pady=10)

# # Oynani ishga tushirish
# root.mainloop()


# def daraja_top(x, y=2):
#     print(x ** y)

# daraja_top(5)     # y avtomatik 2 bo‘ladi
# daraja_top(5, 3)  # y = 3 bo‘ladi


           
# def tekshir_bolinish(son):
#     """Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha 
#     bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya"""
#     bolinuvchilar = []
    
#     for boluvchi in range(2, 11):
#         if son % boluvchi == 0:
#             print(f"{son} soni {boluvchi}ga qoldiqsiz bo'linadi")
#             bolinuvchilar.append(boluvchi)
#         else:
#             print(f"{son} soni {boluvchi}ga bo'linmaydi")
    
#     return bolinuvchilar

# # Asosiy dastur
# son = int(input("Sonni kiriting: "))
# natija = tekshir_bolinish(son)
# print(f"\n{son} soni quyidagi sonlarga qoldiqsiz bo'linadi: {natija}")     



from datetime import datetime
def mijoz_info(ism,familiya,t_yil,t_joy,tel=None,email=None):
    """Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
    email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida 
    qaytaruvchi funksiya"""
    
    hozirgi_yil = datetime.now().year
    yosh = hozirgi_yil - t_yil
    
    info = {
        'ism':ism,
        'familiya':familiya,
        'tugil_yil':t_yil,
        'tugil_joy':t_joy,
        'telefon':tel,
        'email':email,
        #'yoshi':yosh
        }
    
    return info
    
mijozlar = []
while True:
# ---------- FOYDALANUVCHIDAN MA'LUMOT OLISH ----------
    ism = input("Ismingizni kiriting :")
    familiya = input("Familiyangizni kiriting :")
    tugil_yil = int(input("Tug'ilgan yilingizni kiriting :"))
    tugil_joy = input("Tug'ilgan joyingizni kiriting :")    
    telefon = input("Telefon raqamingizni kiriting :") or None
    email = input("Emailingizni kiriting :") or None
    #yosh = input("Yoshingizni kiriting :") or None
# -------- FUNKSIYANI CHAQIRISH VA LISTGA QO'SHISH -----------
    malumot = mijoz_info(ism, familiya, tugil_yil, tugil_joy,telefon,email)
    mijozlar.append(malumot)

    
#------------ TSIKL TO'XTATISH SHARTI -------------
    javob = input("Davom ettirasizmi ?(ha/yoq)")
    if javob!= "ha":
        break

#------------- MIJOZLARNI CONSOLE GA CHIQARISH ---------
for mijoz in mijozlar:
    print(f"Foydalanuvchi {mijoz['ism'].title()} {mijoz['familiya'].title()},{mijoz['tugil_yil']}-yil,"
         f"{mijoz['tugil_joy'].title()} da tug'ilgan, telefoni: {mijoz['telefon']}")


       

        
    
    
        




    
    




































