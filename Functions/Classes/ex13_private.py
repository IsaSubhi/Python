class Person:
    """
    age should be [0-120]
    """
    def __init__(self, age):
        if not Person.is_valid_age(age):
            raise ValueError("age invalid")

        self.age = age

    @staticmethod
    def is_valid_age(age):
        return isinstance(age, int) and 0 <= age <= 120

    def __repr__(self):
        return f"Person({self.age})"


if __name__ == '__main__':
    p1 = Person(100)
    print(p1)
    p1.age = 200
