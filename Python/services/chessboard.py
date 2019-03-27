from Python import do_continue
from PythonPersonalProject.Python.models.chessboard import ChessBoard, validation


if __name__ == '__main__':
    is_continue = True
    while is_continue:
        print('Enter height and width of chessboard. Values must be only integer numbers.')
        try:
            entered_value = input('Height: ')
            height = validation(entered_value)
            entered_value = input('Width: ')
            width = validation(entered_value)
        except ValueError:
            print('Incorrect input.')
            continue
        chessboard = ChessBoard(height, width)
        chessboard.print_chessboard()
        response = str(input('Do you want to continue? [y / yes]\n'))
        is_continue = do_continue(response)
    print('The program is completed.')
