activ = True

while activ:
    
    wort = input("Geben Sie eine Wort ein:").lower()

    erste_buchstabe = wort[0]
    rest_des_wortes = wort[1:]
    
    if erste_buchstabe not in set('aeuioy'):
        new_wort = f'{rest_des_wortes}{erste_buchstabe}'+"ay"
        print(new_wort.lower())
    else:
        new_wort1 = wort + "way"
        print(new_wort1.lower())