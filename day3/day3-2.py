with open("day3/day3.txt") as f:
    data = f.readlines()

data = [string.replace('\n', '') for string in data]

def find_life_support_rating(data):
    
    def get_common_bit(data_list, index, search):
        
        # 1s, 0s
        count = [0, 0]

        for log in data_list:
            if log[index] == '1':
                count[0] += 1
            else:
                count[1] += 1

        if count[0] > count[1] and search == '1':
            return '1'
        elif count[0] < count[1] and search == '1':
            return '0'
        elif count[0] < count[1] and search == '0':
            return '1'
        elif count[0] > count[1] and search == '0':
            return '0'  
        elif count[0] == count[1]:
            return search
        else:
            raise Exception('Something went wrong')


    o2_rating = ""
    co2_rating = ""

    o2_data = data
    o2_bit_index = 0
    co2_data = data
    co2_bit_index = 0

    while len(o2_data) != 1:
        o2_data = list(filter(lambda x: x[o2_bit_index] == get_common_bit(o2_data, o2_bit_index, '1'), o2_data))
        o2_bit_index += 1

    o2_rating = o2_data[0]

    while len(co2_data) != 1:
        co2_data = list(filter(lambda x: x[co2_bit_index] == get_common_bit(co2_data, co2_bit_index, '0'), co2_data))
        co2_bit_index += 1

    co2_rating = co2_data[0]

    o2_decimal = int(o2_rating, 2)
    co2_decimal = int(co2_rating, 2)

    print(f'Oxygen Generator Rating: {o2_rating} (Decimal {o2_decimal})')
    print(f'CO2 Scrubber Rating: {co2_rating} (Decimal {co2_decimal})')
    return o2_decimal * co2_decimal
        
print(f'Life Support Rating: {find_life_support_rating(data)}')