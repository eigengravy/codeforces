for _ in range(int(input())):
    nums = sorted(map(int, input().split(" ")))
    print("YES" if (nums[0] + nums[1] == nums[2]) else "NO")
