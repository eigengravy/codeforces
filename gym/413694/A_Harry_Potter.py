d = {}
for _ in range(int(input())):
    i = input()
    d[i] = d[i] + 1 if i in d else 1
    print("YES" if d[i] > 1 else "NO")
