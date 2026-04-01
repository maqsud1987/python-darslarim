import random as r
son = r.randint(1,10)

#1-qism

print("Keling o'ylangan sonni topish o'yinini o'ynaymiz !")
print("1 dan 10 gacha son o'yladim.Topa olasizmi :\n ")

def son_top(son):
    urinish=0
    while True:
        urinish +=1
        taxmin = int(input("Men o'ylagan sonni toping : "))
        if taxmin > son:
            print("Xato,men o'ylagan son bundan kichikroq.Yana harakat qilib ko'ring :")
        elif taxmin < son:
           print("Men o'ylagan son bundan kichik emas, kattaroq son kiriting")
        elif taxmin==son:
            print(f"TOPDINGIZ! Men {son} sonini o'ylagan edim.",end = "")
            print(f"Siz {urinish} ta urinishda topdingiz.\n")
            break
son_top(son)

#2-qism
past = 1
yuqori = 10

print("Endi siz 1 dan 10 gacha son o'ylang.Men topishga harakat qilaman.")

def son_top_AI(past,yuqori):
    urinish=0
    while True:
        urinish +=1
        tavakkal = (past + yuqori) // 2
        javob = input(f"Menimcha son {tavakkal},to'g'ri bo'lsa (T)," \
              f"men o'ylagan son bundan katta bo'lsa (+),yoki kichik bo'lsa (-):  ")
        if javob=="T":
            print(f"Topildi {urinish} urinishda ")
            break
        elif javob == "+":
            print("Demak son kattaroq,yangi taxmin >>>")
            past = tavakkal + 1
            
        elif javob == "-":
            print("Demak son kichikroq,yangi taxmin >>>")
            yuqori = tavakkal - 1
            
son_top_AI(past,yuqori)

            
            
            
        
        



