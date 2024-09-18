#nurodo žaidmo lentą
def rodyti_lenta(lenta):
    for i in range(0, 9, 3):
        print(' | '.join(lenta[i:i+3]))
        if i < 6: print("---------")
#tikrina laimėjimų kombinacijas
def tikrinti_laimejima(lenta, zaidejas):
    pergales = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(all(lenta[i] == zaidejas for i in kombinacija) for kombinacija in pergales)
#kryžiukų-nuliukų veiksmų eiga
def zaisti():
    lenta, zaidejas = [' '] * 9, 'X'
    while ' ' in lenta:
        rodyti_lenta(lenta)
        ejimas = int(input(f"Žaidėjas {zaidejas}, įveskite ėjimą (1-9): ")) - 1
        if lenta[ejimas] == ' ':
            lenta[ejimas] = zaidejas
            if tikrinti_laimejima(lenta, zaidejas):
                rodyti_lenta(lenta)
                print(f"Žaidėjas {zaidejas} laimėjo!")
                return
            zaidejas = 'O' if zaidejas == 'X' else 'X'
    rodyti_lenta(lenta)
    print("Lygiųjų rezultatas!")

zaisti()
