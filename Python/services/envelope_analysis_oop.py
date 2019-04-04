from PythonPersonalProject.Python.models.envelope_analysis_oop import FloatInput, CheckingRules, GreaterThenZero, Envelope, Choice


if __name__ == '__main__':
    print('Please enter the sizes of the envelopes. Values must be greater than 0.')
    is_continue = True
    while is_continue:
        height = FloatInput("height")
        width = FloatInput("width")
        tested_side = CheckingRules(GreaterThenZero())
        first_envelope = Envelope(tested_side.passed(height.input_side()), tested_side.passed(width.input_side()))
        second_envelope = Envelope(tested_side.passed(height.input_side()), tested_side.passed(width.input_side()))
        print(f'You can put the first envelope into the second envelope. ==> {first_envelope < second_envelope}\n'
              f'You can put the second envelope into the first envelope. ==> {first_envelope > second_envelope}')
        is_continue = Choice().do_continue()
    print('The program is completed.')
