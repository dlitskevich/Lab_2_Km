
def objectify(passed_class):
    """"""
    class Array:
        def __init__(self, coord_list):
            self.vector = passed_class(coord_list)
            self.vector.coord = coord_list
            self.vector.dimension = len(coord_list)

        def __getattr__(self, name):
            return getattr(self.vector, name)

        def __str__(self):
            return "array({})".format(self.vector.coord)

        def __add__(self, other):
            if not self.vector.dimension == other.dimension:
                raise ValueError("To sum up dimensions must be equal")

            new_coord = []
            for coord, an_coord in zip(self.vector.coord, other.coord):
                new_coord.append(coord + an_coord)

            return Vector(new_coord)

        def __mul__(self, other):
            if not isinstance(other, (int, float)):
                raise TypeError("Multiplication is defined for numbers only")

            new_coord = []
            for coord in self.vector.coord:
                new_coord.append(coord * other)

            return Vector(new_coord)
        __rmul__ = __mul__

        def __sub__(self, other):
            if not self.vector.dimension == other.dimension:
                raise ValueError("To subtract dimensions must be equal")

            new_coord = []
            for coord, an_coord in zip(self.vector.coord, other.coord):
                new_coord.append(coord - an_coord)

            return Vector(new_coord)
        __rsub__ = __sub__

        def __cmp__(self, other):
            if not self.vector.dimension == other.dimension:
                return True

            for coord, an_coord in zip(self.vector.coord, other.coord):
                if not coord == an_coord:
                    return True
            return False

        def __len__(self):
            return self.vector.dimension

        def __getitem__(self, index):
            return self.vector.coord[index]

        def __mod__(self, other):
            if not self.vector.dimension == other.dimension:
                raise ValueError("To Multiplication dimensions must be equal")

            product = 0
            for coord, an_coord in zip(self.vector.coord, other.coord):
                product += coord * an_coord

            return product
    return Array


class NdArray(object):
    def __get__(self, instance, owner):
        return instance.coord

    def __set__(self, instance, value):
        instance.coord = value


@objectify
class Vector:
    coord = NdArray()
    dimension = 0

    def __init__(self, *args):
        return


if __name__ == "__main__":
    array = Vector([1, 2, 3])
    an_array = Vector([3, 2, 1])
    cmp_array = Vector([1, 2, 3])
    number = -12.3

    print("What we have:\n"
          "{} : {}\n"
          "{} : {}\n".format(array, array.coord, an_array, an_array.coord))

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

    print(array)
