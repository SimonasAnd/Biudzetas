from biudzetas import Biudzetas

klase = Biudzetas()

while True:
    ivestis = input('''    Meniu:
    1 - Prideti pinigu
    2 - Isimti pinigus
    3 - Parodyti balansa
    4 - Parodyti ataskaita
    5 - Istrinti irasa pagal ID
    6 - Istrinti ataskaita
    # Uzdaryti su ENTER #
    Pasirinkimas: ''')

    if ivestis == '1':
        try:
            print('Prideti pinigu')
            suma = int(input("Suma: "))
            kategorija = input("Kategorija: ")
            siuntejas = input("Siuntejas: ")
            pap_info = input("Papildoma info.: ")
        except:
            print('Blogai ivesti duomenys!')
        else:
            klase.ivesti_pajamas(suma, kategorija, siuntejas, pap_info)
            if klase.gauti_balansa() < 0:
                klase.siusti_email()

    elif ivestis == '2':
        try:
            print('Isimti pinigus')
            suma = int(input("Suma: "))
            kategorija = input("Kategorija: ")
            atsiskaitymo_budas = input("Atsiskaitymo budas: ")
            isigyta_preke_paslauga = input("Isigyta preke/paslauga: ")
        except:
            print('Blogai isvesti duomenys!')
        else:
            klase.ivesti_islaidas(suma, kategorija, atsiskaitymo_budas, isigyta_preke_paslauga)
            if klase.gauti_balansa() < 0:
                klase.siusti_email()

    elif ivestis == '3':
        print(f'Balansas: {klase.gauti_balansa()}')
        if klase.gauti_balansa() < 0:
            klase.siusti_email()
        input('Paspauskite ENTER')

    elif ivestis == '4':
        klase.gauti_ataskaita()
        input('Paspauskite ENTER')

    elif ivestis == '5':
        try:
            id_nr = int(input("Kuri irasa [ID] norite istrinti ? "))
        except:
            print("Blogai ivesti duomenys!")
        else:
            klase.trinti_irasa(id_nr)

    elif ivestis == '6':
        while True:
            artikrai = input('Ar tikrai norite istrinti visa ataskaita? (y/n)')
            if artikrai == 'y':
                klase.trinti_viska()
                print("Ataskaita buvo sekmingai istrinta")
                input('Paspauskite ENTER')
                break
            elif artikrai == 'n':
                break
    else:
        break