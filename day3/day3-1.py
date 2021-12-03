with open("day3/day3.txt") as f:
    data = f.readlines()

data = [string.replace('\n', '') for string in data]

def find_power_consumption(data):
   
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
   
    for log in data:
        for i, char in enumerate(log):
            counts[i] += int(char)
    
    gamma = "".join(['1' if counts[i] >= 500 else '0' for i in range(len(counts))])
    epsilon = "".join(['0' if gamma[i] == '1' else '1' for i in range(len(gamma))])
    gamma_decimal = int(gamma, 2)
    epsilon_decimal = int(epsilon, 2)

    print(f'Totals: {counts}')
    print(f'Gamma: {gamma} (Decimal {gamma_decimal})')
    print(f'Epsilon: {epsilon} (Decimal {gamma_decimal})')
    return gamma_decimal * epsilon_decimal

print(f'Power Consumption: {find_power_consumption(data)}')