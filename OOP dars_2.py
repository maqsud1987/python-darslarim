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

        
print(talaba1.get_info())

talaba1.update_bosqich()

print(talaba1.get_info())

talaba1.update_bosqich()

print(talaba1.get_info())

    
   
    




