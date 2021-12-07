with open('day7/day7.txt', 'r') as f:
    data = f.readlines()

data = data[0].replace('\n', '').split(',')

data = [int(x) for x in data]

lowest = min(data)
highest = max(data)

least_fuel = None
position = None

for i in range(lowest, highest + 1):
    fuel = 0
    for pos in data:
        distance = abs(pos - i)
        # fuel consumption is equal to half of the distance squared plus half of the distance (0.5x^2 + 0.5x)
        fuel += 0.5*(distance*distance) + 0.5*distance
    if least_fuel == None:
        least_fuel = fuel
    elif fuel < least_fuel:
        least_fuel = fuel
        position = i

print(f'Fuel: {round(least_fuel)}')
print(f'Position: {position}')