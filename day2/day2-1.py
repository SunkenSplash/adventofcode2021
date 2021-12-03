import json

data = json.load(open('day2/day2.json'))["data"]

def find_product_of_positions(data):
    x = 0
    y = 0
    for move in data:
        if move.startswith("forward"):
            x += int(move[-1])
        elif move.startswith("down"):
            y += int(move[-1])
        elif move.startswith("up"):
            y -= int(move[-1])
    return x * y

print(find_product_of_positions(data))