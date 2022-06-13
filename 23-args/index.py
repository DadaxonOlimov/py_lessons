             #*argus **kwargus
# def summa(*sonlar):
#     yigindi = 0
#     for son  in sonlar:
#         yigindi += son
#     return yigindi
# print(summa(1,5,3,4,5))

# def summa(*sonlar):
#  return sum(sonlar)
# print(summa(1,5,3,4,5))

# def summa(x,y,*sonlar):   #x,y qilgandan keyin kamida 2ta son qabul qiladi
#     return x+y+sum(sonlar)
# print(summa(1,5,3,4,5))
#        #**kwargs
# def avtomobile(model,narx,**malumotlar):
#     malumotlar['model']=model
#     malumotlar['narx']=narx
#     return malumotlar
# print(avtomobile('gm',18000,rang='oq',holati='alo'))    
           #amaliyot
# def multiply(*sonlar):
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma *= son
#     return kopaytma

# print(multiply(4,5,6))
# def t_malumot(ism,familya,**qoshimcha):
#     qoshimcha ['ismi']=ism
#     qoshimcha['familya']=familya
#     return qoshimcha
# print(t_malumot('shahzod','olimov',akasi='zokir'))    


import math

a=int(input())
print(math.sqrt(a))