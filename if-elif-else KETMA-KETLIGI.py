from gtts import gTTS

matn = """
Python'dagi .get() metodi lug‘atdan ma’lumotni xavfsiz olish uchun ishlatiladi.
Agar kalit bo‘lmasa, xato chiqarmaydi, balki None yoki o‘zing bergan matnni qaytaradi.
Masalan: talaba.get("manzil", "Ma’lumot topilmadi")
.get() majburiy emas, lekin xatolardan saqlaydi va kodni soddalashtiradi.
"""

# Ovoz yaratish (til: o‘zbekcha)
ovoz = gTTS(text=matn, lang='uz', slow=False)
ovoz.save("get_metodi_tushuntirish.mp3")