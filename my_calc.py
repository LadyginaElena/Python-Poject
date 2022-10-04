def plus (x,y):
    return x+y

def minus (x,y):
    return x-y

def multip (x,y):
    return x*y

def divis (x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("На ноль делить нельзя")