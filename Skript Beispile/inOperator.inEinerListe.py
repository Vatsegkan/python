my_list = [1, 2, 3]
activ = True
while activ:
    number = int(input("Geben Sie eine Nummer ein:"))
    if number in my_list:
        print("Die Zahl ist hier!!!")
        break
    else:
        print("Die Zahl ist nicht da!!!")
        continue