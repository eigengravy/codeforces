for _ in range(int(input())):
    input()
    nums = list(map(int, input().split(" ")))
    print( "YES" if len(nums) == len(set(nums)) else "NO")