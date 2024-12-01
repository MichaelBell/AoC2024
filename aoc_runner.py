from time import ticks_us

def run(module):
    start_time = ticks_us()
    module.puzz1()
    stop_time = ticks_us()
    print(f"Puzzle 1 took: {stop_time-start_time}us")

    start_time = ticks_us()
    module.puzz2()
    stop_time = ticks_us()
    print(f"Puzzle 2 took: {stop_time-start_time}us")

import aoc1
run(aoc1)
