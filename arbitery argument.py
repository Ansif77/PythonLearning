def sum(*args):
    total =0
    for number in args:
        total += number
    return total
result=sum(1,2,52,25,17,81,9,8,77,22,25,8)
print(result)