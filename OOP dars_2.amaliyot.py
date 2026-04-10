class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
        self.bosqich = 1
        
    def get_info(self):
        return f"{self.ism} {self.familiya}.{self.bosqich}-bosqich talabasi"
    
    def get_name(self): 
        return self.ism
    
    def get_lastname(self):
        return self.familiya
    
    def set_bosqich(self,bosqich):
        self.bosqich=bosqich
        
           
    def update_bosqich(self):
        self.bosqich+=1
       
        
    
talaba1 = Talaba("Ali", "Valiyev", 2000)        
talaba2 = Talaba("Vali", "Aliyev", 2005)

        
# print(talaba1.get_info())

# talaba1.update_bosqich()
# print(talaba1.get_info())

# talaba1.update_bosqich()
# print(talaba1.get_info())


class Fan:
    
    def __init__(self,fan_nomi):
                
        self.fan_nomi = fan_nomi
        self.talabalar_soni = 0
        self.talabalar = []
        
        
    def add_student(self,talaba):
        # Fan ga talabalar qo'shish 
        self.talabalar.append(talaba)
        self.talabalar_soni +=1
        
    def get_name(self):  # Fan nomi
        return self.fan_nomi
    
    def get_students(self): # Fanga yozilgan talabalar ma'lumoti
        return [talaba.get_name() for talaba in self.talabalar ]
    
matematika = Fan("Oliy matematika")
talaba1 = Talaba("Ali", "Valiyev", 2000)        
talaba2 = Talaba("Vali", "Aliyev", 2005)
talaba3 = Talaba("Eshmat", "Toshmatov", 1985)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

print(matematika.talabalar)
    
        

    
    




























    




