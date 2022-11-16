import random 

number = random.randint(1,50)

benutzer_number = int(input("Geben Sie bitte eine Zahl ein:"))

while benutzer_number < 1 or benutzer_number > 50:
    benutzer_number = int(input("Geben Sie bitte eine Zahl ein:"))

Grün = True

count = 0
while Grün:
    count += 1
    if count == 10:
        print("Sie haben keine Versuche mehr!!")
        print("Hier endet das Programm!!")
        break


    if benutzer_number == number:
        print("Sie haben die Nummer gefunden!!")
        break
    elif benutzer_number < number:
        print("Die Nummer ist kleiner!")
        benutzer_number = int(input("Geben Sie bitte eine andere Zahl ein:"))
        continue
    else:
        print("die Nummer ist großer!!")
        benutzer_number = int(input("Geben Sie bitte eine andere Zahl ein:"))
        continue

print("Sie haben "+count+"Versuche gehabt!")
