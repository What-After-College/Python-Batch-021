# import cal

from cal import add, sub, mul, div, sine


while(True):
    inp=input()
    if(inp =="stop"):
        break
    n=int(input())
    m=int(input())

    d={
        "add" : add(n, m),
        "sub" : sub(n, m),
        "mul" : mul(n, m),
        "div" : div(n, m),

    }
    

    print(d[inp])

# s = add(n, m)
# sub = sub(8, 4)
# mul = mul(4, 8)
# div = div(8, 4)

# print(s, sub, mul, div)

# print(sine(90))

