from Python import do_continue
from PythonPersonalProject.Python.models.triangles import Triangle, check_valid_number, check_valid_triangle, continue_enter


if __name__ == "__main__":
    triangles = []
    is_continue = True
    while True:
        name = input("Name of the triangle: ")
        first_side = input("First side: ")
        first_side = check_valid_number(first_side)
        second_side = input("Second side: ")
        second_side = check_valid_number(second_side)
        third_side = input("Third side: ")
        third_side = check_valid_number(third_side)
        if check_valid_triangle(name, first_side, second_side, third_side):
            triangle = Triangle(name, first_side, second_side, third_side)
            triangles.append(triangle)
        answer = input('Do you want to add another triangle? [yes] / [no]: ')
        if not continue_enter(answer):
            break
    triangles.sort(reverse=True)
    print('============= Triangles list: ===============')
    for x in triangles:
        print(x)
        response = str(input('Do you want to continue? [y / yes]\n'))
        is_continue = do_continue(response)
    print('The program is completed.')