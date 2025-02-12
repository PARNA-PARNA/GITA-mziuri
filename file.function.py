# def read_file(file_name: str) -> str:
#     with open(file_name, "r",encoding="utf-8") as file:
#         content = file.read()
#         return content
odd_nums = []
for num in range(1,11):
    if num % 2 != 0:
        odd_nums.append(num)
print(odd_nums)


txt = " gamarjoba "
new_txt = txt.strip()
print(new_txt)