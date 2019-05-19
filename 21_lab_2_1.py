

class NdArray(object):
    def __get__(self, instance, owner):
        return instance.coord_list

    def __set__(self, instance, value):
        instance.coord_list = value


class Vector:
    coord = NdArray()

    def __init__(self, coord_list):
        self.coord = coord_list
        self.dimension = len(coord_list)
        return

    def __str__(self):
        return "array({})".format(self.coord)

    def __add__(self, other):
        if not self.dimension == other.dimension:
            raise ValueError("To sum up dimensions must be equal")

        new_coord = []
        for coord, an_coord in zip(self.coord, other.coord):
            new_coord.append(coord + an_coord)

        return Vector(new_coord)

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Multiplication is defined for numbers only")

        new_coord = []
        for coord in self.coord:
            new_coord.append(coord * other)

        return Vector(new_coord)

    __rmul__ = __mul__

    def __sub__(self, other):
        if not self.dimension == other.dimension:
            raise ValueError("To subtract dimensions must be equal")

        new_coord = []
        for coord, an_coord in zip(self.coord, other.coord):
            new_coord.append(coord - an_coord)

        return Vector(new_coord)

    __rsub__ = __sub__

    def __eq__(self, other):
        if not self.dimension == other.dimension:
            return False

        for coord, an_coord in zip(self.coord, other.coord):
            if not coord == an_coord:
                return False
        return True

    def __len__(self):
        return self.dimension

    def __getitem__(self, index):
        return self.coord[index]

    def __mod__(self, other):
        if not self.dimension == other.dimension:
            raise ValueError("To Multiplication dimensions must be equal")

        product = 0
        for coord, an_coord in zip(self.coord, other.coord):
            product += coord * an_coord

        return product


if __name__ == "__main__":
    array = Vector([1, 2, 3])
    an_array = Vector([3, 2, 1])
    cmp_array = Vector([1, 2, 3])
    number = -12.3

    print(array.__dict__)
    print(array.coord)
    print(an_array.coord)

    print("What we have:\n"
          "{} : {}\n"
          "{} : {}\n".format(repr(array), array.coord,
                             repr(an_array), an_array.coord))

    print("Addition:\n"
          "{}\n"
          "{}\n".format(array + an_array, an_array + array))

    print("Subtraction:\n"
          "{}\n"
          "{}\n".format(array - an_array, an_array - array))

    print("Multiplication Const:\n"
          "{}\n"
          "{}\n".format(array * number, number * array))

    print("Check equality:\n"
          "{}\n"
          "{}\n".format(array == an_array, array == cmp_array))

    print("Length:\n"
          "{} : {}\n"
          "{} : {}\n".format(array, len(array), an_array, len(an_array)))

    print("Items:\n"
          "{} : {}  -- 3rd\n"
          "{} : {}  -- 3rd\n".format(array, array[2], an_array, an_array[2]))

    print("Multiplication Scalar:\n"
          "{}\n"
          "{}\n".format(array % an_array, array % array))

