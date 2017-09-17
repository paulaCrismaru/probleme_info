### problema joker
http://campion.edu.ro/arhiva/index.php?page=problem&action=view&id=1007

1. Se sorteaza sirul si se calculeaza lungimea celui mai lung subsir crescator
2. Daca in sir nu avem jokerul, afisam maximul de la 1.
3. Daca in sir avem jokerul, cream 2 vectori ce vor tine ultimul element al unui subsir (ue) si lungimea subsirului (ls).
4. Parcurgem ue si verificam daca exista 2 subsiruri consecutive alaturare care pot fi unite cu un joker
5. Afisam maximul

De exp:
a = 6, 2, 4, 7, 0

a = 0, 2, 4, 6, 7

maxim = 2 (6 si 7)

1).

        ======          
        ue  ls              
        ====== 
        2   1   \
        4   1   /    
        7   2      

        ======          
        ue  ls                jokerul
        ======                 \/ 
    ->  2   1   \ 4 - 1 == 2 + 1 ?
    ->  4   1<- /     /\
        7   2      1 element in subsirul cu capatul 4 (din ls)

        ======          
        ue  ls               
        ======                
        2   1<- \ 4 - 1 == 2 + 1 DA
        4   1<- / 
        7   2      maxim = 1 + 1 + 1 = 3, 1 jokerul


2).

        ======          
        ue  ls
        ======
        2   1 
        4   1  \
        7   2  /   

        ======          
        ue  ls
        ======                jokerul
        2   1                   \/  
    ->  4   1   \  7 - 2 == 4 + 1 ?
    ->  7   2<- /   
     
        ======          
        ue  ls
        ======
        2   1
        4   1<-  \  7 - 2 == 4 + 1 DA
        7   2<-  /  maxim =  1 + 2 + 1, 1 jokerul
