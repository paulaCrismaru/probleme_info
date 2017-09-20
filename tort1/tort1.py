from __future__ import print_function


def citeste_din_fisier():
    with open('tort1.in', 'r') as f:
        lines = f.readlines()
        n = int(lines[0].split()[0])
        m = int(lines[0].split()[1])
        k = int(lines[0].split()[2])
        a = []
        for i in range(1, n + 1):
            a.append([int(x) for x in lines[i].split()])
        return n, m, k, a


def main():
    n, m, k1, a = citeste_din_fisier()

    # 1 N, 2 S, 3 E, 4 V
    v = [0, 0, 0, 0]
    k = 0
    v[0] = 0
    maxim = 0
    while k > -1:
        while v[k] <= 4:
            v[k] = v[k] + 1
            if (k == 0) or (v[k] >= v[k - 1] and k < c and v[k] <= 4):
                if k == k1 - 1:
                    print(v[:3])
                    s = 0
                    n = 0
                    capsuni = 0
                    for i in xrange(k1):
                        if v[i] == 1:
                            n += 1
                        elif v[i] == 2:
                            s += 1

                else:
                    k += 1
                    v[k] = 0
        k -= 1


if __name__ == "__main__":
    main()
