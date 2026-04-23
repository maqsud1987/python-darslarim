#1 - qism - Shaxs klassi
class Shaxs:
    odamlar_soni = 0
    def __init__(self,ism,familiya,yosh,telefon):
        self.ism = ism
        self.familiya = familiya
        
        self.__yosh = yosh
        self.set_tel(telefon)
        
        self.__telefon = telefon
        Shaxs.odamlar_soni +=1
        
    def get_yosh(self):
        return  f"Shaxsning yoshi {self.__yosh} da"
    
    def set_yosh(self,yangi_yosh):
        if 0<yangi_yosh <= 120:
            self.__yosh = yangi_yosh
        else:
            print("Xato: yosh musbat va 1 dan 120 gacha bo'lishi kerak")
            
    def get_tel(self):
        return  f"Shaxsning telefoni: {self.__telefon} "
            
    def set_tel(self,yangi_tel):
        if yangi_tel.startswith("+"):
            self.__telefon = yangi_tel
        else:
            print("Xato: raqamlar oldida '+' qo'yilmadi ")
            
    @classmethod
    def get_odamlar_soni(cls):
        return cls.odamlar_soni
    
    
    
# 2-qism — Talaba klassi

class Talaba(Shaxs):
    talabalar_soni = 0
    def __init__(self,ism,familiya,yosh,telefon,guruh):
        super().__init__(ism, familiya, yosh,telefon)
        self.__guruh = guruh
        self.set_tel(telefon)
        Talaba.talabalar_soni +=1
        
    def get_guruh(self):
        return f"Guruh nomi: {self.__guruh} "
    
    def set_guruh(self,yangi_guruh):
        if len(yangi_guruh)>0:
            self.__guruh = yangi_guruh 
        else:
            print("Xato: Guruh nomi bo'sh bo'lmasin")
            
    @classmethod
    def get_talabalar_soni(cls):
        return cls.talabalar_soni
    
odam1 = Shaxs("Ali", "Salimov", 27,"+998997002087")
odam2 = Shaxs("Salim", "Halimov", 35, "+998973002030")
odam3 = Shaxs("Said", "Akbarov", 40, "+998941282087") 

print(odam1.get_yosh())
print(odam1.get_tel())


t1 = Talaba("Jasur", "Toshmatov", 20, "+998901234567", "CS-101")
print(t1.get_guruh())
print(t1.get_yosh())
print(f"Talabalar soni: {Talaba.get_talabalar_soni()} ta" )

   



























            