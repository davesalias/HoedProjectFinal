def meerkeuzevragen_ophalen(bestand):
    with open(bestand) as f:
        data = f.read()

    vragenlijst = data.split('\n')

    return vragenlijst


def print_vragenlijst(lijst, bestand):
    t = open(bestand, 'a')
    index = 0
    teller = 0
    score_se = 0
    score_fict = 0
    score_iat = 0
    score_bdam = 0

    while index < 15:
        print(lijst[index], '\n')
        t.write(f"Vraag {index + 1}: {input('Antwoord:')} \n")

        index += 1
        continue

    while teller < 15:
        if teller == 0:
            print(datastructuur[0])
            antwoord_1 = input('Antwoord: ')
            if antwoord_1 != 1 or 2:
                print("Geen geldig antwoord")
                teller -= 1
            teller += 1
            if antwoord_1 == 1:
                score_se += 1
            if antwoord_1 == 2:
                score_fict += 1
            if antwoord_1 == 3:
                score_bdam += 1
            if antwoord_1 == 4:
                score_iat += 1


def main():
    data = meerkeuzevragen_ophalen("meerkeuzevragen.txt")
    print_vragenlijst(data, "antwoorden_gebruiker.txt")
    input_actie = input(
        "Type 'q' als je het programma wilt stoppen "
        "\nType '1' Als je alle vragen wilt doorlopen "
        "\nType '2' Als je de laatste uitslag wilt zien"
        "\n "
    )

    if input_actie == 'q':
        quit()
    if input_actie == '1':
        print_vragenlijst(meerkeuzevragen)
    if input_actie == '2':
        with open("antwoorden_gebruiker.txt") as k:
            antwoorden_bestand = k.read()
            print(antwoorden_bestand)


if __name__ == "__main__":
    main()