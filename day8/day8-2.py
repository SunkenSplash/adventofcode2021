with open('day8/day8.txt', 'r') as f:
    data = f.readlines()

with open('day8/keys.txt', 'r') as f:
    combos = f.readlines()

combos = [x.replace('\n', '').lower() for x in combos]

data = [x.replace('\n', '') for x in data]

nums = []

for i in range(len(data)):

    data[i] = data[i].split(' | ')
    data_input = data[i][0].split(' ')
    data_output = data[i][1].split(' ')

    num_key = None

    for key in combos:

        rand_map = {
            'a': key[0],
            'b': key[1],
            'c': key[2],
            'd': key[3],
            'e': key[4],
            'f': key[5],
            'g': key[6]
        }
        
        temp = []
        for chars in data_input:
            num_map = [rand_map[char] for char in chars]
            num_map.sort()
            if num_map == ['a', 'b', 'c', 'd', 'e', 'g']:
                temp.append(0)
            elif num_map == ['a', 'b']:
                temp.append(1)
            elif num_map == ['a', 'c', 'd', 'f', 'g']:
                temp.append(2)
            elif num_map == ['a', 'b', 'c', 'd', 'f']:
                temp.append(3)
            elif num_map == ['a', 'b', 'e', 'f']:
                temp.append(4)
            elif num_map == ['b', 'c', 'd', 'e', 'f']:
                temp.append(5)
            elif num_map == ['b', 'c', 'd', 'e', 'f', 'g']:
                temp.append(6)
            elif num_map == ['a', 'b', 'd']:
                temp.append(7)
            elif num_map == ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
                temp.append(8)
            elif num_map == ['a', 'b', 'c', 'd', 'e', 'f']:
                temp.append(9)
            else:
                break

        if len(temp) == 10:
            num_key = rand_map

    out_temp = []
    for chars in data_output:
        num_map = [num_key[char] for char in chars]
        num_map.sort()
        if num_map == ['a', 'b', 'c', 'd', 'e', 'g']:
            out_temp.append(0)
        elif num_map == ['a', 'b']:
            out_temp.append(1)
        elif num_map == ['a', 'c', 'd', 'f', 'g']:
            out_temp.append(2)
        elif num_map == ['a', 'b', 'c', 'd', 'f']:
            out_temp.append(3)
        elif num_map == ['a', 'b', 'e', 'f']:
            out_temp.append(4)
        elif num_map == ['b', 'c', 'd', 'e', 'f']:
            out_temp.append(5)
        elif num_map == ['b', 'c', 'd', 'e', 'f', 'g']:
            out_temp.append(6)
        elif num_map == ['a', 'b', 'd']:
            out_temp.append(7)
        elif num_map == ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            out_temp.append(8)
        elif num_map == ['a', 'b', 'c', 'd', 'e', 'f']:
            out_temp.append(9)
        else:
            break

    if len(out_temp) == 4:
        print(f'Found row {i + 1} with key {"".join(num_key.values())}: {out_temp}')
        nums.append(int(''.join([str(x) for x in out_temp])))

print(f'Sum: {sum(nums)}')