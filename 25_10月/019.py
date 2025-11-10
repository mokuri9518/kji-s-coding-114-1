import re
class Class:
    def __init__(self):
        self.times = []
        self.name = input()
        self.time=int(input())
        for _ in range(self.time):
            self.times.append(input())
        self.error_detect()
    def error(self,e=None)->None:
        try:
            while True:
                input()
        except EOFError:
            pass
        print(-1)
        if e:
            print(e)
        exit()
    def error_detect(self)->None:
        pattern = r'^[A-Za-z ]+\d{4}$'
        if not re.match(pattern, self.name):
            self.error()
        if self.time not in range(1,4):
            self.error()
        for time in self.times:
            if time[0] not in '12345' or time[1] not in '123456789abc':
                self.error()

def conflict(*args: Class)->None:
    timetable = {}
    order = {args[i].name:i for i in range(len(args))}
    for c in args:
        for t in c.times:
            timetable.update({t: timetable.get(t, []) + [c.name]})
    conflicts = []
    for k, v in timetable.items():
        if len(v) > 1:
            conflicts += [(v[i], v[j], k) for i in range(len(v)) for j in range(i+1, len(v))]
    conflicts.sort(key=lambda x: (order[x[0]], order[x[1]], x[2]))
    if conflicts:
        for c1, c2, t in conflicts:
            printe(class1=c1, class2=c2, time=t)
    else:
        print("correct")

def printe(class1, class2, time):
    print(f"{class1},{class2},{time}")

def main():
    counts = int(input())
    classes = [Class() for _ in range(counts)]
    conflict(*classes)

if __name__ == "__main__":
    main()