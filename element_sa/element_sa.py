def max_min_linie(m, a, l):
    min_l = max_l = a[l][0]
    for j in xrange(m):
        if a[l][j] < min_l:
            min_l = a[l][j]
        elif a[l][j] > max_l:
            max_l = a[l][j]
    return min_l, max_l


def max_min_coloana(n, a, c):
    min_c = max_c = a[0][c]
    for i in xrange(n):
        if a[i][c] < min_c:
            min_c = a[i][c]
        elif a[i][c] > max_c:
            max_c = a[i][c]
    return min_c, max_c


class MinMax():
    def __init__(self, minim, maxim):
        self.min = minim
        self.max = maxim


def corect(a, l, c, lin_details, col_details):
    if ((a[l][c] == col_details.min and a[l][c] == lin_details.max) or
       (a[l][c] == lin_details.min and a[l][c] == col_details.max)):
        return True
    return False


def nr_sa(a, n, m):
    l_details = []
    c_details = []
    nr = 0
    for i in xrange(n):
        min_l, max_l = max_min_linie(m, a, i)
        minmax = MinMax(min_l, max_l)
        l_details.append(minmax)
    for j in xrange(m):
        min_c, max_c = max_min_coloana(n, a, j)
        minmax = MinMax(min_c, max_c)
        c_details.append(minmax)
    for i in xrange(n):
        for j in xrange(m):
            if corect(a, i, j, l_details[i], c_details[j]):
                nr += 1
    print nr


def main():
    n = 2
    m = 6
    a = [
        [5, 2, 8, 4, 9, 3],
        [7, 1, 6, 3, 8, 5]
    ]
    nr_sa(a, n, m)


if __name__ == '__main__':
    main()
