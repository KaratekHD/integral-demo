#!/usr/bin/python3
b = 1
n = 150000

def calc_y(x):
    return x**2
    #return 3.552 * (0.9876**x)

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
    #calc_integral(n)
    for i in range(1, n + 1):
        calc_integral(i)
