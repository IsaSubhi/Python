class Person:
    """
    age should be [0-120]
    """

    def __init__(self, age):
        # if not Person.is_valid_age(age):
        #     raise ValueError("age invalid")
        #
        # self._age = age
        self.set_age(age)

    @staticmethod
    def is_valid_age(age):
        return isinstance(age, int) and 0 <= age <= 120

    def __repr__(self):
        return f"Person({self._age})"

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if not Person.is_valid_age(new_age):
            raise ValueError("age invalid")

        self._age = new_age


if __name__ == '__main__':
    p1 = Person(100)
    print(p1)

    # p1.set_age(400)
    p1.set_age(p1.get_age() + 1)



