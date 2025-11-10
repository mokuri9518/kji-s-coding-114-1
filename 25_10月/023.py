class player:
    def __init__(self):
        self.card=input().split()
        self.a=''
        self.sort_card()
    def sort_card(self):
        dic = {}
        for c in self.card:
            if c == 'Joker':
                continue
            dic.update({c[1]:dic.get(c[1],[])+[c]})
        for k in dic:
            if len(dic[k])>1:
                self.card.remove(f'H{k}')
                self.card.remove(f'C{k}')

player1 = player()
player2 = player()
computer = player()
players = [player1, player2, computer]
for p in players:
    p.a = input()

for i in range(3):
    if players[i].a not in players[i+1 if i<2 else 0].card:
        print('Error')
        exit()
    players[i+1 if i<2 else 0].card.remove(players[i].a)
    players[i].card.append(players[i].a)
    players[i].sort_card()
for p in players:
    print(' '.join(p.card))

