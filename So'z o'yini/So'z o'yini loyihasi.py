from uzwords import words
import random

# tasodifiy so'z tanlash
soz = random.choice(words)

# ekranda ko'rinadigan chiziqlar
displey = []
for _ in range(len(soz)):
    displey.append("_")
while "_" in displey:
    harf = input("Harfni kiriting: ")
    # so'z uzunligi bo'yicha yuramiz
    for i in range(len(soz)):
        if soz[i] == harf:
            displey[i] = harf
            
        # displeyni chiqarish
    for belgi in displey:
        print(belgi, end=" ")
    print()
            

    
   
    




