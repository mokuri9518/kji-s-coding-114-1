class Class:
    def __init__(self):
        self.s = int(input())
        self.t1 = input().strip()
        self.t2 = input().strip()

def conflict(*args: Class):
    TimeTable = [[[] for _ in range(9)] for _ in range(5)]
    conflicts = []

    for c in sorted(args, key=lambda x: x.s):
        for t in [c.t1, c.t2]:
            day = int(t[0]) - 1
            period = int(t[1]) - 1
            for exist in TimeTable[day][period]:
                c1, c2 = sorted([exist, c.s])
                conflicts.append((c1, c2, t))
            TimeTable[day][period].append(c.s)
    conflicts.sort(key=lambda x: (x[0], x[1], int(x[2])))
    if conflicts:
        for c1, c2, t in conflicts:
            print(f"{c1} and {c2} conflict on {t}")
    else:
        print("correct")

c1 = Class()
c2 = Class()
c3 = Class()
conflict(c1, c2, c3)
