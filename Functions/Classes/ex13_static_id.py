class Person:
    next_id = 0

    def __init__(self):
        Person.next_id += 1
        self.id = Person.next_id
        self.name = "anonymous"

    def show(self):
        print(F"name: {self.name}, id: {self.id}")


if __name__ == '__main__':
    p1 = Person()
    p1.name = "david"

    p1.show()

    p2 = Person()
    p2.name = "moshe"

    p2.show()
