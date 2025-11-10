def bowling_score():
    rolls = []  
    try:
        while True:
            rolls.append(int(input()))
    except EOFError:
        pass
    total = 0
    i = 0
    for frame in range(1, 3):
        if rolls[i] == 10:
            total += 10 + rolls[i+1] + rolls[i+2]
            i += 1
        elif rolls[i] + rolls[i+1] == 10:
            total += 10 + rolls[i+2]
            i += 2
        else:
            total += rolls[i] + rolls[i+1]
            i += 2
    if rolls[i] == 10:
        total += 10 + rolls[i+1] + rolls[i+2]
    elif rolls[i] + rolls[i+1] == 10:
        total += 10 + rolls[i+2]
    else: 
        total += rolls[i] + rolls[i+1]
    print(total)

if __name__ == "__main__":
    bowling_score()
