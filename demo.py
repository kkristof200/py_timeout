from typing import Optional
import time

from ktimeout import timeout

# TEST WITH CLASS
class T:
    def func(self):
        return timeout.run(
            timeout.partial(self.__func, 1, kw=3),
            2
        )

    def __func(self, i: int, kw: int = 0):
        print(kw)

        return i

try:
    print('res', T().func())
except Exception as e:
    print(e)


# TESTS WITH GLOBAL FUNCS
def func_with_arguments(sleep_time: float, extra_print: Optional[str] = None):
    while True:
        time.sleep(sleep_time)

        print('Sleeping', sleep_time, 'sec', extra_print or '')

def func():
    func_with_arguments(0.5, extra_print='called from func()')

def func_with_return():
    time.sleep(1)

    return 'return_val'

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

try:
    print(timeout.run(func_with_return, 2))
except Exception as e:
    print(e)