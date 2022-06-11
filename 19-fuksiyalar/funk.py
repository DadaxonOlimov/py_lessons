# def salom_ber(ism):
#     """Foydalanuvchini ismini qabul qilib,
#     unga salom beruvchi funksiya"""
#     print(f"Asalomu aleykum hurmatli {ism.title()}")
# salom_ber('farhod')
# salom_ber('zokir')
# salom_ber('shamshod')
# def yoshni_aniqla(ism,yosh):
#     """foydalanuvchini ismini yoshini hisoblovchi dastur """
#     print(f"{ism.title()} {2022-yosh} yoshda ")
# yoshni_aniqla("anvar",2002)
# # Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
# def tyiltop(ism, yosh):
#     print(f"{ism.title()} {2020-yosh} yoshda")

# tyiltop('olim',2002)
# def hisobla(son):
#     """Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya ."""
#     print(f"{son} ning kv {son**2}ga kubi {son**3}")
# hisobla(5)
# def hisobla(son):
#     """Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya """
#     if son%2:
#         print(f"{son}toq son")
#     else:
#         print(f"{son} juft son")
# hisobla(12)
# hisobla(14)
# hisobla(11)
def taqqosla(son1,son2):
    """Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaradigan funksiya."""
    if son1>son2:
        print(f"{son1} katta {son2}")
    elif son2>son1:
        print(f"{son2} katta {son1}")
    else:
        print(f"{son1} teng {son2}")
taqqosla(12,34)     
taqqosla(92,34)   
taqqosla(12,12)
