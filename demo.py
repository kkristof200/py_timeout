from typing import Optional
import time

from ktimeout import timeout



# TESTS WITH GLOBAL FUNCS
def func_with_arguments(sleep_time: float, extra_print: Optional[str] = None):
    while True:
        time.sleep(sleep_time)

        print('Sleeping', sleep_time, 'sec', extra_print or '')

def func():
    func_with_arguments(0.25, extra_print='called from func()')

def func_with_return():
    time.sleep(0.25)

    return 'return_val'

try:
    timeout.run(func, 1)
except Exception as e:
    print(e)

try:
    timeout.run(
        timeout.partial(func_with_arguments, 0.25, extra_print='extra'),
        1
    )
except Exception as e:
    print(e)

try:
    print(timeout.run(func_with_return, 1))
except Exception as e:
    print(e)

time.sleep(5)