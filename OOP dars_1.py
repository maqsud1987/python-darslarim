# ================== Foydalanuvchi uchun web sahifa ====================

# class User:
#     def __init__(self,ism,familiya,telefon,email = ""):
#         self.ism = ism
#         self.familiya = familiya
#         self.tel = telefon
#         self.email = email
#     def get_info(self):
#         return f"Foydalanuvchi:ismi {self.ism},familiyasi {self.familiya},telefon {self.tel} "
        
# foydalanuvchi1 = User("Ali","Salimov",77777)
# print(foydalanuvchi1.ism)
# print(foydalanuvchi1.get_info())

# ==================== Kitoblar kutubxonasi ============================

class book:
    def __init__(self,kitob_nomi,muallif,nashr_yili,sahifa_soni):
        self.kitob_nomi = kitob_nomi
        self.muallif = muallif
        self.nashr_yili = nashr_yili
        self.sahifa_soni = sahifa_soni
        
    def get_info(self):
        return (f"Kitob: {self.kitob_nomi},"
                f"Muallif: {self.muallif},"
                f" Yili: {self.nashr_yili},"
                f"Sahifalari:{self.sahifa_soni}" )
       
        
        
book1 = book(f'Sherlok Xolms', "Arthur Conan Doyle", 1892, 307)
book2 = book("O'tgan kunlar ", "Abdullo Qodiriy", 1926, 383)
print(book1.get_info())
print(book2.get_info())


        


    
   
    




