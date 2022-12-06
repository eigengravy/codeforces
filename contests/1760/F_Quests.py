import math

for _ in range(int(input())):
    n,c,d = map(int, input().split(" "))
    q = sorted(map(int, input().split(" ")), reverse=True)
    q_max = q[0]
    if (c > q_max * d):
        print("Impossible")
    elif (q_max > c):
        print("Infinity")
    else:
        k = d-1
        while(k > 0):
            if sum(q[:k])*d/k > c:
                print(k)
                break 
            k -= 1
        else:
            print(0)
