def GetTime():
    import time
    print (time.strftime("%H:%M:%S"))
    print (time.strftime("%d/%m/%Y"))
kontolist = {}
def SkapaNyttKonto():
    print("Skapa nytt Konto")
    konto = int(input("Ange konto Namn: "))
    if konto in kontolist:
        print("Kontot finns redan")
    else :
        kontolist[konto] = 0
        print("Konto Skapad!")
        print("Du har skapat följande konton: ", kontolist)
def LoggaIN():
    print("Logga in med ditt konto")
    konto = int(input("Ange kontonummer: "))
    if konto in kontolist:
        print("Du är inloggat")
        while True:              
            print("***Konto meny***")
            print("1. Ta ut pengar")
            print("2. Sätt i pengar")
            print("3. Visa saldo")
            print("4. Avsluta")
            choice = str(input())
            if choice == "1":
                print("Ta ut pengar")
                pengarUt = int(input("Ange belopp att ta ut: "))

                if pengarUt < kontolist[konto]  and pengarUt > 0:
                    kontolist[konto]  -= pengarUt   
                    print("Belopp är uttaget")
                else:
                    print("För stort eller felakitgt belopp")

            if choice == "2":                 
                print("Sätt i pengar")
                pengarIn = int(input("Ange belopp du vill sätta in: "))
                kontolist[konto]  = kontolist[konto]  + pengarIn

            if choice == "3":
                print("Ditt saldo är: ", kontolist[konto] )                
            elif choice == "4":
                print("Du har valt att gå till huvudmeny")
                break
    else:
       print("Konton är inte skapad ")


while True:
    GetTime()
    print("***HUVUDMENY***")
    print("1: Skapa nytt konto") 
    print("2: logga in med ditt konto")
    print("3: Avsluta")
    selection = str(input("Välj ett val: "))
    if selection == "1":
       SkapaNyttKonto()
    if selection == "2": 
       LoggaIN()
    elif selection == "3":
        print("Du har valt att avsluta programmet")
        break