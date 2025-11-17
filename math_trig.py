import math


x = 0.5
"""result_rad = math.acos(x)
print(result_rad)
"""
def trig_acos(x)->float:
    result_rad = math.acos(x)
    print(result_rad)

    return result_rad


def trig_asin(x)->float:
    result_rad = math.asin(x)
    print(result_rad)

    return result_rad


def trig_atan(x)->float:
    result_rad = math.atan(x)
    print(result_rad)

    return result_rad
# calculos trigonometricos
trig_acos(x)
trig_asin(x)
trig_atan(x)

# constantes
print(math.e)
#print(math.inf)


a = [1, 5, 8, 0]

min = math.inf

for v in a:
    print(v)

    if v < min:
        min = v
        print(min)

    """if v > max:
        max = v
        print(max)"""
    