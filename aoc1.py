
def puzz1():
    left = []
    right = []

    with open("day1.txt", "r") as f:
        while True:
            line = f.readline()
            if len(line) == 0: break
            
            line = line.split()
            left.append(int(line[0]))
            right.append(int(line[1]))

    left.sort()
    right.sort()

    total = 0
    for i in range(len(left)):
        total += abs(left[i] - right[i])
    #print(total)
    return total

def puzz2():
    left = []
    right = {}

    with open("day1.txt", "r") as f:
        while True:
            line = f.readline()
            if len(line) == 0: break
            
            line = line.split()
            l, r = int(line[0]), int(line[1])
            left.append(l)
            if r in right:
                right[r] += 1
            else:
                right[r] = 1

    left.sort()

    total = 0
    for i in range(len(left)):
        if left[i] in right:
            total += left[i] * right[left[i]]
    #print(total)
    return total
