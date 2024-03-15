
def second_task(name,age):
    try:
        if age < 0 or age > 130:
            raise ValueError('wrong age')
        if not isinstance(name,str):
            raise ValueError('wrong name format')
    except ValueError as e:
        print('Error:',e)
    return f'{name} your age is {age}'

second_task('alex',131)
second_task(11,130)
second_task(11,23)
b1 = second_task('alex',48)
print(b1)
