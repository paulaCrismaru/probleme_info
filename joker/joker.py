from __future__ import print_function


def citeste_din_fisier():
    with open('joker.in', 'r') as f:
        lines = f.readlines()
        n, k = int(lines[0].split()[0]), int(lines[0].split()[1])
        a = []
        for i in range(1, k + 1):
            a.append(int(lines[i]))
        return n, k, a


def main():
    n, k, a = citeste_din_fisier()

    # sorteaza a
    a = sorted(a)

    # vom parcurge sirul numerelor sortate si vom retine in u pozitia de
    # inceput al ultimului sir consecutiv intalnit si vom numara in acelasi
    # timp si elementele acestuia
    if a[0] != 0:
        inceput = 1
        u = 0
        exista_joker = 0
    else:
        inceput = 2
        u = 1
        exista_joker = 1
    print(a)
    joker = 0
    lungime_sir_curent = 1
    maxim = 1
    i = inceput
    while i < k:
        if a[u] + lungime_sir_curent == a[i]:
            # daca elementul curent (a[i]) este element
            # al subsirului consecutiv ce incepe cu a[u]
            # atunci in numaram
            lungime_sir_curent += 1
        elif (exista_joker == 1 and joker == 0 and a[i] - 1 < n and
              a[u] + lungime_sir_curent + 1 == a[i]):
                # daca exista 0 in sirul de numere &&
                # daca jokerul nu a fost deja folosit &&
                # daca n permite utilizarea jokerului &&
                # daca se potriveste intre cele 2 subsiruri
                # (a[u] + lungime_sir_curent + 1 == a[i])
                lungime_sir_curent += 2
                # am folosit jokerul
                joker = 1
        else:
            # am ajuns la sfarsitul unui sir crescator unde a[i] nu mai
            # apartine acestuia
            if exista_joker == 1 and joker == 0:
                # exista posibilitatea ca jockerul sa existe si
                # sa nu se fi folosit pana acum, deci putem sa il
                # lipim la sirul ce abia s-a terminat, in fata
                # sau in spate
                if a[u] - 1 < n or a[i - 1] + 1 < n:
                    lungime_sir_curent += 1
                    if lungime_sir_curent > maxim:
                        # daca nu facem aceasta verificare acum,
                        # lungime_sir_curent se va pierde (devine 1)
                        maxim = lungime_sir_curent
            if exista_joker and joker == 1:
                u = i - 1
                # i trebuie sa ramana acelasi, sa compare noile subsiruri
                # i - 1 anuleaza i + 1
                i = i - 1
            else:
                u = i
            lungime_sir_curent = 1
            joker = 0

        if lungime_sir_curent > maxim:
            maxim = lungime_sir_curent

        i += 1

    if exista_joker == 1 and joker == 0:
        # daca vectorul sortat se termina cu un si crescator, verificarea
        # de la linia 54 nu mai are loc, asa ca trebuie sa o facem dupa ce
        # for-ul se termina
        if a[i - 1] + 1 < n or a[u] - 1 < n:
            lungime_sir_curent += 1
            if lungime_sir_curent > maxim:
                maxim = lungime_sir_curent

    print(maxim)


if __name__ == "__main__":
    main()
