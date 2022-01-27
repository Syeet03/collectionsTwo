import time, os
lijstje = {}

def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

def boodschappenLijstje():
    toevoeg = input('Wat wild u toevoegen aan uw boodschappenlijstje? Voor STOP in om de stoppen.\n')
    if toevoeg == 'STOP':
        print('Uw boodschappenlijstje: ' + str(lijstje))
        clearScreen(10)
        print('Bedankt voor het gebruiken van het boodschappenlijstje!')
        clearScreen(5)
        print('Uw boodschappenlijstje word geupload naar de app van uw gekozen supermarkt!')
        clearScreen(5)
        print('Geupload!')
        clearScreen(5)
        main()
    else:
        if toevoeg in lijstje:
            lijstje[toevoeg] += 1
        else:
            lijstje[toevoeg] = 1
        print('Toegevoegd!')
    clearScreen(1)
    boodschappenLijstje()

def main():
    print('Jouw boodschappenlijstje')
    clearScreen(3)
    print('Laden...')
    clearScreen(2)
    input('Kies: Albert Heijn of Jumbo: ')
    clearScreen(2)
    boodschappenLijstje()

main()