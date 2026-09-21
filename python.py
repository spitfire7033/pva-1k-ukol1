import random

while True:
    dificulty = input("zvol obtiznost (1/2/3): ")

    if dificulty == "1":
        cislo = random.randint(1, 100)
    elif dificulty == "2":
        cislo = random.randint(1, 50)
    elif dificulty == "3":
        cislo = random.randint(1, 25)

    attempts = 0

    while True:
        attempts += 1
        usercislo = int(input("tvuj guess: "))

        if usercislo < cislo:
            print("je vetsi")

        elif usercislo > cislo:
            print("je mensi")

        elif usercislo == cislo:
            print("spravne")
            print("pocet pokusu: " + str(attempts))
            break
        else:
            print("neplatny vstup")

    decision = input("chces hrat znovu (ano/ne): ")
    if decision.lower() != "ano":
        break
