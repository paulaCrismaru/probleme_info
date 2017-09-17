from __future__ import print_function


def citeste_din_fisier():
    with open('piticot.in', 'r') as f:
        lines = f.readlines()
        A = int(lines[0].split()[0])
        B = int(lines[0].split()[1])
        C = int(lines[0].split()[2])
        x0 = int(lines[0].split()[3])

        nr_j = int(lines[1].split()[0])
        nr_c = int(lines[1].split()[1])

        # echivalentul cu declararea globala a lui c si p
        c = [0] * nr_c
        p = [0] * nr_c
        for i in xrange(2, nr_c):
            # = cu valoarea citita din fisier
            c[i] = int(lines[i].split()[0])
            p[i] = int(lines[i].split()[1])

        return A, B, C, x0, nr_j, nr_c, c, p


def main():
    # cand citesc datele de intrare, pe c[0], c[nr_c - 1], p[0], p[nr_c - 1]
    # pun 0 pentru ca pe pozitia 0 se afla cerculetul de start si pe
    # pozitia nr_c - 1 se afla cerculetul de finish, cerculete ce nu au actiuni
    A, B, C, x0, nr_j, nr_c, c, p = citeste_din_fisier()

    # tabla tine pozitiile curente ale jucatorului i
    # tabla[i] = numarul cerculetului in care se afla pionul
    #            jucatorului i
    # initial toti pionii sunt pe cerculetul de start (1)
    tabla = []
    for i in xrange(nr_c):
        # tabla[i] = 1
        tabla.append(1)

    # Xi+1 = (A * Xi + B) % C
    xi = x0
    sfarsit_joc = 0
    castigator = -1
    jucator = 1
    mutari = 0
    aruncare_zar = 1

    while sfarsit_joc == 0:

        # nu arunc cu zarul decat daca mi se permite.
        # exista posibilitatea ca cerculetul pe care ma aflu
        # sa aiba o actiune. de exp daca am ajuns pe un cerculet
        # care zice sa ma deplasez undeva pe tabla, dupa ce ma
        # deplasez e posibil ca cerculetul pe care am ajuns sa
        # aiba si el o actiune. in acest caz, rezolv actiunea
        # si mai apoi, daca noul cerculet pe care am ajuns nu are
        # nicio actiune, se poate arunca din nou cu zarul
        if aruncare_zar == 1:
            zar = (A * xi + B) % C
            # cerculetul curent inainte de mutare = tabla[jucator]
            cerculet = tabla[jucator] + zar
            # mut pionul
            tabla[jucator] = cerculet
            # numae mutarea
            mutari += 1
            # Xi+1 = (A * Xi + B) % C
            xi = zar

        # daca am ajuns in ultimul cerculet sau l-am depasit jocul s-a
        # terminat
        if cerculet >= nr_c:
            sfarsit_joc = 1
            castigator = jucator
        else:
            if c[cerculet] == 0 and p[cerculet] == 0:
                # cerculetul nu are nicio actiune, trec la jucatorul urmator
                # si zarul poate fi aruncat
                jucator += 1
                aruncare_zar = 1
            else:
                if c[cerculet] == 1:
                    if p[cerculet] > 0:
                        # mut pionul p[cerculet] cerculete
                        cerculet = cerculet + p[cerculet]
                        tabla[jucator] = cerculet
                        mutari += 1
                        # nu arunc cu zarul pana cand sunt sigur ca
                        # cerculetul pe care ma aflu nu are nicio actiune.
                        aruncare_zar = 0
                        # acuma o iau de la capat (linia 49)
                    else:
                        if p[cerculet] < 0:
                            cerculet = cerculet - (-p[cerculet])
                            if cerculet < 1:
                                cerculet = 1
                            tabla[jucator] = cerculet
                            mutari += 1
                            # nu arunc cu zarul pana cand cerculetul pe care
                            # ma aflu nu are nicio actiune
                            aruncare_zar = 0
                        else:
                            # else inseamna ca p[cerculet] == 0
                            # jucatorul trebuie sa mai dea o data cu zarul.
                            # nu modific jucatorul, acesta ramane acelasi
                            # si cand o va lua de la capat (linia 48) se va
                            # da din nou cu zarul
                            aruncare_zar = 1

        # daca numarul jucatorului > nr_j inseamna ca s-a terminat o runda de
        # joc si va fi randul jucatorului 1 din nou
        if jucator > nr_j:
            jucator = 1

    print(castigator, mutari)


if __name__ == "__main__":
    main()
