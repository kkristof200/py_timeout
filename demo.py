import time

from ktimeout import timeout

def random_func():
    while True:
        time.sleep(1)

        print('Sleeping 1 sec')

timeout.run(random_func, 3)