from typing import Optional
import time

from ktimeout import timeout

def func_with_arguments(sleep_time: float, extra_print: Optional[str] = None):
    while True:
        time.sleep(sleep_time)

        print('Sleeping', sleep_time, 'sec', extra_print or '')

def func():
    func_with_arguments(0.5, extra_print='called from func()')

try:
    timeout.run(func, 2)
except Exception as e:
    print(e)

try:
    timeout.run(
        timeout.partial(func_with_arguments, 0.25, extra_print='extra'),
        2
    )
except Exception as e:
    print(e)