
def sum_total(*args) -> int:
    tot = 0
    for num in args:
        tot += num
    return tot


result = sum_total(1,2,3,4,5,6,7,8,9,10)
print(f'El resultado es: {result}')
