# ============= Listni teskari qaytaruvchi funksiya yozing ==============
# royxat = [3,4,5]

# def teskari_royxat(royxat):
#     teskari = []
#     for n in range(len(royxat)-1,-1,-1):
#         teskari.append(royxat[n])
#     return teskari
        
# print(teskari_royxat(royxat))    

# # ============ Listdagi takroriy elementlarni olib tashlang =========
# royxat = ["non","choy","sabzi","non","kino","sabzi"]
# def takror_elemenlar(royxat):
#     noyob =[]
#     for element in royxat:
#         if element not in noyob:
#             noyob.append(element)
#     return noyob

# print(takror_elemenlar(royxat))        

# # ============ Listdagi takroriy elementlarni chiqarish =============
# royxat = ["non","choy","sabzi","non","kino","sabzi"]
# def takrorlanuvchisini_ol(royxat):
#     korilganlar = []
#     takrorlanuvchilar = []
#     for element in royxat:
#         if element in korilganlar:
#             if element not in takrorlanuvchilar:
#                  takrorlanuvchilar.append(element)
#         korilganlar.append(element)
#     return takrorlanuvchilar
# print(takrorlanuvchisini_ol(royxat))

# ============ Sonning raqamlari yig‘indisini qaytaring ================
def raqamlar_yigindisi(son):
    son = abs(son)
    yigindi = 0
    while son>0:
        
        raqam = son%10
        yigindi+=raqam
        son = son // 10
    return yigindi

print(raqamlar_yigindisi(-123456789))


def raqamlar_kopaytmasi(son):
    kopaytma = 1
    while son>0:
        raqam=son%10
        kopaytma*=raqam
        son=son//10
    return kopaytma

print(raqamlar_kopaytmasi(1234)) 
        
        
        
    
    



























    
    

    

        
