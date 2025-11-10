def compute(password: str) -> float:
    total = 0.0
    integers = 0
    for char in password:
        if char.islower():
            total += 1
        elif char.isupper():
            total += 3
        elif char.isdigit():
            total += 2
            integers += 1
        elif char in r'{ ~!@#$%^&*<>_+=}':
            total += 4.5
    if len(password) > 8:
        total += len(password) - 8
    if password.find('1234')>0:
        total -= 10
    if integers >= 5:
        add = 10
        last_char = ''
        for c in password:
            if c.isdigit() and last_char.isdigit():
                add = 0
            last_char = c
        total += add
    return total
count = int(input())
passwords = [input() for _ in range(count)]

rank = {p:compute(p) for p in passwords}
rank = sorted(rank.items(), key=lambda x: (-x[1], x[0]),reverse=False)
print(f'{rank[0][0]} {rank[0][1]:.1f}')
print(f'{rank[-1][0]} {rank[-1][1]:.1f}')