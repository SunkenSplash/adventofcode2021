import json

data = json.load(open('day1/day1.json'))["data"]

def find_greater(data):
    count = 0
    for i in range(len(data)):
        if data[i] > data[i-1]:
            count += 1
    return count

print(find_greater(data))