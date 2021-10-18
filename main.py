def citire_lista(lista_de_numere):
    string_citire = input("dati lista de numere separate prin virgula: ")
    valori = string_citire.split(",")
    for x in valori:
        lista_de_numere.append(int(x))
    return lista_de_numere


def cautare_element(lista, numar):
    """
    Verifica daca o valoare intreaga "numar" se afla intr-o lista de numere
    :param lista: o lista de numere intregi
    :param numar: un numar intreg
    :return: True, daca numarul se afla in lista, respectiv False in caz contrar
    """
    for i in range(len(lista)):
        if lista[i] == numar:
            return True
    return False


def eliminare_duplicate(lista_de_numere):
    """
    Elimina elementele duplicate dintr-o lista de valori intregi
    :param lista_de_numere: o lista de numere intregi
    :return: o noua lista de numere intregi
    """
    rezultat = []
    rezultat.append(lista_de_numere[0])
    for i in range(1, len(lista_de_numere)):
        gaseste = cautare_element(rezultat, lista_de_numere[i])
        if gaseste is False:
            rezultat.append(lista_de_numere[i])
    return rezultat


def afisare_lista(lista_de_numere):
    afisare = str(lista_de_numere)
    print(afisare)


def test_cautare_element():
    assert cautare_element([1, 2, 3], 3) is True
    assert cautare_element([17, 10, 19], 14) is False
    assert cautare_element([10, 20], 1) is False


def test_eliminare_duplicate():
    assert eliminare_duplicate([1, 2, 3, 4, 5, 5]) == [1, 2, 3, 4, 5]
    assert eliminare_duplicate([10, 17, 19]) == [10, 17, 19]
    assert eliminare_duplicate([]) == []


def meniu():
    print("1. Citirea unei liste de numere intregi")
    print("2. Afisarea listei")
    print("3.")
    print("4.")
    print("5.")
    print("6. Iesire")
    merge = True
    lista_de_numere = []
    while merge is True:
        optiune = int(input("Dati o valoare de la 1 la 6: "))
        if optiune == 1:
            lista_de_numere = []
            citire_lista(lista_de_numere)
        elif optiune == 2:
            rezultat = eliminare_duplicate(lista_de_numere)
            afisare_lista(rezultat)
        elif optiune == 6:
            merge = False
        else:
            print("Valoare gresita! Incercati din nou!")


def main():
    test_cautare_element()
    meniu()


if __name__ == '__main__':
    main()
