def sub(n):
    return int(n*(n+1)/2)

for _ in range(int(input())):
    n = int(input())
    s = input()
    d = {}
    for c in s:
        d[c] = d[c] + 1 if c in d else 1
    offset = max(d.values()) - len(d)
    print(sub(n) - offset * len(d))

