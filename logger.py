from datetime import datetime as dt
from time import time
def user_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a', encoding="utf-8") as file:
        file.write('{}; действие - {}\n'
                    .format(time, data))