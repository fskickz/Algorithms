# Søkestrukturer

En søkestruktur er en struktur for å finne objekter basert på et kriterium

### Map
Et map er et objekt som lagrer nøkkel, verdi par, og som kan bruke nøkkelen til å finne verdien. I python er dictionary et svar på map.

### Hashtabeller
Idéen til hashing er å bruke en hashfunksjon for å regne ut hvor i tabellen du skal slå opp for å finne en gitt nøkkel. Eit problem som lett kan oppstå da er kollisjon. Det vil si at hashfunksjonen gir den samme verdien til ulike nøkler. Det finnes flere løsninger på dette.

### Løsning 1: Spre dataene
Den enkleste måten å spre dataene på er ved å ta verdi%tabellstørrelse. Dersom du skal hashe strenger kan du konverter første bokstav i strengen til tallkoden for bokstaven og lagre den som hash_verdi. Deretter kan du gjøre dete for hver bokstav etter første bokstav:
* Gang hash_verdi med 31 eller 37.
* Gjør nåværende bokstav til et tall og lagre dette tallet til hash_verdi.
* Sett hash_verdi lik hash_verdi % ønsket-tabellstørrelse.


### Løsning 2: Open addressing (Håndter de kollisjonene som likevel oppstår)
**Fyllingsgrad**: Tall fra 0.0(tom) til 1.0(full) som sier hvor mange av cellene som har en verdi. Kan regnes ut som fyllingsgrad = antall elementer / størrelsen til tabellen.

**Lineær prøving**: Dersom plassen er opptatt, prøver vi neste plass helt til vi finner en ledig plass. Dette kan bli veldig dårlig etter hvert som fyllingsgraden blir stor ettersom at vi må leite lengre etter ledig plass.

**Kvadratisk prøving**: For å redusere clustering, bruker vi enn sekvens som er kvadratisk: K, K+1<sup>2</sup>, K+2<sup>2</sup>, K+3<sup>2</sup> osv... Generell formel K<sub>i</sub> = K<sub>i-1</sub> + 2*i + 1.
Problemet nå er at verdier som kolliderer vil prøve di samme stedene. Dette kalles sekundær clustering og er et marginalt problem.

### Løsning 3: Chaining:
Tar elementer som linker til same plass og plasserer dem i ei lenket liste. En plass i tabellen inneholder ikke en verdi lenger, men en lenket liste med flere verdier.

Kjøretida for chaining vil være O(1+loading factor) i både et suksessfullt og mislykket søk. 

### Kjøretid:

| Average |           |          | Worst  |           |          |
|---------|-----------|----------|--------|-----------|----------|
| Search  | Insertion | Deletion | Search | Insertion | Deletion |
| O(1)    | O(1)      | O(1)     | O(n)   | O(n)      | O(n)     |