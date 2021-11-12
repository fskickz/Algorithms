# Trestrukturer
Et tre er en struktur som består av ei rot og fleire noder under.

### Terminologi:
* En node er rotnoden og der treet starter
* Alle andre noder har en foreldrenode
* En **sti** er en sekvens av noder forbundet med kanter
* Lengden på stien (antall pekere man må følge) for å komme fra en node til en rotnoden er **dybden** til noden
* **Høyden** til treet er den maksimale dybden til en node (høyde er "motsatt" av dybde)
* En **bladnode** er en node som ikke har barn
* En **indre node** er en node som ikke er en bladnode
* **Søsken**: Noder som har samme forelder
* **Fullt tre**: Hver interne node har to barn
* **Perfekt tre**: Alle bladnoder har samme nivå
* **Balansert tre**: Forskjellen i høyde på venstre og høyre subtre er maks 1
* **Komplett tre**: Alle nivåer unntatt det nederste er fullt, det nederste fylles fra venstre mot høyre.


### Implementasjon:
* Hver node har et objekt og ei liste med barn
    * Fordel: raskere navigering
    * Ulempe: ineffektiv lagring da hver node må inneholde ei liste
* Hver node har et objekt, en referanse til første barn, og en referanse til nærmeste søskennode
    * Fordel: Effektiv lagring
    * Ulempe: Tregere navigering (barna blir i praksis ei lenket liste i stedet for arraylist)
* Bruk av pekere oppover i treet for å forbedre visse algoritmer

### Traversing
* **Preorder**: 
    1. Besøk rotnoden
    2. Traverser venstre subtre rekursivt
    3. Traverser høyre subtre rekursivt

A → B → D → E → C → F → G

![](https://www.tutorialspoint.com/data_structures_algorithms/images/preorder_traversal.jpg)

---

* **Inorder**: 
    1. Traverser venstre subtre rekursivt
    2. Besøk rotnoden
    3. Traverser høyre subtre rekursivt

D → B → E → A → F → C → G

![](https://www.tutorialspoint.com/data_structures_algorithms/images/inorder_traversal.jpg)

---

* **Postorder**: 
    1. Traverser venstre subtre rekursivt
    2. Traverser høyre subtre rekursivt
    3. Besøk rotnoden

D → E → B → F → G → C → A

![](https://www.tutorialspoint.com/data_structures_algorithms/images/postorder_traversal.jpg)




## Binærtre
Et binærtre er et tre som kun inneholder 0-2 barn per node.
Vi har også **binært søketre** der venstre subtre inneholder verdier som er mindre enn rotnoden, og høyre subtre inneholder verdier som er større. 

Å traversere et tre tar uansett O(n) fordi ein må gjennom alle verdier.

## AVL-tre
Et AVL-tre er et høydebalansert binært søketre. Vi ser på **balansefaktoren** til en node:
* Høyde(venstre subtre) - høyde(høyre subtre)

I et AVL-tre må balansefaktoren regnes ut ved hver node:
* Balansefaktoren må være -1 <= x <= 1 
* Lagre balansefaktoren på hver node

For å balansere et AVL-tre må man gjøre rotasjoner for å endre hvordan treet ser ut:

### Venstre rotasjon:

![](https://www.tutorialspoint.com/data_structures_algorithms/images/avl_left_rotation.jpg)

### Høyre rotasjon:

![](https://www.tutorialspoint.com/data_structures_algorithms/images/avl_right_rotation.jpg)

### Venstre-høyre rotasjon:

![](/fig/Venstre-hoyre.png)

### Høyre-venstre rotasjon:

![](/fig/Hoyre-venstre.png)



|         | Average   |           |           | Worst     |           |           |
|---------|-----------|-----------|-----------|-----------|-----------|-----------|
|         | Search    | Insertion | Deletion  | Search    | Insertion | Deletion  |
| AVL-tre | O(log(n)) | O(log(n)) | O(log(n)) | O(log(n)) | O(log(n)) | O(log(n)) |
| Binært søketre | O(log(n)) | O(log(n)) | O(log(n)) | O(n)      | O(n)      | O(n)      |
| Binærtre       | O(log(n)) | O(log(n)) | O(log(n)) | O(log(n)) | O(log(n)) | O(log(n)) |