# =============== Talaba bahosini hisoblovchi funksiya yozing =================
print("========== Talabani baholash ============")
def talaba_bahosi(b1, b2, b3):
    orta = (b1 + b2 + b3) / 3
    return orta

while True:
    
    ism = input("Ismingizni kiriting: ")
    b1=int(input("1-fan bahosini kiriting: "))
    b2=int(input("2-fan bahosini kiriting: "))
    b3=int(input("3-fan bahosini kiriting: "))
    ortacha = talaba_bahosi(b1,b2,b3)
    print(f"{ism.title()}ning ortacha bahosi {ortacha} ")
    chiqish=input("To'xtatish uchun 'stop' yozing >>>")
    if chiqish=="stop":
        print("Dastur to'xtamoqda.....")
        break