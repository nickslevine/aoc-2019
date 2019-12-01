def read_input(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    stripped = map(lambda x: x.strip(), lines)
    return list(stripped)


def map_ints(list_name):
    return list(map(int, list_name))


def print_answers(answer_01, answer_02):
    print(f'Answer 1: {answer_01}')
    print(f'Answer 2: {answer_02}')
