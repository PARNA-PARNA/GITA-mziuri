def sum_two_numbers(a: int,b:int) -> int:
    return a + b
print(sum_two_numbers(3,5))


def calculate_avg(*args):
    return sum(args) / len(args)


def print_data(**kwargs):
    for key,value in kwargs.items():
        print(f" key : {key},value : {value}")


print(calculate_avg(1,2,3,4,5,6))
print_data(name="parna", age=21)



def count_vowels(a):
    vowels_list = ["ა","ე","ი","ო","უ"]
    vowels_sum = 0
    for vowels in a:
        if  vowels in vowels_list:
            vowels_sum += 1
    return vowels_sum

print(count_vowels("ასაეუუუეხგ"))

def read_txt_file(file_name: str) -> str:
    with open(file_name,"r",encoding="utf-8") as file:
        content = file.read()
        return content

print(read_txt_file("age.txt"))


"""
merve davaleba
 """

def  is_palindrome(a):
        return a == a[::-1]
print(is_palindrome("aseesa"))

matrix = [[1, 2], [3, 4]]
print(matrix[0])
matrix = [[1, 2], [3, 4]]

# ელემენტის ნახვა
row = 0  # სტრიქონის ინდექსი
col = 1  # სვეტის ინდექსი
element = matrix[row][col]

print(f"ელემენტი ({row}, {col}): {element}")
