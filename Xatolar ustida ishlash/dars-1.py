# Xatolar ustida ishlash

# #1 🟢 ZeroDivisionError va ValueError

# x= input("Birinchi sonni kiriting: ")
# y= input("Ikkinchi sonni kiriting: ")
# try:
#     x=int(x)
#     y=int(y)
#     z=x/y
# except ZeroDivisionError:
#     print("0 ga bo'lish mumkin emas !")
    
# except ValueError:
#     print("Siz noto'g'ri qiymat kiritdingiz")
# else:
#     print(z)
    
# #2 🔴  ValueError va  IndexError

# talabalar = ["Ali", "Vali", "Salim", "Hamid", "Zafar"]
# son = input("Iltimos son kiriting: ")

# try:
#     son = int(son)
#     talaba = talabalar[son]
    
# except ValueError:
#     print("Son kiriting ")
    
# except IndexError:
#     print("Bunday talaba yo'q")
    
# else: 
#     print(talaba)


# #3 🟡 ValueError va  IndexError

# ism = input("Talabaning ismini kiriting: ")
# baho = input("Bahosini kiriting: ")

# try:
#     baho = int(baho)
#     if baho==5:
#         print(f"{ism} -A'lo ! ")
#     elif baho==4:
#         print(f"{ism} - Yaxshi!")
#     elif baho==3:
#         print(f"{ism} - Qoniqarli!")
#     elif baho==2:
#          print(f"{ism} - Qoniqarsiz!")
#     else:
#         print("2 dan 5 gacha son qiymat kiriting")    
         
# except ValueError:
#     print("faqat son kiriting")
    


    


































    