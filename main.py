from user_interface import input_expression
from mod_calculator import calculator
from logger import user_logger
user_logger('Запуск')
out=calculator(input_expression())
print(f'Результат вычисления равен = {out}')
user_logger(f'Получен ответ: {out}')
user_logger('Конец работы')
