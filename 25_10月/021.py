def make_row(i: int) -> str:
    return ''.join(str(x) for x in range(1, i)) + str(i) + ''.join(str(x) for x in range(i - 1, 0, -1))


def main():
    M = int(input().strip())
    N = int(input().strip())
    if not (3 <= N <= 50):
        print("Row Error")
        return
    if M == 1:
        for i in range(1, N + 1):
            print(make_row(i))
    elif M == 2:
        for i in range(1, N + 1):
            row = make_row(i)
            spaces = '_' * (N - i)
            print(f"{spaces}{row}{spaces}")
    elif M == 3:
        for i in range(1, N + 1):
            spaces = '_' * (i - 1)
            row = make_row(N - i + 1)
            print(f"{spaces}{row}{spaces}")
    else:
        print("Row Error")


if __name__ == "__main__":
    main()
