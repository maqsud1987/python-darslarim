class Fan:
    def __init__(self,fan_nomi):
        self.fan_nomi = fan_nomi
        self.talabalar = []
        
    def add_student(self,talaba):
        self.talabalar.append(talaba)
        
    def __len__(self):
        return len(self.talabalar)
        
class Talaba:
    def __init__(self,id,ism):
        self.id = id
        self.ism = ism
        
        
class Talaba:
    def __init__(self, id, ism):
        self.id = id        # Talabaning ID raqami
        self.ism = ism      # Talabaning ismi

    def __repr__(self):
        # Talaba obyektini chiroyli ko'rsatish uchun
        return f"Talaba(id={self.id}, ism={self.ism})"


class Fan:
    def __init__(self, fan_nomi):
        self.fan_nomi = fan_nomi  # Fanning nomi
        self.talabalar = []       # Talabalar ro'yxati (bo'sh boshlanadi)

    # --- Talaba qo'shish ---
    def add_student(self, talaba):
        """Oddiy usul bilan talaba qo'shish"""
        self.talabalar.append(talaba)

    def __add__(self, talaba):
        """+ operatori bilan talaba qo'shish
        Misol: fizika + talaba1
        """
        self.talabalar.append(talaba)
        return self  # o'zini qaytaradi, zanjir bo'lsin deb

    # --- Talaba olib tashlash ---
    def __sub__(self, talaba_id):
        """- operatori bilan ID bo'yicha talabani olib tashlash
        Misol: fizika - 101
        """
        # ID bo'yicha talabani qidiradi va olib tashlaydi
        self.talabalar = [t for t in self.talabalar if t.id != talaba_id]
        return self  # o'zini qaytaradi

    # --- Indeks bo'yicha olish ---
    def __getitem__(self, indeks):
        """Indeks bo'yicha talabani olish
        Misol: fizika[0] → birinchi talaba
        """
        return self.talabalar[indeks]

    # --- Indeks bo'yicha o'zgartirish ---
    def __setitem__(self, indeks, talaba):
        """Indeks bo'yicha talabani almashtirish
        Misol: fizika[0] = yangi_talaba
        """
        self.talabalar[indeks] = talaba

    # --- Uzunlik ---
    def __len__(self):
        """Talabalar sonini qaytaradi
        Misol: len(fizika) → 3
        """
        return len(self.talabalar)

    # --- Chaqiriladigan qilish ---
    def __call__(self, talaba=None):
        """Fan obyektini funksiya kabi chaqirish imkonini beradi.
        - Agar talaba berilsa → uni qo'shadi
        - Agar berilmasa → barcha talabalar ro'yxatini chop etadi
        Misol: fizika()         → ro'yxat ko'rsatadi
               fizika(talaba1)  → talaba qo'shadi
        """
        if talaba is None:
            print(f"\n{self.fan_nomi} fani talabalari ({len(self)} nafar):")
            for i, t in enumerate(self.talabalar, 1):
                print(f"  {i}. {t.ism} (ID: {t.id})")
        else:
            self.add_student(talaba)
            print(f"{talaba.ism} → {self.fan_nomi} faniga qo'shildi!")

    def __repr__(self):
        return f"Fan('{self.fan_nomi}', talabalar soni={len(self)})"


# ===================== SINAB KO'RISH =====================

# Talabalar yaratish
talaba1 = Talaba(id=101, ism="Ali Valiyev")
talaba2 = Talaba(id=102, ism="Zulfiya Karimova")
talaba3 = Talaba(id=103, ism="Bobur Toshmatov")
talaba4 = Talaba(id=104, ism="Malika Yusupova")

# Fan yaratish
fizika = Fan("Fizika")

# 1) add_student() bilan qo'shish
fizika.add_student(talaba1)
print("add_student() bilan qo'shildi:", fizika)

# 2) + operatori bilan qo'shish
fizika + talaba2
fizika + talaba3
print("+ operatori bilan qo'shildi:", fizika)

# 3) __call__ orqali qo'shish (talaba bilan)
fizika(talaba4)

# 4) len() - talabalar soni
print(f"\nJami talabalar: {len(fizika)}")

# 5) __getitem__ - indeks bo'yicha olish
print(f"Birinchi talaba: {fizika[0]}")

# 6) __setitem__ - almashtirish
yangi_talaba = Talaba(id=105, ism="Sardor Nazarov")
fizika[0] = yangi_talaba
print(f"0-indeks almashtirildi. Yangi talaba: {fizika[0]}")

# 7) __call__ (talabasiz) - ro'yxat ko'rsatish
fizika()

# 8) - operatori bilan olib tashlash (ID bo'yicha)
fizika - 102  # Zulfiya olib tashlandi
print("\n102-ID olib tashlangandan keyin:")
fizika()        