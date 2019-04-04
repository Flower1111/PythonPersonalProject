from Python.do_continue import do_continue
from PythonPersonalProject.Python.models.envelope_analysis_f import Envelope, comparison_of_envelopes, check_valid_side


if __name__ == '__main__':
    is_continue = True
    while is_continue:
        print('Please enter the sizes of the envelopes. Values must be greater than 0.')
        try:
            side = float(input('Enter height of the first envelope: '))
            side_a = check_valid_side(side)
            side = float(input('Enter width of the first envelope: '))
            side_b = check_valid_side(side)
            side = float(input('Enter height of the second envelope: '))
            side_c = check_valid_side(side)
            side = float(input('Enter width of the second envelope: '))
            side_d = check_valid_side(side)
        except ValueError:
            print('Invalid value. Values must be greater than 0.\n')
            continue
        first_envelope = Envelope(side_a, side_b)
        second_envelope = Envelope(side_c, side_d)
        entry_result = comparison_of_envelopes(first_envelope, second_envelope)
        print(entry_result)
        response = str(input('Do you want to continue? [y / yes]\n'))
        is_continue = do_continue(response)
    print('The program is completed.')
