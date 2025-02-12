# def div_nums(a,b) -> float:
#     if not isinstance(a,int) or not isinstance(b,int):
#         raise ValueError("integerebi unda iyos")
#     if b == 0:
#         raise ZeroDivisionError("zeroa ra")
#
# print(div_nums(3,7))



def average(numbers: list) -> float:
    if len(numbers) < 1:
        raise ValueError("carieli lista")

    for num in numbers:
        if not isinstance(num, int) and not isinstance(num,float):
            raise ValueError("list elements must be int/float")

    return sum(numbers) / len(numbers)
print(average([1,2,3,4,"k"]))