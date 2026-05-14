# # 🟡 1 - JSON faylni yuklab,har bir talaba haqida ma'lumot berish
# import json

# with open("students.json","r")  as file:
#     students = json.load(file)
    
# # print(students)


# for student in students['students']:
#     print(f"{student['ism']} {student['familiya']},{student['kurs']}-kurs,"
#           f"{student['fakultet']} fakulteti talabasi.")
    

# # 🟡 2 - JSON fayl 
import json
with open("maqola.json","r") as file:
    essay = json.load(file)
    
#print(essay)

sarlavha =(essay['query']['pages']['13801']['title'])
qisqa_matn =(essay['query']['pages']['13801']['extract']) 

# print(sarlavha) 
# print(qisqa_matn)

print(f"Sarlavha: {sarlavha} \nQisqacha ma'lumot: {qisqa_matn}")