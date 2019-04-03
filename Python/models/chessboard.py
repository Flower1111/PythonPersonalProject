class ChessBoard:
    def __init__(self, height, width):
        self.chessboard = []
        self.height = height
        self.width = width

    def print_chessboard(self):
        for i in range(self.height):
            self.chessboard.append([])
            for j in range(self.width):
                if (i + j) % 2 == 0:
                    self.chessboard[i].append('■')
                else:
                    self.chessboard[i].append('□')
        for row in self.chessboard:
            print(''.join(row))


def check_valid_number(entered_value):
    try:
        number = int(entered_value)
        if number > 0:
            return number
        else:
            raise ValueError
    except ValueError:
        print('Incorrect value. Values must be only integer numbers. Values must be greater than 0')
        return 0
