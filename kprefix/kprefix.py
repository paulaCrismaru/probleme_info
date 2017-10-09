def kprefix(n, k):
    cn = n
    nr = 0
    while cn != 0:
        nr += 1
        cn /= 10
    print n / (10 ** (nr - k))


def main():
    kprefix(27594, 3)


if __name__ == "__main__":
    main()
