from itertools import chain


class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.data = list(chain.from_iterable(self.nested_list))

    def __iter__(self):
        self.cursor = - 1
        self.end = len(self.data)
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor >= self.end:
            raise StopIteration
        return self.data[self.cursor]
