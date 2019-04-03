import math


def check_valid_number(entered_number):
    try:
        number = float(entered_number)
        if number > 0:
            return number
        else:
            raise ValueError
    except ValueError:
        print('Incorrect value. It must be greater than 0')
        return 0


def triangle_is_exist(first_side, second_side, third_side):
    if (first_side + second_side) > third_side and (second_side + third_side) > first_side and (first_side + third_side) \
            > second_side:
        return True


def check_valid_triangle(name, first_side, second_side, third_side):
    if first_side and second_side and third_side and name:
        if triangle_is_exist(first_side, second_side, third_side):
            return True


def continue_enter(answer):
    if (answer.lower() == 'y') or (answer.lower() == 'yes'):
        return True
    else:
        return False


class Triangle:
    def __init__(self, name, first_side, second_side, third_side):
        self.name = name
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side
        self.square = self.area(first_side, second_side, third_side)

    def __lt__(self, other):
        return self.square < other.square

    def __str__(self):
        return '[Triangle %s]: %.2f cm' % (self.name, self.square)

    def area(self, first_side, second_side, third_side):
        perimeter = (first_side + second_side + third_side) / 2
        square = math.sqrt(
            perimeter * (perimeter - first_side) * (perimeter - second_side) * (perimeter - third_side))
        return square



