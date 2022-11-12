for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    count = 0
    sum_a = sum(a)
    if sum_a != 0 and 0 in a:
         a[a.index(0)] = -sum_a
    for i in range(1,n+1):
        if sum(a[:i]) == 0:
            count+=1
    print(count)

