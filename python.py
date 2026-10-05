import random

while True:
    dificulty = input("zvol obtiznost (1/2/3): ")
    if dificulty not in ["1", "2", "3"]:
        print("neplatny vstup")
        continue

    maxlenght = 100

    if dificulty == "1":
        cislo = random.randint(1, 100)
        maxlenght = 100

    elif dificulty == "2":
        cislo = random.randint(1, 50)
        maxlenght = 50
    elif dificulty == "3":
        cislo = random.randint(1, 25)
        maxlenght = 25

    attempts = 0

    while True:
        
        usercislo = input("tvuj guess: ")
        if usercislo.isdigit() == False :
            print("neplatny vstup")
            continue
        if int(usercislo) < 1 or int(usercislo) > maxlenght:
            print("neplatny vstup")
            continue

        attempts += 1
        usercislo = int(usercislo)
        if usercislo < cislo:
            print("je vetsi")

        elif usercislo > cislo:
            print("je mensi")

        elif usercislo == cislo:
            print("spravne")
            print("pocet pokusu: " + str(attempts))
            break

    decision = input("chces hrat znovu (ano/ne): ")
    if decision.lower() != "ano":
        break
