
def first_task():
    try:
        name = str(input('input your name'))
        age = int(input('input your age'))
        if age < 0 or age > 130:
            raise ValueError('wrong age')
        print(f"Привіт, {name}! Твій вік — {age}")
    except ValueError as e:
        print('Error',e)


