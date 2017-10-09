def mutare(n, v, start):
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
        aux = v[index_par]
        v[index_par] = v[index_impar]
        v[index_impar] = aux
        return True, index_par + 1
    return False, index_par + 1


def aranjare(v, n):
    start = 0
    while True:
        sch, start = mutare(n, v, start)
        if not sch:
            break


def main():
    v = [22, 38, 42, 7, 47, 25, 9]
    v = [22, 38, 42, 0, 0, 0, 8]
    v = [1, 3, 5, 7, 9, 19, 29]
    v = [22, 3, 5, 2, 9, 19, 29]
    n = 7
    aranjare(v, n)
    print v


if __name__ == "__main__":
    main()
