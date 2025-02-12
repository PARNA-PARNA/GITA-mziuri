# def print_multi_table(n):
#     for num in range(1,11):
#      print(f" {n} * {num} = {n * num}")
#
# print_multi_table(6)
#
#
# def non_parameter_fun():
#     return "this function doesnot have parameters"
#
# print( non_parameter_fun())
# add_num =lambda a, b: a + b
# print(add_num(1,2))
# n = lambda x : "positive" if x > 0 else "negative"
# print(n(-99))
#
#
# def gpn(*args):
    # pn = []
    # for num in args:
    #     if num > 0:
    #         pn.append(num)
    # return pn
from os.path import split


#     return [num for num in args if num > 0 ]
#
# pos_num = gpn(1,23,34,-4,-65,55,-7,-76,-56)
# print(pos_num)

# კითხულობს ფაილს და
# აბრუნებს საშუალო ასაკს ახალ ფაილში

def read_file(file_name: str) -> list:
    with open(file_name,"r", encoding="utf-8") as file:
        ages_list = []
        lines = file.readlines()
        for line in lines:
           name, age = line.strip().split(", ")
           ages_list.append(int(age))
    return ages_list

def calc_average(data: list) -> float:
    return sum(data) / len(data)

def write_average(filename: str, average: float):
    with open(filename,"w", encoding="utf-8") as file:
        file.write(f'average age : { average}')



ages_data = read_file("age.txt")
average_age = calc_average((ages_data))
write_average("average_age.txt",average_age)







