class Person:
    """
    age should be [0-120]
    """

    def __init__(self, age):
        self.age = age

    @staticmethod
    def is_valid_age(age):
        return isinstance(age, int) and 0 <= age <= 120

    def __repr__(self):
        return f"Person({self.__age})"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if not Person.is_valid_age(new_age):
            raise ValueError("age invalid")

        self.__age = new_age


if __name__ == '__main__':
    p1 = Person(100)
    print(p1)

    # p1.set_age(400)
    #p1.set_age(p1.get_age() + 1)
    p1.age += 1
    #p1.age = p1.age +  1

    p1._Person__age = 2000
    print(p1)
    print(dir(p1))




