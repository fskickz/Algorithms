# Lister

## Lenket liste
Ei lenket liste er ei liste der elementene peiker til hverandre. Dette gjør det enkelt å legge til elementer fordi vi kan bare endre pekeren til elementet foran.

Ei lenket liste kan vere dobbel-linket og single-linket. Dersom den er dobbel, vil et element peike til sitt forrige element også.

#### Pros:
* Rask innsetting og sletting
* Bruker ikke mer minne enn den trenger

#### Cons:
* O(k) for å finne det k-ende elementet i lista fordi ein må starte ved først element og gå nedover
* Tar lenger tid enn array for å finne et element

---

## Stacks
Stack er enn kolleksjon av objekter som er inserta og remova med last-in, first-out prinsippet.

En stack kan:
* S.push(9) : Dette legger til 9 øverst i stacken
* S.pop() : Fjerner 9 siden det var siste element som blei lagt til.

Dersom vi pusher 1, 2, 3 på stacken vil den poppe 3, 2, 1 på grunn av LIFO-prinsippet.

---

## Queue
En kø er en kolleksjon av objekter som er inserta og remova med first-in, first-out prinsippet. Det betyr at det elementet som har er først i køen får bli frikjent først.

En kø kan:
* Q.enqueue(9) : Legger til 9 bakerst i køen.
* Q.dequeue() : Fjerner det første elementet i køen.