def c(y):
    if y%4==0:
        if y%100==0:
            if y%400==0:
                return "Leap Year"
            else:
                return "Common Year"
        else:
            return "Leap Year"
    return "Common Year"

i,s = int(input()),int(input())
print(c(i))
print(c(s))