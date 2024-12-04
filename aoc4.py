test_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

search_dir = [
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1) ]

xmas = "XMAS"

def puzz1():
    data = []
    #for line in test_data.split('\n'):
    #    data.append(line)
    with open("day4.txt", "r") as f:
        while True:
            line = f.readline()
            if len(line) == 0: break
            data.append(line)
    
    #print(data)
    
    total = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] != 'X': continue
            for d in search_dir:
                try:
                    p = (x, y)
                    for i in range(1, 4):
                        p = [sum(x) for x in zip(p, d)]
                        if p[1] < 0 or p[0] < 0 or data[p[1]][p[0]] != xmas[i]:
                            break
                    else:
                        #print(x, y, d)
                        total += 1
                except IndexError:
                    pass
    return total

def puzz2():
    data = []
    #for line in test_data.split('\n'):
    #    data.append(line)
    with open("day4.txt", "r") as f:
        while True:
            line = f.readline()
            if len(line) == 0: break
            data.append(line)
    
    #print(data)
    
    total = 0
    for y in range(1,len(data)-1):
        for x in range(1,len(data[0])-1):
            if data[y][x] != 'A': continue
            if (data[y-1][x-1] + data[y+1][x+1] in ('MS', 'SM') and
                data[y-1][x+1] + data[y+1][x-1] in ('MS', 'SM')):
                total += 1
    return total