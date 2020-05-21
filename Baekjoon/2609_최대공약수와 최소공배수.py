import sys

def main():
    for line in sys.stdin:
        N, M = map(int, line.strip().split())

        if N < M:
            a, b = (M, N)
        else:
            a, b = (N, M)

        while (b != 0):
            nmg = a % b
            a = b
            b = nmg

        gcd = a
        lcm = int(N * M / gcd)

        print(gcd, lcm)


if __name__ == '__main__':
    main()
