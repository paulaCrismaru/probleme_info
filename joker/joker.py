from __future__ import print_function


def citeste_din_fisier():
    with open('joker.in', 'r') as f:
        lines = f.readlines()
        n, k = int(lines[0].split()[0]), int(lines[0].split()[1])
        a = []
        for i in xrange(1, k + 1):
            a.append(int(lines[i]))
        return n, k, a


def main():
    n, k, a = citeste_din_fisier()

    # sorteaza a
    a = sorted(a)

    # vector ce va tine ultimul element al secventelor consecutive
    # (Ultimul Element)
    ue = []
    # vector ce va tine lungimile sirurilor cu capetele din ue (Lungime Sir)
    ls = []

    if a[0] == 0:

        # cautam capetele secventelor consecutive din a si completam ue si ls
        # in acelasi timp calculam si maximul din ue.
        # pentru asta vom avea nevoie de elementul precedent si de lungimea
        # curenta a sirului
        lc = 1
        prec = a[1]
        maxim = 0
        index_ue = 0
        # for(i=2, i<k; i++)
        for index in xrange(2, k):
            if a[index] == prec + 1:
                lc += 1
            else:
                if lc > maxim:
                    maxim = lc
                # ue[index_ue] = prec
                ue.append(prec)
                # ls[index_ue] = lc
                ls.append(lc)
                index_ue += 1
                lc = 1
            prec = a[index]
        # dupa ce for-ul se termina, ultimul element nu va fi adaugat pt ue in
        # for adaugam elementul prec, nu elementul curent. pentru asta va
        # trebui sa adaugam de mana ultimul element in ue si ls
        # ue[index_ue] = prec
        ue.append(prec)
        # ls[index_ue] = lc
        ls.append(lc)
        if lc > maxim:
            maxim = lc

        # verificam daca exista 2 subsiruri consecutive care impreuna cu
        # jokerul sa formeze un subsir consecutiv mai lung decat cel care mai
        # lung subsir consecutiv gasit mai sus

        # for(i=1, i<index_ue; i++)
        for index in xrange(1, index_ue):
            # verificam daca posibilul joker ar fi < n, adica daca avem a si b
            # 2 subsiruri, ultimul element al lui a sa fie mai mic decat n
            if (n > ue[index - 1]):
                # verificam daca diferenta dintre sfarsitul primului subsir si
                # inceputul al 2 lea subsir este de 2
                if ue[index] - ls[index] == ue[index - 1] + 1:
                    # calculam lungimea noului subsir format din cele 2+joker
                    lungime_sir = ls[index] + ls[index - 1] + 1
                    if maxim < lungime_sir:
                        maxim = lungime_sir
    elif a[0] != 0:
        # aici doar cautam subsirul consecutiv de lungime maxima
        lc = 1
        prec = a[0]
        maxim = 0
        # for(i=1, i<k; i++)
        for index in xrange(1, k):
            if a[index] == prec + 1:
                lc += 1
            else:
                if lc > maxim:
                    maxim = lc
                lc = 1
            prec = a[index]
        if lc > maxim:
            maxim = lc

    # cout<<maxim
    print(maxim)


if __name__ == "__main__":
    main()
