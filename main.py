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


def suma_elemente_pozitive(lista, n):
    """
    Calculeaza suma a primelor n numere pozitive dintr-o lista
    :param lista: o lista de numere intregi
    :param n: o valoare intreaga
    :return: o valoare intreaga
    """
    suma = 0
    pozitie = 0
    for i in range(len(lista)):
        if lista[i] >= 0:
            suma = suma + lista[i]
            pozitie = pozitie + 1
            if pozitie == n:
                return suma
    return None


def verificare_ordine_elemente_pozitive(lista):
    """
    Verifica daca elementele pozitive dintr-o lista sunt in ordine crescatoare
    :param lista: o lista de numere intregi
    :return: True, daca lista are aceasta proprietate, respectiv False in caz contrar
    """
    lista_pozitive = []
    for i in range(len(lista)):
        if lista[i] >= 0:
            lista_pozitive.append(lista[i])
    for i in range(1, len(lista_pozitive)):
        if lista_pozitive[i - 1] > lista_pozitive[i]:
            return False
    return True


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
    assert eliminare_duplicate([1]) == [1]


def test_suma_elemente_pozitive():
    assert suma_elemente_pozitive([10, -3, 25, -1, 3, 25, 18], 3) == 38
    assert suma_elemente_pozitive([-1, -2, -3], 1) is None
    assert suma_elemente_pozitive([1, 2, 3, 4], 5) is None


def test_verificare_ordine_elemente_pozitive():
    assert verificare_ordine_elemente_pozitive([10, 13, -1, 24, 33, 45]) is True
    assert verificare_ordine_elemente_pozitive([5, 4, 3, 2, -1]) is False
    assert verificare_ordine_elemente_pozitive([1, 2, 3, 3, -1, 0]) is False


def meniu():
    print("1. Citirea unei liste de numere intregi")
    print("2. Afisarea listei fara duplicate.")
    print("3. Afisarea sumei primelor n numere pozitive din lista, unde n se citeste de la tastatura.")
    print("4. Sa se afiseze “DA” in cazul in care toate numerele pozitive din lista sunt in ordine crescatoare si “NU” altfel.")
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
        elif optiune == 3:
            numar = int(input("Dati valoarea numarului: "))
            rezultat = suma_elemente_pozitive(lista_de_numere, numar)
            if rezultat is None:
                print("Dimensiunea listei este prea mica")
            else:
                print("Rezultatul este:", rezultat)
        elif optiune == 4:
            verificare = verificare_ordine_elemente_pozitive(lista_de_numere)
            if verificare is True:
                print("DA")
            else:
                print("NU")
        elif optiune == 6:
            merge = False
        else:
            print("Valoare gresita! Incercati din nou!")


def main():
    test_cautare_element()
    test_eliminare_duplicate()
    test_suma_elemente_pozitive()
    test_verificare_ordine_elemente_pozitive()
    meniu()


if __name__ == '__main__':
    main()
