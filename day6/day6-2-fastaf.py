import time

DAYS = 256

start_time = time.time()

with open('day6/day6.txt', 'r') as f:
    data = f.readlines()

fish_list = data[0].split(',')

fish_list = [int(x) for x in fish_list]

fish_counts = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0
}

for fish in fish_list:
    fish_counts[fish] += 1

for i in range(DAYS):

    birthing_fish = fish_counts[0]

    fish_counts[0] = fish_counts[1]
    fish_counts[1] = fish_counts[2]
    fish_counts[2] = fish_counts[3]
    fish_counts[3] = fish_counts[4]
    fish_counts[4] = fish_counts[5]
    fish_counts[5] = fish_counts[6]
    fish_counts[6] = fish_counts[7]
    fish_counts[7] = fish_counts[8]
    fish_counts[8] = birthing_fish
    fish_counts[6] += birthing_fish

total_fish = sum(fish_counts.values())

end_time = time.time()

print(f'Total Fish: {total_fish}')
print(f'Execution Time (s): {end_time - start_time}')