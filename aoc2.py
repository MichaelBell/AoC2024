def check_report(r, damped):
    mn = 1
    mx = 3
    if r[1] < r[0]:
        mn, mx = -mx, -mn

    for i in range(1, len(r)):
        diff = r[i] - r[i-1]
        if not mn <= diff <= mx:
            if not damped:
                ra = r.copy()
                del ra[i]
                #print("Check", ra)
                if check_report(ra, True):
                    return True
                ra = r.copy()
                del ra[i-1]
                #print("Check", ra)
                return check_report(ra, True)
            else:
                #print("Unsafe", r)
                return False

    #print("Safe", r)
    return True

def puzz1():
    safe = 0
    with open("day2.txt", "r") as f:
        while True:
            line = f.readline()
            if len(line) == 0: break
            
            r = [int(l) for l in line.split()]
            if check_report(r, True):
                safe += 1
            
    return safe

def puzz2():
    safe = 0
    with open("day2.txt", "r") as f:
        while True:
            line = f.readline()
            if len(line) == 0: break
            
            r = [int(l) for l in line.split()]
            
            #print("Test", r)
            if check_report(r, False):
                safe += 1
            elif check_report(r[1:], True):
                safe += 1
            else:
                del r[1]
                if check_report(r, True):
                    safe += 1
    
    return safe
