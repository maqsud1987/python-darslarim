class Shaxs:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya=familiya
        self.tyil=tyil
        
    def get_info(self):
        return f"{self.ism} {self.familiya} {self.tyil}-yilda tug'ilgan"
    

class Talaba(Shaxs):
    def __init__(self,ism,familiya,tyil,idraqam,manzil):
        super().__init__(ism,familiya,tyil)
        self.idraqam=idraqam
        self.manzil= manzil
        
    def get_id(self):
        return self.idraqam
    
    def get_info(self):
        return( f"{self.ism} {self.familiya} {self.tyil}-yilda tug'ilgan," 
               f"ID:{self.idraqam}")
    
class Manzil:
    def __init__(self,uy,kocha,tuman,viloyat):
        self.viloyat = viloyat
        self.tuman = tuman
        self.kocha = kocha
        self.uy = uy
              
    def get_manzil(self):
        return( f"{self.viloyat} viloyati,{self.tuman} tumani,"
               f"{self.kocha} kochasi,{self.uy}-uy")
    

        
    
# 🔴 1. Avval manzil yaratamiz
manzil = Manzil(12, "Bog'bon", "Payariq", "Samarqand")

# 🔴 2. Keyin shu manzilni talabaga beramiz
talaba = Talaba("Ali", "Salimov", 1995, 112523, manzil)

# 🔴 3. Endi ichidagi obyektga murojaat qilamiz
print(talaba.get_info())
print(talaba.manzil.get_manzil())







