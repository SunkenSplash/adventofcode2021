import json

data = json.load(open('day2/day2.json'))["data"]

def find_product_of_positions_with_aim(data):
    x = 0
    y = 0
    aim = 0
    for move in data:
        if move.startswith("forward"):
            x += int(move[-1])
            if aim != 0:
                y += int(move[-1]) * aim
        elif move.startswith("down"):
            aim += int(move[-1])
        elif move.startswith("up"):
            aim -= int(move[-1])
    return x * y

print(find_product_of_positions_with_aim(data))