# Rekursjon

En rekursiv funksjon er en funksjon som kaller på seg selv. Det er tre lover for rekursive algoritmer:
* Alle rekursive algoritmer må ha et basetilfelle hvor rekursjonen stopper.
* Hvert rekursive kall må endre tilstanden i retning mot basetilfellet.
* Den rekursive algoritmen må kalle seg selv.

Fakultet er et godt eksempel på rekursjon:
* 0! er basetilfellet. Når den når dette punktet stopper den.
* For å finne n! må du også finne (n-1)! og deretter (n-2)! helt ned til 0! som er basetilfellet.
* Den følger dei tre reglene fordi den har et basetilfellet, den endrer seg for hver gang den kalles, og den kaller seg selv.

Kjøretida til rekursive funksjoner er ikke generelle så ta en titt på vedlagte filer for kjøretida til ulike algoritmer.

## Linært søk vs binært søk
Et linært søk er raskere for lister under 10 elementer. Det er liten forskjell på lister mellom 10 og 1000. Binært søk er best for 1000+ elementer. 

Binært søk har O(log n) fordi det alltid deler lista opp i 2. 

Ulempen med binært søk er at lista må være sortert.