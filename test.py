from time import sleep

from lib.throttler import Throttler


throttler = Throttler(10, 10)

i = 0

while True:
    i += 1

    if not throttler.allowed():
        sleep(1)
        print('Not allowed to send (try #{0})'.format(i))
        continue

    throttler.action_done()

    print('Allowed to send (try #{0})'.format(i))