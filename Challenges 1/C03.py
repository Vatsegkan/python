number1 = int(input("Geben Sie eine Zahl über 100 ein:"))

while number1 < 100 :
    number1 = int(input("Geben Sie eine Zahl ein:"))

number2 = int(input("Geben Sie eine Zahl unter 10 ein:"))

while number2 > 10:
    number2 = int(input("Geben Sie eine Zahl ein:"))

result = number1 // number2

print("Erste Zahl ist:"+str(number1))
print("Zweite Zahl ist:"+str(number2))
print("passt "+str(result)+"mal rein!")
