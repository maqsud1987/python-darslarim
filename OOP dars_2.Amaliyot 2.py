class Avto:
    def __init__(self,model, rang, karobka, narh):
        self.model=model
        self.rang = rang
        self.karobka = karobka
        self.narh=narh
        self.kilometr = 0
        
    def get_info(self):
        return (f"Model:{self.model},rang:{self.rang},karobka:{self.karobka},"
               f"narh:{self.narh},kilometr:{self.kilometr}")
    
    def update_km(self,kilometr):
        self.kilometr += kilometr
    
    
avto1 = Avto("Cobalt","oq","avtomat",1000)
avto2 = Avto("Spark","delfin","mexanika",8000)
avto3 = Avto("Matiz","oq","mexanika",5000)

class Avtosalon:
    def __init__(self,nomi,manzil):
        self.nomi=nomi
        self.manzil=manzil
        self.avtolar=[]
        
    def add_car(self,avto):
        self.avtolar.append(avto)
        
    def show_cars(self):
        return [avto.get_info() for avto in self.avtolar]
    
    def show_white_cars(self):
        for avto in self.avtolar:
            if avto.rang == "oq":
               print(avto.get_info())
           
salon1 = Avtosalon("GM Salon","Toshkent")  
salon1.add_car(avto1)
    
salon2 = Avtosalon("GM Salon","Buxoro")  
salon2.add_car(avto2)

salon3 = Avtosalon("GM Salon","Samarqand")  
salon3.add_car(avto3)

print(salon1.show_cars())



























    




