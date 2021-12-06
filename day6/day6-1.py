with open('day6/day6.txt', 'r') as f:
    data = f.readlines()

data = data[0].split(',')

fish_list = []

class LanternFish:
    def __init__(self, age: int = 9):
        self._age = age

    def __str__(self):
        return "Lanternfish Age {}".format(self._age)

    def __int__(self):
        return self._age
    
    @property
    def age(self):
        return self._age

    def tick(self):
        if self._age == 0:
            self._age = 6
            fish_list.append(LanternFish())
            return
        self._age -= 1

for age in data:
    fish_list.append(LanternFish(int(age)))

for i in range(256):
    for fish in fish_list:
        fish.tick()

print(f'Total Fish: {len(fish_list)}')