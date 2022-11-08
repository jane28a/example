class NotEndlessRange:

    def __init__(self, limit):
        self.number = 0
        self.limit = limit


    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= self.limit:
            tmp = self.number
            self.number += 1
            return tmp
        else:
            raise StopIteration

if __name__ == '__main__':
    for element in NotEndlessRange(10):
        print(element)
    ne_range = NotEndlessRange(2)
    try:
        ne_iter = iter(ne_range)
        print(next(ne_iter))
        print(next(ne_iter))
        print(next(ne_iter))
        print(next(ne_iter))
    except StopIteration:
        pass
    example_str = 'Hello World'
    print(dir(example_str))

