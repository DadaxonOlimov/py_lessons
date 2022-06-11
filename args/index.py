             #*argus **kwargus
def summa(*sonlar):
    yigindi = 0
    for son  in sonlar:
        yigindi += son
    return yigindi
print(summa(1,5,3,4,5))

def summa(*sonlar):
 return sum(sonlar)
print(summa(1,5,3,4,5))

def summa(x,y,*sonlar):   #x,y qilgandan keyin kamida 2ta son qabul qiladi
    return x+y+sum(sonlar)
print(summa(1,5,3,4,5))
       #**kwargs
def avtomobile(model,narx,**malumotlar):
    malumotlar['model']=model
    malumotlar['narx']=narx
    return malumotlar
print(avtomobile('gm',18000,rang='oq',holati='alo'))    




    