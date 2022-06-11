def baholar(ismlar):
    bahola=[]
    while ismlar:
        ism= ismlar.pop()
        baho =input(f"talaba{ism.title()}ning bahosini kiriting:")
        bahola[ism]=int(baho)
        return bahola
    talabalar =['ali','vali','zokir']
    bahola = baholar(talabalar)  
    print  