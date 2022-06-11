# yosh = int(input("yoshinimgizni kiriting??"))
# if yosh <4:
#     print("sizga kirish bepul")
# elif yosh<12:
#     print("sizga kirish 10.00)
# else:
#     print("sizga kirish 25.000so'm")  0 so'm")  
# kun = input("bugun qanday kun?")
# if kun.lower() =="shanba" or kun.lower() == "yakshanba":  
#     print("bugun dam olish")
# else:
#     print("bugun ish kuni")      
# kun = input("bugun qanday kun\n")
# harorat = float(input("harorat qanday??"))
# if kun =="yakshanba" and harorat>30:
#     print("kettik sho'milishga")
# elif kun.lower =="yakshanba" and harorat<30:
#     print("boshqa kun cho'milishga boramiz !!")    
from pickle import FALSE, TRUE


# narx = 15000
# choy = True
# salat = False
# kompot = True
# if choy and salat:
#     narx = narx+5000
# elif salat or kompot:
#     narx = narx+4000
#     print(f"jami narx { narx } ming so'm")
# narx = 15000
# kampot = True
# salat = False
# assarti = True
# if kampot:
#     print("mijoz kampot oldi")
#     narx = narx+5000
#     if salat:
#         print("mijoz salat olmadi")
#         print(f"jami summa{narx}ming so'm")
# menyu = ['manti','shorva','osh','mastava']
# ovqat = input("nima ovqat yeysiz?\n")
# if ovqat.lower() in menyu:
#     print("bizda bu ovqat bor tez orada olib kelamiz!!")
# else:
#     print("uzr bizda bunday taom yo'q")
menyu = ['manti','shorva','osh','mastava']
buyurtmalar = ["shashlik","shorva","osh","mastava"]
for taom in menyu:
    if taom in buyurtmalar:
        print(f"ha bu taomlar {taom} bor")
else:
    print(f'UZR bu {taom} menyuda yoq')        







