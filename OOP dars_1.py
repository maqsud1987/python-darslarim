class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.t_yil = tyil
    def yosh(self,joriy_yil):
        return joriy_yil - self.t_yil
    def tanishtir(self):
        return f"Ismim {self.ism},familiyam {self.familiya},{self.t_yil} ta tug'ilganman"
talaba1=Talaba("Salim","Olimov",1987)
talaba2=Talaba("Olim","Salimov",2009)
talaba3=Talaba("Halim","Karimov",1995)


    
   
    




