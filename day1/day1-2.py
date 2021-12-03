import json

data = json.load(open('day1/day1.json'))["data"]

def find_greater_sliding(data):
    count = 0
    for i in range(len(data)):
        if i+3 >= len(data):
            return count
        if data[i+1] + data[i+2] + data[i+3] > data[i] + data[i+1] + data[i+2]:
            count += 1
    return count

print(find_greater_sliding(data))