def aranjare(v, n):
    start = 0
    sch = False
    while True:
        index_impar = index_par = -1
        for i in xrange(start, n):
            if v[i] % 2 == 0 and index_par == -1:
                    index_par = i
            elif v[i] % 2 != 0 and index_impar == -1:
                if index_impar == -1:
                    index_impar = i
            elif index_par != -1 and index_impar != -1:
                break
        if index_impar != -1 and index_par != -1:
            if index_par < index_impar:
                # numarul par este in stanga numarului impar
                # deci le schimbam intre ele
                aux = v[index_par]
                v[index_par] = v[index_impar]
                v[index_impar] = aux
                sch = True
            else:
                # numarul par este in dreapta numarului impar
                # deci ordinea este corecta. trecem la urmatorul
                # numar, adica cel din dreapta numarului impar
                start = index_impar + 1
                sch = True
        else:
            # sunt numai numere impare sau numai pare
            break
        if not sch:
            break


def main():
    v = [22, 38, 42, 7, 47, 25, 9]
    v = [22, 38, 42, 0, 0, 0, 8]
    v = [1, 3, 5, 7, 9, 19, 29]
    v = [22, 3, 5, 2, 9, 19, 29]
    v = [21, 37, 42, 7, 48, 25, 9]
    n = 7
    aranjare(v, n)
    print v


if __name__ == "__main__":
    main()
