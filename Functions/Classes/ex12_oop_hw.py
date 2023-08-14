import random


class Wheel:
    def __init__(self, radius, is_punctured=False, air=None):
        if air is None:
            air = random.randint(85, 95)

        self.air = air
        self.clamp_air()

        self.is_punctured = is_punctured
        self.radius = radius

    def inflate(self, air_to_add):
        self.air += air_to_add
        self.clamp_air()

    def clamp_air(self):
        # if self.air < 0:
        #     self.air = 0
        #
        # if self.air > 100:
        #     self.air = 100

        self.air = max(min(self.air, 100), 0)

    def __repr__(self):
        return f"Wheel(raidus = {self.radius}, " \
               f"air = {self.air}, " \
               f"is_punctured = {self.is_punctured})"



class Vehicle:
    AIR_LIMIT = 60

    def __init__(self, wheels: list[Wheel] = None):
        if wheels is None:
            wheels = []

        self.wheels = wheels

    def check_is_driveable(self):
        if len(self.wheels) <= 0:
            return False

        for wheel in self.wheels[1:]:
            if self.wheels[0].radius != wheel.radius:
                return False

        for wheel in self.wheels:
            if wheel.is_punctured:
                return False

        for wheel in self.wheels:
            if wheel.air <= Vehicle.AIR_LIMIT:
                return False

        return True

    def add_wheel(self, w: Wheel):
        self.wheels.append(w)

    def del_wheel(self, index: int):
        del self.wheels[index]

    def drive(self, distance):
        if not self.check_is_driveable():
            print("cannot drive at all")
            return

        distance_driven = 0
        while distance_driven < distance and self.check_is_driveable():
            # drive 1 unit of distance
            distance_driven += 1

            # reduce air unit by 1 for each wheel
            for w in self.wheels:
                w.air -= 1

        print(f"drove a total of {distance_driven} distance")

    def __repr__(self):
        result = "vehicle wheels:"
        for w in self.wheels:
            result += f" {w}"

        return result


if __name__ == '__main__':
    w1 = Wheel(100)
    w2 = Wheel(100)
    w3 = Wheel(100)
    print(w1)
    print(w2)
    print(w3)

    v1 = Vehicle()
    v1.add_wheel(w1)
    v1.add_wheel(w2)
    v1.add_wheel(w3)
    v1.add_wheel(Wheel(100))
    print()
    print(v1)

    v1.drive(2000)


    v2 = Vehicle()
    v2.drive(100000)
