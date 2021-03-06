#!/usr/bin/env python3

from ev3dev.ev3 import *
import time

mA = LargeMotor('outA')

for i in range(100, -120, -20):
    mA.position = current_time = 0
    s = 'data' + str(i) + '.txt'
    fh = open(s, 'w')
    fh.write('0 ' + '0 ' + '0' + '\n')
    start_time = time.time()
    try:
        while True:
            current_time = time.time() - start_time
            if current_time > 1:
                break
            else:
                mA.run_direct(duty_cycle_sp=i)
                fh.write(str(current_time) + ' ' + str(mA.position) + ' ' + str(mA.speed) + '\n')

    finally:
        mA.stop(stop_action='brake')
        fh.close()
        time.sleep(1)
