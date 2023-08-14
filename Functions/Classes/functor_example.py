class NumberSum:
    def __init__(self, *args):
        self.numbers = list(args)

    def __call__(self, *args):
        print(sum(self.numbers) + sum(args))


if __name__ == '__main__':
    ns = NumberSum(10, 20, 30)

    ns()

    ns(1, 700, 8000)

    NumberSum(1, 2, 3)(7000)
