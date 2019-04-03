from Python import do_continue
from PythonPersonalProject.Python.models.converting_number_to_word import number_to_word


if __name__ == '__main__':
    is_continue = True
    while is_continue:
        try:
            entered_number = input('Enter a number: ')
            print(entered_number, '==>', number_to_word(entered_number))
        except ValueError:
            print('Invalid enter.\n')
        response = str(input('Do you want to continue? [y / yes]\n'))
        is_continue = do_continue(response)
    print('The program is completed.')
