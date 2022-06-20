from itertools import chain


def flat_generator(nested_list):
    cursor = 0
    data = list(chain.from_iterable(nested_list))
    end = len(data)
    while cursor < end:
        yield data[cursor]
        cursor += 1
