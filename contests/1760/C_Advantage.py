for _ in range(int(input())):
    input()
    strenghts = list(map(int, input().split(" ")))
    first, second = 0,0
    for i in strenghts:
        if i >= first:
            second = first
            first = i
        elif i >= second:
            second = i
    print(" ".join(map(str, [(i-first) if i < first else (i-second) for i in strenghts])))