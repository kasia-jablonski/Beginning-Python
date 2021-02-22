import copy

class FilledList(list):
    def __init__(self, count, value, *args, **kwargs):
        super().__init__()
        for _ in range(count):
            self.append(copy.copy(value))

fl = FilledList(5, 2)               # returns [2, 2, 2, 2, 2]
fl2 = FilledList(2, [1, 2, 3])      # returns [[1, 2, 3], [1, 2, 3]]