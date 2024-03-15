

def third_task():
    try:
        print('Input numbers. To stop, type a non-numeric value.')
        number_list = []
        summ = 0
        while True:
            a = input('Input a number: ')
            if not a:
                break
            try:
                number = int(a)
            except ValueError:
                break
            if number < 0:
                raise ValueError('Negative number detected.')
            summ += number
            number_list.append(number)
        print(f'Sum of {number_list}: {summ}')
        return summ
    except ValueError as e:
        print('Error:', e)

third_task()

