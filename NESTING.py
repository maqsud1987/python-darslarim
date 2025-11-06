# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13000,
#         'km':50000,
#         'korobka':'avtomat'
#         }

# car1 = {
#         'model':'nexia 3',
#         'rang':'qora',
#         'yil':2015,
#         'narh':9000,
#         'km':89000,
#         'korobka':'mexanika'
#         }

# car2 = {
#         'model':'gentra',
#         'rang':'qizil',
#         'yil':2019,
#         'narh':15000,
#         'km':20000,
#         'korobka':'mexanika'
#         }
# cars = [car0,car1,car2]
# for car in cars:
    # print(f"{car['model'].title()}",
    #       f"{car['rang']} rang",
    #       f"{car['yil']} yil",
    #       f"{car['narh']} $",
    #                 )
    
# print(f"{cars[1]['model']},"
#       f" probeg:{cars[1]['km']} km"
#       )


# malibus = []
# for n in range(10):
#     new_car = {
#             'model':'malibu',
#             'rang':None,   # rangi noaniq
#             'yil':2025,
#             'narh':None,   #narh noaniq
#             'km':0,
#             'korobka':'avto'
#             }
#     malibus.append(new_car)

# for malibu in malibus[:3]:
#     malibu['rang'] = 'qizil'
    
# for malibu in malibus[3:6]:
#     malibu['rang'] = 'qora'
    
# for malibu in malibus[6:]:
#     malibu['rang'] = 'qora'
#     malibu['korobka'] = 'mexanika'
    
# for malibu in malibus:
#     if malibu['korobka'] == 'avto':
#         malibu['narh'] = 40000 
#     else:
#         malibu['narh'] = 38000
        
# for malibu in malibus:
#     print(malibu)

# dasturchilar = {
#     'ali' : ['python','c++'],
#     'vali':['js','css'],
#     'tohir':['html','css'],
#     'zokr':['word','exel']
#     }
# for ism,tillar in dasturchilar.items():
#     print(f"{ism.title()} quyidagu dasturlarni biladi")
#     for til in tillar:
#         print(f"{til.upper()} ", end = '')

# abituriyentlar = []
# for n in range(8):
#     new_abituriyent = {
#         'yosh':None,
     
#         'fan':None,
#         't_yil':None
#         }
#     abituriyentlar.append(new_abituriyent)
# for abituriyent in abituriyentlar[:3]:
#     abituriyent['yosh']=18
    
# for abituriyent in abituriyentlar[3:6]:
#     abituriyent['yosh']=17
    
# for abituriyent in abituriyentlar[6:]:
#     abituriyent['yosh']=20

# for abituriyent in abituriyentlar:
#     abituriyent['fan']='fizika'
    
# for abituriyent in abituriyentlar[:4]:
#     abituriyent['t_yil']=2009
    
# for abituriyent in abituriyentlar[4:]:
#     abituriyent['t_yil']=2008
    
    
# for abituriyent in abituriyentlar:
#     print(abituriyent)

# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['js','css'],
#     'olim':['sql','c#'],
#     'husan':['html','c++']
#     }

# for ism,tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlarni tillarini biladi :", end = '')
#     for til in tillar:
#         print(f"{til.upper()}",end= " ")

# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro',
           
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
#     print(f"{shaxs['ism']}",
#           f"{shaxs['tyil'] } - yilda tug'ilib',",
#           f"{shaxs['vyil']} - yilda ",
#           f"{shaxs['tjoy']}da vafot etdi.",
              
#           )


# kinolar = {
#     'ali':['Terminator','Rambo','Titanic'],
#     'vali':['Tenet','Inception','Interstellar'],
#     'hasan':['Abdullajon','Bomba','Shaytanat'],
#     'husan':['Mahallada duv-duv gap','John Wick']
#     }

# for ism,kinolar in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari :")
    
#     for kino in kinolar:
#          print(kino)

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
#     if davlat.lower()=='aqsh':
#         davlat = davlat.upper()
#     else:
#         davlat = davlat.capitalize()
#     print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")
    


    
    

    
   
    
    
    

   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
                  
          
    
        


    





        
        

    

    
    
    




