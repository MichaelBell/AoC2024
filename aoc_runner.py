from time import ticks_us

def run(module):
    start_time = ticks_us()
    ans = module.puzz1()
    stop_time = ticks_us()
    print(f"Puzzle 1 = {ans}, took: {stop_time-start_time}us")

    start_time = ticks_us()
    ans = module.puzz2()
    stop_time = ticks_us()
    print(f"Puzzle 2 = {ans}, took: {stop_time-start_time}us")

import aoc2
run(aoc2)
