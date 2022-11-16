my_number = int(input("Geben Sie bitte eine Zahl ein:"))

if my_number < 10:
    print("zu klein!")
elif my_number in range(10,20+1):
    print("in Ordnung")
else:
    print("zu Hoch!")

