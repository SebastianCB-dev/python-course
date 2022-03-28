
def sum_total(*args) -> int:
    tot = 1
    for num in args:
        tot *= num
    return tot

print(f'El resultado es: {sum_total(1,2,3,4,5,6,7,8,9,10)}')
