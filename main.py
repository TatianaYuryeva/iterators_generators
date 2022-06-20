from iterators import FlatIterator
from generators import flat_generator

NESTED_LIST = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]


if __name__ == '__main__':

    for i in FlatIterator(NESTED_LIST):
        print(i)
    flat_list = [item for item in FlatIterator(NESTED_LIST)]
    print(flat_list)

    for item in flat_generator(NESTED_LIST):
        print(item)
        