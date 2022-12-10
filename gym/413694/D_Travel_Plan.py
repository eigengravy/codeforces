_ = int(input())
coordinates = sorted(map(int, input().split(" ")))\

min = abs(coordinates[0]-coordinates[1])
count = 0
for i in range(len(coordinates)-1):
    if abs(coordinates[i]-coordinates[i+1]) < min:
        min = abs(coordinates[i]-coordinates[i+1])
        count = 1
    elif abs(coordinates[i]-coordinates[i+1]) == min:
        count += 1

print(min, count)