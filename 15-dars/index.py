# from ast import NamedExpr


# malibus=[] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
# for n in range(10):
#     new_car = { # har bir yangi mashina uchun lug'at yaratamiz
#         'model':'malibu',
#         'rang':None, # rangi noaniq
#         'yil':2020,
#         'narh':None, # narhi belgilanmagan
#         'km':0,
#         'korobka':'avto'
#         }
#     malibus.append(new_car) # yangi lug'atni ro'yxatga qo'shamiz
#     for malibu in malibus[:3]:
#      malibu['rang']='qizil'
#     for malibu in malibus:
#      print(malibu)
#     for malibu in malibus:
#         malibu["model"]=='malibu'
#         malibu['narx']=12000
#         print(malibu)
# dasturchilar = {
#     'rustam':['c++','html'],
#     'farhod':['js','py','html'],
#     "oybel":['js','py','html','c++']
# }
# for ism, til in dasturchilar.items():
#     print(f"\n {ism.title()} tillarni biladi ")
#     for tillar in til:
#         print (tillar.upper())

          #amalyot
# sh1 = {
#     "ismi":"amir temur",
#     't_yil':1368,
#     'ishi':"ulug' sarkarda"
# }
# sh2 ={
#     'ismi':'alesher navoiy',
#     't_yil':1441,
#     "ishi":"adabiyotga qo'shgan hissasi"
# }
# sh3 ={
#     'ismi':'mirzo ulugbek',
#     "t_yil":1489,
#     'ishi':"osmon jismlarini o'rgangan"
# }
# buyuk =[sh1  ,sh2 ,sh3]
# for shaxs in  buyuk:
#     print(f"{shaxs['ismi']} "
#     f"{shaxs['t_yil']} da tug'ilgan"
#     )
    #2-amalyot
    
buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
           'tyil':810,
           'vyil':870,
           'tjoy':'Buxoro',
           'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
           }

qodiriy = {'ism':'Abdulla Qodiriy',
           'tyil':1894,
           'vyil':1938,
           'tjoy':'Toshkent',
           'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
           }

vohidov = {'ism':'Erkin Vohidov',
           'tyil':1936,
           'vyil':2016,
           'tjoy':"Farg'ona",
           'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
           }

navoiy = {'ism':'Alisher Navoiy',
           'tyil':1441,
           'vyil':1501,
           'tjoy':"Xirot",
           'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
           }

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

for shaxs in shaxslar:
    ism = shaxs['ism']
    asarlar = shaxs['asarlar']
    print(f"\n{ism} ning mashxur asarlari: ")
    for asar in asarlar:
        print(asar)