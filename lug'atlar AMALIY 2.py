# talaba = {
#     'ism':{'yosh':22,
#            'til':['python','css'],
#            'kasb':'IT'}}
# #print(talaba['ism']['til'][0])
# for til in talaba['ism']['til']:
#     print(til.upper())


#---- TARIXIY SHAXSLAR ----------
# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro'
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent'
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona"
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot"
#            }
# shaxslar = [buxoriy,qodiriy,vohidov,navoiy]
# for shaxs in shaxslar:
#     print(f"{shaxs['ism']} {shaxs['tyil']}-yilda {shaxs['tjoy']}da tug'ilgan " ""
#           f"{shaxs['vyil']}da vafot etgan.")
    
    
#----- TARIXIY SHAXSLARNING ASARLARINI HAM QO'SHISH -------

# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro',
#            'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent',
#            'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona",
#            'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot",
#            'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
#            }

# shaxslar = [buxoriy,qodiriy,vohidov,navoiy]
# for shaxs in shaxslar:
#     print(f"{shaxs['ism'].title()}ning asarlari: {shaxs['asarlar']}")

#------------ DAVLATLAR HAQIDA MA'LUMOT ------------
# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }

# for davlat, info in davlatlar.items():
#     print(f"\n{davlat.title()}:")
#     for kalit, qiymat in info.items():
#         print(f"  {kalit.title()}: {qiymat}")

#---- YUQORIDAGI DASTURNI FOYDALANUVCHI SO'RAGAN DAVLATNI CHIQARISH ---

davlatlar = {
    "o'zbekiston":{'davlat_nomi':"o'zbekiston",
                   'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'davlat_nomi':"rossiya",
                   'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{       'davlat_nomi':"aqsh",
                   'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{  'davlat_nomi':"malayziya",
                   'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }


davlat_nomi = input("Davlat nomini kiriting : ").lower()
info = davlatlar.get(davlat_nomi,"Bunday davlat yo'q")
for kalit,qiymat in info.items():
    print(f"{kalit.title()}:{qiymat}")




    
    
    
    
    
    
    
    
    
    
    
    
    