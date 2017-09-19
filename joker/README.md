### problema joker
http://campion.edu.ro/arhiva/index.php?page=problem&action=view&id=1007

1. Se sorteaza sirul
2. Se parcurge sirul sortat si se calculeaza lungimea sirului curent cu ajutorul unui parametru ce va tine pozitia in care incepe ultimul sir crescator si in acelasi timp calculam si lungimea maxima ce se cere.
3. Daca in sir avem jokerul
    a). in momentul in care diferenta a 2 vecini e 2, utilizam jokerul si il marcam ca si folosit
    b). daca am ajuns la sfarsitul unui sir consecutiv si nu am utilizat jokerul, verificam daca il putem lipi la vreun capat al sirului
4. Afisam maximul

De exp:
```
joker.in
    10 10
    5
    8
    9
    10
    11
    12
    13
    1
    16
    4
    0
```
```
a = [0, 1, 4, 5, 8, 9, 10, 11, 12, 13]
k = 11
n = 10
exista_joker = 1
```
### i = 2
```
lungime_sir_curent = 1
joker = 0
maxim = 1
```
         0  1  2  3  4  5   6  7   8   9   
    a = [0, 1, 3, 5, 8, 9, 10, 11, 12, 13]
            |  |
            u  i
            consecutive? NU
            jokerul neutilizat &&
             se portiveste intre 1 si 3 &&
             n permite (pentru [1, 3])
                lungime_sir_curent = 3 DA
                maxim = 3
                joker = 1
                i++

### i = 3
```
lungime_sir_curent = 3
joker = 1
maxim = 3
```
         0  1  2  3  4  5   6  7   8   9 
    a = [0, 1, 3, 5, 8, 9, 10, 11, 12, 13]
            |     |
            u     i
            consecutive? NU
            jokerul neutilizat NU
                lungime_sir_curent = 1
                jocker = 0
                u = i
                i++

### i = 3
```
lungime_sir_curent = 1
joker = 0
maxim = 3
```
         0  1  2  3  4  5   6  7   8   9 
    a = [0, 1, 3, 5, 8, 9, 10, 11, 12, 13]
               |  |
               u  i
            consecutive? NU
            jokerul neutilizat &&
             se portiveste intre 3 si 5 DA
             n permite (pentru [3, 5]) DA
                lungime_sir_curent = 3
                joker = 1
                i++

### i = 4
``` 
lungime_sir_curent = 3
joker = 1
maxim = 3
```
         0  1  2  3  4  5   6  7   8   9 
    a = [0, 1, 3, 5, 8, 9, 10, 11, 12, 13]
               |     |
               u     i
            consecutive? NU
            jokerul neutilizat NU
                lungime_sir_curent = 1
                jocker = 0
                u = i
                i++

### i = 4
``` 
lungime_sir_curent = 1
joker = 0
maxim = 3
```
         0  1  2  3  4  5   6  7   8   9 
    a = [0, 1, 3, 5, 8, 9, 10, 11, 12, 13]
                  |  |
                  u  i
            consecutive? NU
            jokerul neutilizat &&
             se portiveste intre 3 si 5 NU
                lungime_sir_curent = 1
                u = i
                i++

### i = 5
``` 
lungime_sir_curent = 1
joker = 0
maxim = 3
```
         0  1  2  3  4  5   6  7   8   9 
    a = [0, 1, 3, 5, 8, 9, 10, 11, 12, 13]
                     |  |
                     u  i
            consecutive? DA
                lungime_sir_curent = 2
                i++

### i = 6
``` 
lungime_sir_curent = 2
joker = 0
maxim = 3
```
         0  1  2  3  4  5   6  7   8   9 
    a = [0, 1, 3, 5, 8, 9, 10, 11, 12, 13]
                     |     |
                     u     i
            consecutive? DA
                lungime_sir_curent = 3
                i++


...


### i = 9
``` 
lungime_sir_curent = 5
joker = 0
maxim = 5
```
         0  1  2  3  4  5   6  7   8   9 
    a = [0, 1, 3, 5, 8, 9, 10, 11, 12, 13]
                     |                  |
                     u                  i
            consecutive? DA
                lungime_sir_curent = 6
                maxim = 6
                i++

### i = 10
``` 
lungime_sir_curent = 5
joker = 0
maxim = 5
```
*** while se opreste ***

    joker neutilizat &&
     n permite (pentru [8, 15]) DA
        lungime_sir_curent = 7
        maxim = 7

### maxim = 7
