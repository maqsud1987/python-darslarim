# def summa(*sonlar):
#     """Kiritilgan sonning yig'indisini hisoblovchi funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi

# print(summa(1,2))
# print(summa(1,2,3,4,5))


# ------- yuqoridagini qisqaroq yozsak --------
# def summa(*sonlar):
#     return sum(sonlar)
# print(summa(1,2))
# print(summa(1,2,3,4,5))



# def summa(x,y,*sonlar):
#     return x+y+sum(sonlar)
# print(summa(1,2))
# print(summa(1,2,3,4,5))



# def yigindi_kv(a,b):
#     return (a+b)**2
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))

# print("Yig'indining kvadrati:", yigindi_kv(a, b))





# def talaba_info(ism,familiya,**malumot):
#     talabalar = {}
#     talabalar['ism']=ism
#     talabalar['familiya']=familiya
#     talabalar['yosh']=32
#     return talabalar
# talaba1 = talaba_info('ali', 'sobirov',yosh=32)
# print(talaba1) 


def talaba_info(ism, familiya, **malumot):
    malumot['ism'] = ism
    malumot['familiya'] = familiya
    return malumot

talaba = talaba_info(
    'olim', 'olimov',
    tyil=1995,
    fakultet='IT',
    yonalish='AT'
)
print(talaba)















        
        