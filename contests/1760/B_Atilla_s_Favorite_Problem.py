from functools import reduce


for _ in range(int(input())):
    input()
    print(ord(reduce(lambda x,y: y if y > x else x, list(input())))-96)