import re

def puzz1():
    total = 0
    with open("day3.txt", "r") as f:
        data = f.read()
    #data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    
    m = re.search(r'mul\(([0-9]+),([0-9]+)\)', data)
    
    start = 0
    while m is not None:
        total += int(m.group(1)) * int(m.group(2))
        end = start + m.end()
        m = re.search(r'mul\(([0-9]+),([0-9]+)\)', data[end:])
        start = end
    
    return total

def puzz2():
    total = 0
    with open("day3.txt", "r") as f:
        data = f.read()
    #data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    
    start = 0
    
    while start < len(data):
        next_dont = data.find("don't()", start)
        #print("dont", next_dont)
        if next_dont != -1:
            m = re.search(r'mul\(([0-9]+),([0-9]+)\)', data[start:next_dont])
        else:
            m = re.search(r'mul\(([0-9]+),([0-9]+)\)', data[start:])
        while m is not None:
            total += int(m.group(1)) * int(m.group(2))
            end = start + m.end()
            m = re.search(r'mul\(([0-9]+),([0-9]+)\)', data[end:next_dont])
            start = end
        
        if start == len(data): break
        
        next_do = data.find("do()", start)
        #print("do", next_do)
        if next_do == -1: break
        start = next_do + 4
    
    return total