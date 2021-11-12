# Innsettingsortering
### Idé:
Kan forklares med at du har ingen kort i venstre hand og ei full hand i høyre hand. Då tar du et og et kort ut av høyre hand og plasser i venstre hand. Når du da legger til et nytt kort sjekker du om det er mindre eller større og plasserer kortet der det tilhører i sortert tilstand.

![](https://runestone.academy/runestone/books/published/pythonds/_images/insertionsort.png)

Det femte kallet:
![](https://runestone.academy/runestone/books/published/pythonds/_images/insertionpass.png)
### Kjøretid: O(n^2)
### Fordeler:
* Kort kode
* Bra lokalitet
* Rask på små datasett (har lavere konstantledd enn de fleste andre algoritmnene)
* Rask på nesten sortert liste
* In-place
### Ulemper
* Treg på store datasett


# Bubblesort
### Idé:
Går gjennom lista gjentatte ganger og switcher elementer ved siden av hverandre som ikke er i sortert tilstand. Bubblesort er tregere enn innsettingsortering. Du flytter elementet dersom det er større enn naboen til høyre. Når det er mindre enn naboen, går du videre til naboen og fortsetter derfra. Dette må gjøres flere ganger.

Første kall
![](https://runestone.academy/runestone/books/published/pythonds/_images/bubblepass.png)
Som du ser må den gjøre dette gjentatte ganger og blir derfor ikke så effektiv.

### Kjøretid: O(n^2)


# Shellsort
### Idé:
Sammenlikner elementer med *k* avstand fra hverandre. Vi setter *k* til n/2 først og deretter sorteringer på *k*/2 helt til du ender opp med å gjøre sortering på en nesten sortert liste når *k* = 1.

Dersom du har ei liste med 9 elementer kan du dele opp i 3 slik som her:
![](https://runestone.academy/runestone/books/published/pythonds/_images/shellsortA.png)

Neste steg:

![](https://runestone.academy/runestone/books/published/pythonds/_images/shellsortB.png)

Siste steg med k=1

![](https://runestone.academy/runestone/books/published/pythonds/_images/shellsortC.png)

### Kjøretid: O(n(log(n))^2)

### Fordeler
* Kort kode, men ikke like kort som insettingsortering
* Rask på datasett av middels størrelse
* In-place
### Ulemper
* Tregere enn de beste algoritmene på store datasett
* Bevisene for kjøretid er enten svært vanskelige eller ikke-eksisterende
* Ustabil

# Flettesortering (Mergesort)
### Idé:
Deler opp lista i mindre lister og sorterer dem når di settes sammen igjen.

![](https://runestone.academy/runestone/books/published/pythonds/_images/mergesortA.png)

![](https://runestone.academy/runestone/books/published/pythonds/_images/mergesortB.png)

### Kjøretid: O(n log(n))

### Fordeler:
* Har garantert O(n*log(n)) kjøretid, derfor alltid brukbart rask selv på store eller merkelige datasett.
* Enkel å parallellisere (send hver halvpart til egen maskin / prossesorkjerne for sortering)
* Stabil
### Ulemper:
* Stor tidskonstant på grunn av kopiering av array.
* Trenger mer plass enn de andre på grunn av kopiering av array.
* Ikke in-place

---

# Quicksort
### Idé:
Quicksort velger først en *pivot*. Deretter gjer den rekursiv quicksort på venstre og høyre del av lista.

Velger som regel pivot verdi basert på *median of three*. Det vil si vi sjekker første, midterste og siste element og velger medianen av dei tre tala. 

Kan også velge første element, eller et tilfeldig element. 

I eksempelet er pivot valgt til første element:

![](https://runestone.academy/runestone/books/published/pythonds/_images/firstsplit.png)

Nå sjekker vi når et element er større enn 54 og deretter hvilket som er mindre frå høyre:

![](https://runestone.academy/runestone/books/published/pythonds/_images/partitionA.png)

Nå kan vi splitte lista her:

![](https://runestone.academy/runestone/books/published/pythonds/_images/partitionB.png)

Og fortsette slik igjen

### Kjøretid: O(n log(n))

### Foredeler:
* Den raskeste sorteringsalgoritmen for mange store datasett
* Sorterer in-place, som reduserer tidskonstanten og minnebruken.
### Ulemper:
* Komplisert algoritme med mange fallgruver i implementering sammenliknet med de andre.
* Treg worst-case
* Ustabil

![](/fig/Array-sorting.png)