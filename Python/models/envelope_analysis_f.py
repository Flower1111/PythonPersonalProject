class Envelope:
    def __init__(self, first_side, second_side):
        self.first_side = first_side
        self.second_side = second_side


def comparison_of_envelopes(first_envelope, second_envelope):
    if (first_envelope.first_side ** 2 + first_envelope.second_side ** 2
            < second_envelope.first_side ** 2 + second_envelope.second_side ** 2):
        return 'You can put the first envelope into the second envelope.\n'
    if (first_envelope.first_side ** 2 + first_envelope.second_side ** 2
            > second_envelope.first_side ** 2 + second_envelope.second_side ** 2):
        return 'You can put the second envelope into the first envelope.\n'
    return 'You cannot put one envelope into another one.\n'


def check_valid_side(side):
    try:
        entered_side = float(side)
        if entered_side > 0:
            return entered_side
        else:
            raise ValueError
    except ValueError:
        print('Invalid value. Please try again.\n')
        return 0
