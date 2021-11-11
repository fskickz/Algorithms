# Analyse av algoritmer / aritmetisk analyse

## Time complexity
* Tiden en algoritme bruker
* Undersøker tre scenarioer
    1. Worst case
    2. Average case
    3. Best case

### Worst case:
Worst case er casen der algoritmen bruker max antall operasjoner for å gjennomføres

### Average case:
Average case er gjennomsnittet av alle mulige operasjoner

### Best case:
Best case er casen der algoritmen bruker minst mulig operasjoner for å gjennomføres. For eksempel å finne først element i ei liste.

--- 

## Notasjoner
Big O : Worst case 

Ω (Omega) : Best case

Θ (Theta) : Average case

O(1) : Ingen loop, rekursjon eller kall til annen funksjon som ikkje er konstant. Den kan loope men kun et konstant antall ganger.

O(n) : Loop er O(n) dersom den blir inkrementa elle dekrementa med et konstant antall 

O(n^c) : Nested loops er O(n^c) der c er antall ganger du nester.

O(log n) : En loop som blir dividert/multiplisert med en konstant er O(log n)

O(log log n) : Dersom en loop blir økt/redusert eksponensielt er det O(log log n)

---

![](/fig/Big-o.png)

Kjøretid til datastrukturer

![](/fig/Common-DS.png)