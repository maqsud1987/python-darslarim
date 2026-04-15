# Book klassini yaratdik — kitob uchun qolip
class Book:
    
    # Kitob yaratilganda 3 ta ma'lumot oladi
    def __init__(self, nomi, muallif, yil):
        self.nomi = nomi        # bu kitobning nomi
        self.muallif = muallif  # bu kitobning muallifi
        self.yil = yil          # bu kitobning yili

    # Kitob haqida chiroyli matn qaytaradi
    def get_info(self):
        return f"{self.nomi} - {self.muallif}, {self.yil}"


# User klassini yaratdik — foydalanuvchi uchun qolip
class User:
    
    # Foydalanuvchi yaratilganda faqat ismi oladi
    def __init__(self, ism):
        self.ism = ism        # foydalanuvchi ismi
        self.kitoblar = []    # bo'sh ro'yxat — hali kitob yo'q

    # Ro'yxatga kitob qo'shadi
    def add_book(self, kitob):
        self.kitoblar.append(kitob)  # book obyektini ro'yxatga qo'shadi

    # Barcha kitoblarni ekranga chiqaradi
    def show_books(self):
        for book in self.kitoblar:      # har bir kitobni aylanib chiqadi
            print(book.get_info())      # har birining ma'lumotini chiqaradi


# 3 ta kitob obyekti yaratdik
kitob1 = Book("O'tkan kunlar", "Abdulla Qodiriy", 1926)
kitob2 = Book("Kecha va Kunduz", "Cho'lpon", 1936)
kitob3 = Book("Shum bola", "G'afur G'ulom", 1936)

# Ali ismli foydalanuvchi yaratdik
shaxs = User("Ali")

# Alining ro'yxatiga kitoblarni qo'shdik
shaxs.add_book(kitob1)
shaxs.add_book(kitob2)
shaxs.add_book(kitob3)

# Alining barcha kitoblarini ekranga chiqardik
shaxs.show_books()






































     