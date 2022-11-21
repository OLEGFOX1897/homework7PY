from my_functions import inp_num
from mod_calculator import calculator
from logger import user_logger

def input_expression ():
    while True:
        print('Введите вариант числа \n 1 - Рациональные \n 0 - Комплексные')
        option=inp_num(1)
        if option==0 or option==1:
            if option==1:
                user_logger('Выбраны рациональные числа')
            elif option==0:
                user_logger('Выбраны рациональные числа')
            break

        else:
            user_logger('Неверный выбор варианта числа')

    while True:
        expression=input('Введите выражение, которое необходимо вычислить: ')
        user_logger(f'Введенно выражение: {expression}')
        if option==0 and 'j' in expression:
            break
        elif option==1 and 'j' not in expression:
            break
        else: 
            print('Повторите ввод выражения!')
            user_logger('Введенное выражение не соответствует выбранному варианту')
    return option, expression


    
    
