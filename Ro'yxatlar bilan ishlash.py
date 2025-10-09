#Ro'yxatlar bilan ishlash

# toq_sonlar = list(range(1,20,2))
# toq_sonlar.sort(reverse=True)
# print(max(toq_sonlar))

# narxlar = [1000,2000,3000,4000,5000]
# arzon = min(narxlar)
# qimmat=max(narxlar) 
# jami = sum(narxlar)
# print(f"Do'konda eng arzon mollar {arzon} so'm narxda,eng qimmat narxlar {qimmat} so'm\nnarxda,jami {jami} so'm so'mlik mol bor")

# cars= ["Tiko","Nexia","Damas","Cobalt","Jiguli"]
# print(cars)
# print(cars[0:3])  #--0,1,2 ni kesib oladi
# print(cars[:3]) # ---0,1,2 kesadi
# print(cars[1:]) # --- 1 dan oxirigaxha nusxa oladi
# print(cars[:])  # --- to'liq nusxa

cars= ["Tiko","Nexia","Damas","Cobalt","Jiguli"]
my_cars = cars # -- bu nusha olish emas ikkalasi bir narsa 
my_cars = cars[:] # -- bu nusha olishda nushasini o'zgartirib boladi asl o'zgarmaydi

# TUPLE - o'zgarmas ro'yxat.Bunda list dumaloq qavs bilan yoziladi

# toys = ('bus','car','bear','dino','snake','lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5]) # -- bu amallarni bajariladi,lekin nusha olish,append orqali qo'shib bo'maydi

#TUPLES >>> LIST ---o'zgartirish uchun LIST ga o'tkazib olishimiz kerak

# toys = ('bus','car','bear','dino','snake','lizard')
# toys = list(toys)
# toys.append("lego")
# print(toys)

# LIST >>> TUPLES #Agar LIST ni TUPLE ga o'tkazsak o'zgarmas ro'yxat bo'ladi

# toys = tuple(toys)
# del toys[0]
# print(toys) # -- bu buyruq bajarilmaydi

# AMALIYOT

# davlatlar = ["Rossiya","Turkiya","Kanada","AQSH","Xitoy","Yaponiya"]
# print(sorted(davlatlar))
# print(sorted(davlatlar, reverse=True))
# print(f"Ro'yxatdagi davlatlar soni {len(davlatlar)} ta")


# j_sonlar = list(range(120,1200,2))
# jami = sum(j_sonlar)
# katta = max(j_sonlar)
# kichik = min(j_sonlar)
# # j_son = list(j_sonlar)
# # j_son = list[0:21]
# print(j_sonlar)
# print(jami)
# print(f"1200 -120 = {katta - kichik}")
# print(f"j_sonlar jadvalida jami {len(j_sonlar)} ta element bor")
# print(j_sonlar[0:20])
# print(j_sonlar[-20:])
# print(j_sonlar[530:550])


# taomlar = ["osh","shirguruch","kasha","chuchvara","manti"]
# nonushta = taomlar[:]
# del nonushta[0]
# del nonushta[3]
# nonushta.remove("chuchvara")
# print(taomlar)
# print(nonushta)






























