class Fan:
    def __init__(self,name):
        self.name =name
        
        
class Shaxs:
    def __init__(self,ism,yosh):
        self.ism = ism
        self.yosh = yosh
        

class Talaba(Shaxs):
    def __init__(self,ism,yosh,familiya):
        super().__init__(ism,yosh) 
        
        self.familiya = familiya
        self.fanlar = []
        
    def get_info(self):
        return f"Talaba: {self.ism} {self.familiya}, {self.yosh} - yoshda"
 
    def fanga_yozil(self,fan):
        self.fanlar.append(fan)
        
        
    def remove_fan(self,fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else: 
            print("Siz bu fanga yozilmagansiz")
            
            
class Professor(Shaxs):
     def __init__(self,ism,yosh,fan):
         super().__init__(ism, yosh)
         self.fan = fan
         
    
    
            
fan1 = Fan("Fizika")
fan2 = Fan("Matematika")

talaba = Talaba("Ali", 20, "Salimov")

talaba.fanga_yozil(fan1)
talaba.fanga_yozil(fan2)

print(talaba.get_info())

talaba.remove_fan(fan1)

# ==========================================
# 1-QISM: FAN KLASSI
# ==========================================
class Fan:
    def __init__(self, name):
        self.name = name  # Fanning nomi: "Fizika", "Matematika"

#Fan klassidan obyektlar:
fan1 = Fan("Fizika")
#fan1.name → "Fizika"
print(fan1.name)


# ==========================================
# 2-QISM: SHAXS KLASSI (Asosiy/Ota klass)
# ==========================================
class Shaxs:
    def __init__(self, ism, yosh):
        self.ism = ism    # Har qanday insonning ismi
        self.yosh = yosh  # Har qanday insonning yoshi

# Shaxs klassidan obyekt:
# shaxs1 = Shaxs("Ali", 20)
# shaxs1.ism → "Ali"
# shaxs1.yosh → 20


# ==========================================
# 3-QISM: TALABA KLASSI (Shaxsdan meros oldi)
# ==========================================
class Talaba(Shaxs):  # (Shaxs) → Shaxsning barcha xususiyatlarini oldi

    def __init__(self, ism, yosh, familiya):
        super().__init__(ism, yosh)  # ism, yoshni Shaxsga yubordi — Shaxs saqlaydi
        self.familiya = familiya     # Faqat Talabaga xos — Shaxsda yo'q
        self.fanlar = []             # Faqat Talabaga xos — bo'sh ro'yxat

    # Talaba haqida ma'lumot chiqaradi
    def get_info(self):
        return f"Talaba: {self.ism} {self.familiya}, {self.yosh} - yoshda"

    # Talabani fanga yozadi
    def fanga_yozil(self, fan):
        self.fanlar.append(fan)  # Fan obyektini ro'yxatga qo'shadi

    # Talabani fandan chiqaradi
    def remove_fan(self, fan):
        if fan in self.fanlar:       # Agar fan ro'yxatda bor bo'lsa
            self.fanlar.remove(fan)  # O'chirib tashlaydi
        else:
            print("Siz bu fanga yozilmagansiz")  # Yo'q bo'lsa xabar beradi


# ==========================================
# 4-QISM: PROFESSOR KLASSI (Shaxsdan meros oldi)
# ==========================================
class Professor(Shaxs):  # (Shaxs) → Shaxsning barcha xususiyatlarini oldi

    def __init__(self, ism, yosh, fan):
        super().__init__(ism, yosh)  # ism, yoshni Shaxsga yubordi
        self.fan = fan  # Faqat Professorga xos — qaysi fanni o'qitadi


# ==========================================
# 5-QISM: UMUMIY MANZARA
# ==========================================

#         SHAXS (ism, yosh)
#        /                \
#   TALABA                PROFESSOR
#   (familiya,            (fan)
#    fanlar[])


         

































            