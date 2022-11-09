import sys

b = 0

def calc_y(x):
    return 4 - (x*x)

def calc_integral(n):
    dx = b / n
    temp = []
    for i in range(n):
        x = i * dx
        temp.append(dx * calc_y(x))
    res = 0
    for t in temp:
        res = res + t
    print(f"n = {n} | dx = {dx} | {res} FE")

if __name__ == "__main__":
    b = int(sys.argv[1])
    for i in range(1, 8 + 1):
        calc_integral(i)
