def corect(a, b, c, x, y):
    return a * x * x + b * y * y == c


def diofantic(n, s, a, b, c):

    perechi = 0
    for index_x in range(n - 1):
        for index_y in range(index_x, n):
            x = s[index_x]
            y = s[index_y]
            if corect(a, b, c, x, y):
                perechi += 1
    return perechi


def main():
    n = 5
    s = [0, 3, 4, 5, 18]
    a = 1
    b = 1
    c = 25
    print diofantic(n, s, a, b, c)


if __name__ == '__main__':
    main()
