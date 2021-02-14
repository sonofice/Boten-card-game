import time, random, os

print("Welkom bij het drankspel 3 kaarten!", "\nDit zijn de ronde's: ")

def sleep():
    time.sleep(1)

def volgende_ronde():
    print("Volgende ronde!")

# kaartdeck generation zwart
ranks_zwart = ["2","3","4","5","6","7","8","9","10","boer","koningin","koning","Aas"]
cat_zwart = ["schoppen","klaver"]
deck_zwart = []

value = 1
for rank in ranks_zwart:
    for cat in cat_zwart:
        deck_zwart.append([cat + " " + rank, value])
    value +=1 

# kaartdeck generation rood
ranks_rood = ["2","3","4","5","6","7","8","9","10","boer","koningin","koning","Aas"]
cat_rood = ["harten","ruiten"]
deck_rood = []

value = 1
for rank in ranks_rood:

    for cat in cat_rood:
        deck_rood.append([cat + " " + rank, value])
    value +=1 

user_deck = []
deck_samengevoegd = []
deck_samengevoegd = deck_rood + deck_zwart

# soorten rondes
rnd = [" ", "Rood of zwart", "Hoger of lager", "Binnen of buiten"]

# print van alle rondes per seconde
for ronde in range(1, 4):
    print("Ronde", ronde, rnd[ronde])
    sleep()

while True:
    print("We gaan beginnen met ronde 1!")
    user_deck = []
    random.shuffle(deck_samengevoegd)

    while True:
        random_kaart = deck_samengevoegd.pop(0)
        user_deck.append(random_kaart)
        colours = ["rood", "zwart"]
        for kaart in random_kaart:
            print("Wat kies je? rood of zwart?")
            #check of de kaart rood of zwart is
            for kleur in random_kaart:
                if random_kaart in deck_rood:
                    kaart = "rood"
                    break
                else: 
                    kaart = "zwart"
                    break
            while True:
                gekozen_kleur = input(": ")
                if gekozen_kleur.lower() == "rood" and kaart == "rood":
                    os.system("cls")
                    print("Lekker pik")
                    break
                elif gekozen_kleur.lower() == "rood" and kaart == "zwart":
                    os.system("cls")
                    print("Neem een shot!")
                    break
                elif gekozen_kleur.lower() == "zwart" and kaart == "zwart":
                    os.system("cls")
                    print("Lekker pik")
                    break
                elif gekozen_kleur.lower() == "zwart" and kaart == "rood":
                    os.system("cls")
                    print("Neem een shot!")
                    break
                elif gekozen_kleur.lower != colours:
                    print("Kies rood of zwart")
            break
        break

    print("Je hebt nu de volgende kaarten in je deck:", *user_deck[0])

    volgende_ronde()
    sleep()
    print("Ronde 2!")
    sleep()
    random.shuffle(deck_samengevoegd)

    # ronde 2 higher lower
    while True:
        random_kaart2 = deck_samengevoegd.pop(0)
        user_deck2 = user_deck[0]
        user_deck.append(random_kaart2)
        opties = ["hoger", " lager"]
        print("Hoger of lager?")
        while True:
            keuze = input(": ")
            if keuze.lower() == "hoger" and random_kaart2[1] >  user_deck2[1]:
                os.system("cls")
                print("Eeeyyoooo nice gedaan!")
                break
            elif keuze.lower() == "hoger" and random_kaart2[1] <  user_deck2[1]:
                os.system("cls")
                print("Jammer jammer. Dat wordt een shotjuuuhh")
                break

            elif keuze.lower() == "lager" and random_kaart2[1] <  user_deck2[1]:
                os.system("cls")
                print("Eeeyyoooo nice gedaan!")
                break
            elif keuze.lower() == "lager" and random_kaart2[1] >  user_deck2[1]:
                os.system("cls")
                print("Jammer jammer. Dat wordt een shotjuuuhh")
                break
            elif keuze != opties[0 or 1]:
                print("Kies hoger of lager")
        break


    print("Je hebt nu de volgende kaarten in je deck:", *user_deck[0], *user_deck[1])


    sleep()
    volgende_ronde()
    sleep()
    print("Ronde 3!")
    sleep()

    random.shuffle(deck_samengevoegd)

    #ronde 3 binnen buiten
    while True:
        random_kaart3 = deck_samengevoegd.pop(0)
        udeck1st = user_deck[0]
        udeck2nd = user_deck[1]
        user_deck.append(random_kaart3)
        opties = "binnen" or "buiten"
        print("Binnen of buiten?")
        while True:
            keuze = input(": ")   
            if keuze.lower() == "binnen" and random_kaart3[1] > udeck1st[1] and random_kaart3[1] < udeck2nd[1]:
                os.system("cls")
                print("Ok, ok. Goeie")
                break
            elif keuze.lower() == "binnen" and random_kaart3[1] < udeck1st[1] and random_kaart3[1] > udeck2nd[1]:
                os.system("cls")
                print("Ok, ok. Goeie")
                break
            elif keuze.lower() == "binnen" and random_kaart3[1] < udeck1st[1] and random_kaart3[1] < udeck2nd[1]:
                os.system("cls")
                print("kansloooos. Neem een shot")
                break
            elif keuze.lower() == "binnen" and random_kaart3[1] > udeck1st[1] and random_kaart3[1] > udeck2nd[1]:
                os.system("cls")
                print("kansloooos. Neem een shot")
                break

            elif keuze.lower() == "buiten" and random_kaart3[1] > udeck1st[1] and random_kaart3[1] < udeck2nd[1]:
                os.system("cls")
                print("kansloooos. Neem een shot")
                break
            elif keuze.lower() == "buiten" and random_kaart3[1] < udeck1st[1] and random_kaart3[1] > udeck2nd[1]:
                os.system("cls")
                print("kansloooos. Neem een shot")
                break
            elif keuze.lower() == "buiten" and random_kaart3[1] < udeck1st[1] and random_kaart3[1] < udeck2nd[1]:
                os.system("cls")
                print("Ok, ok. Goeie")
                break
            elif keuze.lower() == "buiten" and random_kaart3[1] > udeck1st[1] and random_kaart3[1] > udeck2nd[1]:
                os.system("cls")
                print("Ok, ok. Goeie")
                break
            elif keuze.lower() == "buiten" or "binnen" and random_kaart3[1] == udeck1st[1] or random_kaart3[1] == udeck2nd[1]:
                os.system("cls")
                print("Je mag kiezen of je een shot neemt")
                break
            elif keuze.lower() != opties:
                print("Kies binnen of buiten")
        break
    print("Dit zijn je kaarten", *user_deck[0], *user_deck[1], *user_deck[2])
    print("Wil je het nog een keer spelen? Ja of nee")
    opnieuw = input(": ")
    if opnieuw.lower() == "ja":
        os.system("cls")
        print("Let's gooooo")
    else:
        opnieuw.lower() == "nee"
        break
