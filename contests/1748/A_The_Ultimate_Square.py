import math

for _ in range(int(input())):
    n = int(input())
    print(math.ceil((n-1)/2) if n%2 == 0 else math.ceil(n/2))