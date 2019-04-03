from Python import do_continue
from PythonPersonalProject.Python.models.lucky_tickets import easy_way_counting, difficult_way_counting


if __name__ == '__main__':
    is_continue = True
    while is_continue:
        try:
            file_dir = input('Input directory: ')  # Write full path where the `tickets.txt` file was saved
            with open(fr'{file_dir}', 'r') as file:
                easy = easy_way_counting(file)
                print(f'Number of lucky tickets in an easy way: {easy}')
            with open(fr'{file_dir}', 'r') as file:
                difficult = difficult_way_counting(file)
                print(f'Number of lucky tickets in a difficult way: {difficult}')
        except FileNotFoundError:
            print('No such file or directory\n')
        response = str(input('Do you want to continue? [y / yes]\n'))
        is_continue = do_continue(response)
    print('The program is completed.')
