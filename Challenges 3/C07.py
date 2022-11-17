activ = True

while activ:
    my_list = ['a','e','u','i','o','y']

    wort = input("Geben Sie eine Wort ein:").lower()

    erste_buchstabe = wort[0]
    rest_des_wortes = wort[1:]
    
    
    
    if erste_buchstabe not my_list:
        new_wort = f'{rest_des_wortes}{erste_buchstabe}'+"ay"
        print(new_wort.lower())
        continue
    elif erste_buchstabe is my_list:
        new_wort1 = f'{erste_buchstabe}{rest_des_wortes}'+"way"
        print(new_wort1.lower())
        continue
    else:
        print("False eingabe!")
        break
    
    


