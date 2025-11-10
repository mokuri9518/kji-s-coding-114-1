card_point = {
    'A': 1, '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 0.5, 'Q': 0.5, 'K': 0.5
}

class player:
    def __init__(self, name, bet, first_card):
        self.name = name
        self.point = card_point[first_card]
        self.bet = int(bet)
        self.price = 0
        self.bust = False

    def card_in(self):
        while True:
            if self.name == "Computer":
                c = input().strip()
                self.point += card_point[c]
                if self.point > 10.5:
                    self.bust = True
                break
            c = input().split()
            if len(c) == 1 or c[0] == "N":
                break
            self.point += card_point[c[1]]
            if self.point > 10.5:
                self.bust = True
                break
            if self.point == 10.5:
                break

player_count = int(input())
bets = input().split()
first_card = input().split()

players = [player("Computer", 0, first_card[0])]
for i in range(1, player_count + 1):
    players.append(player(f'Player{i}', bets[i - 1], first_card[i]))

for i in range(1, player_count + 1):
    players[i].card_in()

alive = [p for p in players[1:] if not p.bust and p.point < 10.5]
if not alive:
    pass
else:
    # 莊家要牌
    target = min(p.point for p in alive)
    while True:
        if players[0].point <= target and not players[0].bust:
            c = input().strip()
            players[0].point += card_point[c]
            if players[0].point > 10.5:
                players[0].bust = True
                break
            if players[0].point == 10.5:
                break
            target = min(p.point for p in alive)
        else:
            break


computer = players[0]
for p in players[1:]:
    if p.bust:
        p.price -= p.bet
        computer.price += p.bet
    elif p.point == 10.5:
        p.price += p.bet
        computer.price -= p.bet
    elif computer.bust:
        p.price += p.bet
        computer.price -= p.bet
    elif computer.point == 10.5:
        p.price -= p.bet
        computer.price += p.bet
    else:
        if computer.point >= p.point:
            p.price -= p.bet
            computer.price += p.bet
        else:
            p.price += p.bet
            computer.price -= p.bet


for i in range(1, player_count + 1):
    print(f"{players[i].name} {'+' if players[i].price > 0 else ''}{players[i].price}")
print(f"{computer.name} {'+' if computer.price > 0 else ''}{computer.price}")
