

class MyRange:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __len__(self):
        return self.end - self.start + 1

    def __getitem__(self, item):

        result = self.start + item

        if result > self.end:
            raise IndexError

        return result

