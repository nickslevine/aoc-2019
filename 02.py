f = open('02.txt')
line = f.readlines()
fields = line[0].split(',')
fields_int = list(map(int, fields))


def handle_01(a_list, i):
    position_1 = a_list[i + 1]
    position_2 = a_list[i + 2]
    position_3 = a_list[i + 3]
    a_list[position_3] = a_list[position_1] + a_list[position_2]


def handle_02(a_list, i):
    position_1 = a_list[i + 1]
    position_2 = a_list[i + 2]
    position_3 = a_list[i + 3]
    a_list[position_3] = a_list[position_1] * a_list[position_2]


# Part 1
position = 0
value = fields_int[position]

while value != 99:
    if value == 1:
        handle_01(fields_int, position)
    elif value == 2:
        handle_02(fields_int, position)
    position += 4
    value = fields_int[position]

print(fields_int[0])

# Part 2


def test_inputs(a, b):
    new_list = fields_int[:]
    new_list[1] = a
    new_list[2] = b
    position = 0
    value = new_list[position]
    while value != 99:
        if value == 1:
            handle_01(new_list, position)
        elif value == 2:
            handle_02(new_list, position)
        position += 4
        value = new_list[position]
    return new_list[0]


result = 0
for a in range(0, 100):
    if result == 19690720:
        break
    for b in range(0, 100):
        if result == 19690720:
            break
        print(f'{a},{b}')
        try:
            result = test_inputs(a, b)
            # print(result)
            if result == 19690720:
                break
        except:
            pass
print(f'Result: {fields_int[0]}')
print(f'100 * noun + verb = {100 * a + b}')

print(test_inputs(65, 77))
print(100 * 65 + 77)
