with open('day8/day8.txt', 'r') as f:
    data = f.readlines()

data = [x.replace('\n', '') for x in data]

unique_nums = 0

for i in range(len(data)):
    data[i] = data[i].split(' ')
    data[i].remove('|')

    for chars in data[i][-4:]:
        if len(chars) in [2, 4, 3, 7]:
            unique_nums += 1

print(f'Unique Numbers: {unique_nums}')