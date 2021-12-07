with open('day7/day7.txt', 'r') as f:
    data = f.readlines()

data = data[0].replace('\n', '').split(',')

data = [int(x) for x in data]

lowest = min(data)
highest = max(data)

fuel = None
position = None

for i in range(lowest, highest + 1):
    distance = 0
    for pos in data:
        distance += abs(int(pos) - i)
    if fuel == None:
        fuel = distance
    elif distance < fuel:
        fuel = distance
        position = i

print(f'Fuel: {fuel}')
print(f'Position: {position}')