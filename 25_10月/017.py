fl = input().split()
pt = input().split()
HCP_List = {"A":4,"K":3,"Q":2,"J":1}
for i in range(101):
    HCP_List.update({str(i):0})
HCP = sum(HCP_List[x] for x in pt )
print(f"HCP: {HCP}")
Spade,Heart,Diamond,Club = fl.count("S"),fl.count("H"),fl.count("D"),fl.count("C")
Total = HCP + (2 if Spade>4 or Heart>4 or Diamond>4 or Club>4 else 0)
print(f"Total Points: {Total}")
print(f"Distribution (S-H-D-C): {Spade}-{Heart}-{Diamond}-{Club}")
Stop_Suit = []
for i in range(len(pt)):
    if pt[i] == 'A':
        Stop_Suit.append(fl[i])
    elif pt[i] == 'K' and fl.count(fl[i])>1:
        Stop_Suit.append(fl[i])
    elif pt[i] == 'Q' and fl.count(fl[i])>2:
        Stop_Suit.append(fl[i])
order = {'S': 4, 'H': 3, 'D': 2, 'C': 1}
Stop_Suit = sorted(set(Stop_Suit), key=lambda s: -order[s])
print(f"Stopped Suits: {list(set(Stop_Suit))}")
Open_Bid = "void"
if Total<8:
    Open_Bid = "Pass"
elif Total>=15:
    Open_Bid = "Strong Open"
else:
    count = {'S': Spade, 'H': Heart, 'D': Diamond, 'C': Club}
    max_len = max(count.values())
    longest = [s for s, n in count.items() if n == max_len]
    best = max(longest, key=lambda s: order[s])
    suit_name = {"S": "Spade", "H": "Heart", "D": "Diamond", "C": "Club"}[best]
    Open_Bid = f"Open {suit_name}"

print(f"Opening Bid: {Open_Bid}")