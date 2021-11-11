class ListeElement:
    def __init__(self, element):
        self.element = element
        self.neste = None

class LenketListe:
    def __init__(self):
        self.forste = ListeElement(None)
        self.siste = self.forste
        self.lengde = 0

    # Legger til element paa slutten av lista
    # - Lag et nytt listeElement
    # - Sett siste element til aa referere til det
    # - Oppdater referansene
    # Kjoretid O(1)
    def append(self, element):
        nytt_element = ListeElement(element)
        self.siste.neste = nytt_element
        self.siste = nytt_element
        self.lengde += 1

    # Kjoretid Theta(indeks)
    # Kjoretid O(1) best case, forste element
    # Kjoretid O(n) worst case, siste element
    def finn_element(self, indeks):
        if indeks >= self.lengde:
            raise IndexError
        nv_element = self.forste
        for i in range(indeks):
            nv_element = nv_element.neste
        return nv_element

    # Legger inn det oppgitte elementet paa oppgitt indeks, og forskyver alle elementer som ligger
    # etterpaa ett hakk bak
    # Kjoretid som finn_element
    def insert(self, indeks, element):
        nv_element = self.finn_element(indeks)
        nytt_element = ListeElement(element)
        nytt_element.neste = nv_element.neste
        nv_element.neste = nytt_element
        self.lengde += 1

    # Overskriver det som ligger paa oppgitt indeks med det oppgitte elementet.
    # Tilsvarer Python liste[indeks] = element
    # Kjoretid som finn_element
    def put(self, indeks, element):
        if indeks == self.lengde -1:
            nv_element = self.siste
        else:
            nv_element = self.finn_element(indeks)
            nv_element.element = element

    # Fjerner forste forekomst av oppgitt element
    def remove(self, element):
        nv_element = self.forste
        while nv_element.neste is not None:
            if nv_element.element == element:
                nv_element.neste = nv_element.neste.neste
                self.lengde -= 1
                return
            nv_element = nv_element.neste

    # Fjerner elementet paa oppgitt indeks
    # Tilsvarer Python del liste[indeks]
    def delete(self, indeks):
        nv_element = self.finn_element(indeks-1)
        nv_element.neste = nv_element.neste.neste
        self.lengde -= 1

    # Legger alle elementete i oppgitt samling til i lista
    # Kjoretid O(antall elementer i den nye lista)
    def append_all(self, samling):
        for element in samling:
            self.append(element)

    # Setter inn den oppgitte samlingen paa oppgitt indeks, og forskyver alt som ligger bak
    # Kjoretid O(m + n), m er elementene i den nye kustam b er elementene i den gamle.
    def insert_all(self, indeks, samling):
        nv_element = self.finn_element(indeks)
        for element in samling:
            nytt_element = ListeElement(element)
            nytt_element.neste = nv_element.neste
            nv_element.neste = nytt_element
            nv_element = nytt_element
            self.lengde += 1

    # Returnerer elementet paa oppgitt indeks.
    # Tilsvarer Python variabel = liste[indeks]
    # Kjoretid som for finn_element
    def get(self, indeks):
        if indeks == self.lengde-1:
            return self.siste
        nv_element = self.finn_element(indeks)
        return nv_element.element

    # Finner forste indeks hvor dette elementet forekommer
    # Sekvensielt sok
    def search(self, element):
        nv_element = self.forste.neste
        nv_index = 0
        while nv_element is not None:
            if nv_element.element == element:
                return nv_index
            nv_index += 1
            nv_element = nv_element.neste
        return -1

    # Gaa gjennom lista, element for element
    def __iter__(self):
        return LenketListeIterator(self)

class LenketListeIterator:
    def __init__(self, lista):
        self.lista = lista
        self.nv_element = lista.forste

    def __next__(self):
        self.nv_element = self.nv_element.neste
        if self.nv_element is None:
            raise StopIteration
        else:
            return self.nv_element.element

    def __iter__(self):
        return self

if __name__ == "__main__":
    liste = LenketListe()
    liste.append(6)
    liste.append(9)
    liste.append(-2)
    liste.insert(0, -5)
    liste.insert(3, -8)
    liste.append(5)
    liste.append(7)
    print(liste.get(2))
    print(liste.search(5))
    print()
    for element in liste:
        print(element)
    print()
    liste.remove(9)
    liste.delete(1)
    for element in liste:
        print(element)