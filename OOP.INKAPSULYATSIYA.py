from uuid import uuid4
class Talaba:
    talabalar_soni = 0
    def __init__(self,ism,familiya,yosh):
        self.ism = ism
        self.familiya=familiya
        self.__yosh = yosh
        
        Talaba.talabalar_soni +=1
        
    def get_yosh(self):
        return f"Talabaning yoshi {self.__yosh} da"
    
    def set_yosh(self,yangi_yosh):
        if 0<yangi_yosh <= 120:
            self.__yosh = yangi_yosh
        else:
            print("Xato: yosh musbat va 1 dan 120 gacha bo'lishi kerak")
    @classmethod
    def get_talabalar_soni(cls):
        return cls.talabalar_soni

talaba1 = Talaba("Ali", "Valiyev", 18)
talaba2 = Talaba("Hasan", "Karimov", 20)
talaba3 = Talaba("Dilshod", "Tursunov", 19)

print("Jami talabalar soni:", Talaba.get_talabalar_soni())

print(talaba1.get_yosh())
print(talaba2.get_yosh())


talaba1.set_yosh(22)
print(talaba1.get_yosh())



# class Talaba:
#     # 📊 Klassga oid xususiyat: umumiy talabalar soni
#     talabalar_soni = 0

#     def __init__(self, ism, familiya, yosh):
#         # 👤 Obyekt xususiyatlari
#         self.ism = ism
#         self.familiya = familiya
#         self.__yosh = yosh  # 🔒 private (tashqaridan to‘g‘ridan-to‘g‘ri kira olmaysan)

#         # ➕ Har yangi talaba yaratilganda umumiy son oshadi
#         Talaba.talabalar_soni += 1

#         # 🖨️ Yangi talaba yaratilganini chiqaramiz
#         print(f"✅ Yangi talaba qo‘shildi: {self.ism} {self.familiya}")

#     # 🔍 Yoshni ko‘rish (getter)
#     def get_yosh(self):
#         return f"{self.ism} {self.familiya} yoshi: {self.__yosh}"

#     # ✏️ Yoshni o‘zgartirish (setter)
#     def set_yosh(self, yangi_yosh):
#         if 0 < yangi_yosh <= 120:
#             self.__yosh = yangi_yosh
#             print(f"🔄 Yosh yangilandi: {self.__yosh}")
#         else:
#             print("❌ Xato: yosh 1 dan 120 gacha bo‘lishi kerak")

#     # 📊 Klass metodi: umumiy talabalar sonini qaytaradi
#     @classmethod
#     def get_talabalar_soni(cls):
#         return cls.talabalar_soni
    
# # 🧑‍🎓 Talabalar yaratamiz
# t1 = Talaba("Ali", "Valiyev", 18)
# t2 = Talaba("Hasan", "Karimov", 20)
# t3 = Talaba("Dilshod", "Tursunov", 19)

# print("\n----------------------------\n")

# # 📊 Jami talabalar soni
# print("📊 Jami talabalar soni:", Talaba.get_talabalar_soni())

# print("\n----------------------------\n")

# # 👤 Talabalar yoshini ko‘rish
# print(t1.get_yosh())
# print(t2.get_yosh())
# print(t3.get_yosh())

# print("\n----------------------------\n")

# # ✏️ Yoshni o‘zgartirish
# t1.set_yosh(22)
# print(t1.get_yosh())

# print("\n----------------------------\n")

# # ❌ Xato test (inkapsulyatsiya ishlashi)
# t2.set_yosh(200)






































