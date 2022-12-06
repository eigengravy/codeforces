for _ in range(int(input())):
    input()
    n = list(map(int, input().split(" ")))
    ls = []
    rs = []
    for i in range(len(n)):
        if i == 0 or n[i-1] > n[i]:
            ls.append(i)
        if i == len(n)-1 or n[i+1] > n[i]:
            rs.append(i)
    count = 0
    for l in ls:
        for r in rs:
            if len(set(n[l:r+1])) == 1:
                count += 1
    
    if count == 1:
        print("YES")
    else:
        print("NO")