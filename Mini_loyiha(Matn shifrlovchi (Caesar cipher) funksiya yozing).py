# ============ Matn shifrlovchi (Caesar cipher) funksiya yozing =============

# ============ Matn shifrlovchi (Caesar cipher) funksiya yozing =============

def caesar_cipher(matn, qadam):
    shifrlangan = ""

    for harf in matn:
        if harf.isupper():
            yangi_harf = chr((ord(harf) - ord('A') + qadam) % 26 + ord('A'))
            shifrlangan += yangi_harf

        elif harf.islower():
            yangi_harf = chr((ord(harf) - ord('a') + qadam) % 26 + ord('a'))
            shifrlangan += yangi_harf

        else:
            shifrlangan += harf

    return shifrlangan


# foydalanuvchidan ma'lumot olish
matn = input("Matn kiriting: ")
qadam = int(input("Qadamni kiriting: "))

natija = caesar_cipher(matn, qadam)

print("Shifrlangan matn:", natija)
        

    


    
    