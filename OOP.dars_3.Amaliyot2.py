class Book:
    def __init__(self,nomi,muallif,yil):
        self.nomi = nomi
        self.muallif = muallif
        self.yil = yil
        
    
    def __repr__(self):
        return self.nomi
        
class User:
    def __init__(self,ism,familiya):
        self.ism = ism
        self.familiya = familiya
        self.books = []
    
class Library:
    def __init__(self):
        self.kitoblar = []
        
    def add_book(self,book):
        self.kitoblar.append(book)

    def borrow_book(self,user,book):
        
        if book in self.kitoblar:
            self.kitoblar.remove(book)
            user.books.append(book)
        else: 
            print("Bizda bu kitob yo'q")
            
# Kitoblar yaratamiz
book1 = Book("Python", "Aliyev", 2020)
book2 = Book("Java", "Karimov", 2019)

# User yaratamiz
user1 = User("Ali", "Valiyev")

# Library yaratamiz
lib = Library()

# Kitoblarni kutubxonaga qo‘shamiz
lib.add_book(book1)
lib.add_book(book2)

print("Kutubxonadagi kitoblar:", lib.kitoblar)

# Kitob olish
lib.borrow_book(user1, book1)

print("\nKitob olingandan keyin:")
print("Kutubxonadagi kitoblar:", lib.kitoblar)
print("Foydalanuvchidagi kitoblar:", user1.books)
            
        
            
       
