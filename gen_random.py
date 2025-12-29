import random

NUM_COUNT = 5
MIN_VAL = 1
MAX_VAL = 3

def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield random.randint(begin, end)

if __name__ == '__main__':
    print(list(gen_random(NUM_COUNT, MIN_VAL, MAX_VAL)))
