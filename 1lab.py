from cmath import *
w = 0.1
def roots(x):
    out = set()
    out.update({x ** (1 / 3),
                (x ** (1 / 3)) * (-1 / 2 + (sqrt(3) * 1j) / 2),
                (x ** (1 / 3)) * (-1 / 2 - (sqrt(3) * 1j) / 2)})
    return out
def pol(a, b, c, d):
    if a != 0:
        out = []
        p = (3 * a * c - b ** 2) / (3 * a ** 2)
        q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
        x1 = roots(-q / 2 + sqrt((q / 2) ** 2 + (p / 3) ** 3))
        x2 = roots(-q / 2 - sqrt((q / 2) ** 2 + (p / 3) ** 3))
        for r1 in x1:
            for r2 in x2:
                if abs((r1 * r2) + p / 3) <= 0.00000000001:
                    x = r1 + r2 - b / (3 * a)
                    print(x, abs((r1 * r2) + p / 3), 'good')
                else:
                    if abs((r1 * r2) + p / 3) <= w:
                        x = r1 + r2 - b / (3 * a)
                        print(x, abs((r1 * r2) + p / 3), 'notgood')

    else:
        print('square')
        print((-c + (c**2 - 4 * b * d)**0.5)/2*b, "\n", (-c - (c**2 - 4 * b * d)**0.5)/2*b)
    return out
inp = input().split()
if len(inp) > 4:
    print(o)
try:
    a, b, c, d = complex(inp[0]), complex(inp[1]), complex(inp[2]), complex(inp[3])
    otv = pol(a, b, c, d)
except:
    print("incorrect input")


