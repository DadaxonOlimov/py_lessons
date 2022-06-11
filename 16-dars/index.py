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
        
# moshin = []
# for car in moshin:
#     print(f"mashina modeli {car['model']}"
#     f"uning rangi {car['rang']}"
#     f" uning yili{car['yil']}"
#     f"uning narxi{car['narh']}")
# print(moshin[0]["rang"],moshin[1]['model'])
mashinalar = []
for moshin in range(10):
    new_car ={
      'model':'malibu',
      'rangi':None,
      'yili':'2022',
      'narxi':None,
      'km':'0',
      'karobka':"avto"
  }
    mashinalar.append(new_car)
for malibu in mashinalar[:3]:
    malibu['rang']='qizil'
for malibu in mashinalar[3:6]:
    malibu['rang']='sariq'
for malibu in mashinalar[6:]:
    malibu['rang']='qara'    

for malibu in mashinalar:
    print(malibu)
   


