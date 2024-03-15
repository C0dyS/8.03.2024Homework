

def fourth_task(number_list):
    try:
        summ = 0
        for element in number_list:
            if not isinstance(element, int):
                raise ValueError('not integer value found')
            if element < 0:
                raise ValueError('negative number found')
    except ValueError as e:
        print('error:',e)
    return sum(number_list)

def fourth_task_b(llist):
        summ = 0
        for element in llist:
            if not isinstance(element, int):
                raise ValueError('not integer value found')
            if element < 0:
                raise ValueError('negative number found')
        return sum(llist)

list_1 = [1,2,5,8,5]
list_2 = [1,4 ,-3]
a = fourth_task(list_1)
fourth_task(list_2)
print(a)

try:
    input_list = [1, 2, 3, 4, 5]
    result = fourth_task_b(list_2)
    print('Sum:', result)
except ValueError as e:
    print('Error:', e)