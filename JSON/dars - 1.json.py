import json

# 🔵 1 - pythondagi lug'atni jsonga str ga o'tkazish  

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}

data_json = json.dumps(data)      #🔶 Lug'at → String
#print(data_json)


# 🟢 2 - json formatdan ➤ Python lug'at ➤ talaba ism,familiyasini chiqarish 

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba = json.loads(talaba_json)   #🔶 String → Lug'at
#print(talaba["ism"])
#print(talaba["familiya"])


# 🟡 3 - Yuqoridagi 1- va 2 - o'zgaruvchilarni JSON faylga saqlash  

with open('data_1.json','w') as f:
    json.dump(data,f)              #🔶 Lug'at → Fayl
    
with open("talaba_1.json","w") as f:
    json.dump(talaba,f)
    




    