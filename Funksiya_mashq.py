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
import tkinter as tk
from tkinter import messagebox

def son_daraja_top():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        natija = f"{a} ning {b}-darajasi, {a**b} ga teng"
        label_natija.config(text=natija)
    except ValueError:
        messagebox.showerror("Xatolik", "Iltimos, son kiriting!")

# Asosiy oynani yaratish
root = tk.Tk()
root.title("Sonning darajasini topish")
root.geometry("400x200")

# Kirish uchun entry va label
label_a = tk.Label(root, text="Sonni kiriting:")
label_a.pack(pady=5)
entry_a = tk.Entry(root)
entry_a.pack(pady=5)

label_b = tk.Label(root, text="Qanday darajaga ko'tarmoqchis:")
label_b.pack(pady=5)
entry_b = tk.Entry(root)
entry_b.pack(pady=5)

# Hisoblash tugmasi
btn_hisobla = tk.Button(root, text="Hisoblash", command=son_daraja_top)
btn_hisobla.pack(pady=10)

# Natija ko‘rsatiladigan label
label_natija = tk.Label(root, text="", font=("Arial", 12))
label_natija.pack(pady=10)

# Oynani ishga tushirish
root.mainloop()


        




    
    




































