# mevalar = ["alma" , "anjir"]
# print(len(mevalar)) # len massiv ichidagi qiymatlar sonini aniqlaydi

# mevalar = ['olma' , 'anor', 'shaftoli', 'nok']
# # print(mevalar[-1]) # bu holat qiymatlarni oxiridan boshlab chaqirish

# # mevalar[-2] = "uzum"
# # print(mevalar)

# # print(mevalar[1].upper())
# # print(mevalar[2].title())

# # append - bu metod oz'garuvchini oxiriga qiymat qo'shadi 
# # mevalar = ['olma' , 'anor', 'shaftoli', 'nok']
# # mevalar.append("tarvuz")                   #  mevalar qiymatiga tarvuz qoshildi
# # print(mevalar)

# # insert - bu metod o'zgaruvchiga istalgan indexsiga qiymat berish mumkin
# # mevalar = ['olma' , 'anor', 'shaftoli', 'nok']
# # mevalar.insert(0, "banan")
# # print(mevalar)

# cars = []
# cars.append("Lacetti")
# cars.append("Nexia")
# cars.append("Spark")
# cars.append("Malibu")

# print(cars)

# # del - bu element o'zgaruvchini qiymatini (index) raqami orqali o'chirish
# del cars[1]
# print(cars)

# cars.insert(1, "Nexia 3")
# print(cars)

# remove - bu element o'zgaruvchidagi qiymatni teksti orqali o'chirish
cars.remove("Spark")
print(cars)

# remove - bu holatda o'zgaruvchida bir xil qiymatlar bo'lsa 1-sini o'chiradi
# hayvonlar = ["sigir", 'mushuk', "it", "sher", "yo'lbars", 'mushuk']
# hayvonlar.remove('mushuk')
# print(hayvonlar)

#      pop - bu funksiya o'zgaruvchi ichidagi qiymatlarni tanlab oladi
# bozorlik = ["banan", "go'sht", "piyoz", "kartoshka", "kola"]
# mahsulot = bozorlik.pop(1)
# print("Men " + mahsulot + " oldim" )
# print("Olinmagan mahsulotlar " , bozorlik)

# pop() bu holatda o'zgaruvchini oxirgi qiymatini oladi
# bozorlik = ["banan", "go'sht", "piyoz", "kartoshka", "kola"]
# mahsulot2 = bozorlik.pop()
# print(mahsulot2)

# misolcha
# narhlar = [12 ,23, 34, 45, 56]
# narhlar[3] = narhlar[3] + 12
# print(narhlar)


# AMALIYOT

# ismlar = ["Maxmud", "Mirshod", "Ahmad" ]

# print("Salom " + ismlar[0] + " yaxshimisan?")
# print(ismlar[1] + " qayerdasan?")
# print(ismlar[2] + " qachan kelasan?")

# sonlar = [12, 23, 34, 45, 56, 67, 78]
# sonlar[1] = sonlar[2] - sonlar[1]
# sonlar[4] = sonlar[2] * sonlar[3]
# sonlar[2] = sonlar[2] * sonlar[-1]

# del sonlar[5]
# sonlar.insert(1, 452)
# sonlar.append(122222)
# sonlar.insert(6, 45)

# print(sonlar)


# t_shaxslar = ["Umar" , "Ali" "Usmon"]
# z_shaxslar = ["Ishoqjon" , "Abror", "Rustamjon"]

# print(f"Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan \nzamonaviy shaxslardan esa {z_shaxslar.pop(1)} bilan \nsuhbat qilishni istar edim")

# friends = [ ]
# friends.append("Zokir")
# friends.append("Oybek")
# friends.append("Sobir")
# friends.append("Shaxzod")
# friends.append("Dadaxon")

# print(friends)

# friends.remove("Oybek")
# friends.remove("Shaxzod")
# print(friends)

# friends.insert(0, "Jasur")
# friends.insert(2, "Maxmud")
# friends.append("Ahmad")
# print(friends)

# mehmonlar = []
# mehmonlar.append(friends.pop(1))
# mehmonlar.append(friends.pop(3))
# mehmonlar.append(friends.pop(0))
# print(mehmonlar)



