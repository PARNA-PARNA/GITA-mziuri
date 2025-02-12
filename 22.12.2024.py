# # def read_contacts(file_name: str):
# #     with open(file_name,"r",encoding="utf-8") as file:
# #         print(file.read())
# #
# #
# #
# # def add_contacts(file_name: str,name: str, email: str):
# #     with open(file_name, "a",encoding="utf-8") as file:
# #         file.write(f"{name}: {email}\n")
# #
# #
# # def delete_contact(file_name: str,name: str):
# #     with    open(file_name, "r",encoding="utf-8") as file:
# #         # updated_data = dict()
# #         content =file.read()
# #         lines =content.split("\n")
# #         if name not in contact:
# #             return  f"{name} is not in file content!"
# #         for line in lines:
# #             if line != "":
# #                 old_name, email = line.split(": ")
# #             if name not in line and name == old_name:
# #                 updated_data[old_name] = email
# #             print(updated_data)
# #
# #
# # delete_contact(file_name= "contact.txt",name ="ნინო")
# #
# from wsgiref.util import setup_testing_defaults
#
# # file = open("word.text","r",encoding="utf-8")
# # # full_content =file.read()
# # # print(full_content)
# # # print(file.read())
# # # print(file.readlines())
# # # lines = file.readlines()
# # # for line in lines:
# # #     print(line)
# # content = file.read().split()
# # print(len(content))
# # print(file.read())
#
# # lines = ("prveli xazi\n","meore xazi\n","mesame xazi\n")
# # line ="kodi"
# # file = open("
# # new_test.txt","w+", encoding="utf-8" )
# # # file.write("\n".join(lines))
# # # for line in lines:
# # #     file.write(line)
# # # file.writelines(lines)
# #
# # file.seek(0)
# # print(file.read())
# # file.close()
#
#
# # # append
# # lines = ("pirveli xazi\n","meore xazi\n","mesame xazi")
# # file = open("new_test.txt","a+", encoding="utf-8" )
# # # file.write("\nmeotxe xazi\n")
# # # file.writelines(lines)
# # file.write("\n".join(lines))
# #
# # file.seek(0)
# # print(file.read())
# # file.close
#
# # with statement
# # with open("new_test.txt","r+",encoding="utf-8") as file:
# #     lines = file.readlines()
# #     print(f'{lines[1]},{lines[2]}')
# #
# # students = {
# #     "ლაშა":21,
# #     "მარი":22,
# #     "გიორგი":20,
# #     "თამარი":23}
# #
# # with open("students.txt","w+",encoding="utf-8") as file:
# #     for key,value in students.items():
# #         file.write(f"{key}: {value} \n")
# #     file.seek(0)
# #     print(file.read())
#
#
#
# # with open("source.txt","r",encoding="utf-8") as f:
# #     old_file_content = f.read()
# # with open("destination.txt","w",encoding="utf-8") as f:
# #     f.write(old_file_content)
#
# # def mult_two_numbers(a: float,b:float) -> float:
# #     return a * b
# # print(mult_two_numbers(3,5))
#
# def dev_two_numbers(a: float,b:float) -> float:
#     if b == 0:
#         return "ნულზე გაყოფა არ შეიძლება"
#     else:
#         return a / b
# print(dev_two_numbers(3,3))
#
#
#
# def double_number(n: int) -> int:
#     return n * 2
# doubled = double_number(5)
# # print(doubled)
# for d in range(51):
#     print(doubled)
#
# from operator import ifloordiv

# any_list = [1,1,2,2,3,3,4,5,6]
# print(len(any_list))
# print(set(any_list))
# print(len(set(any_list)))
def uniq_values(list_name):
   if len(list_name) == len(set(list_name)):
       return "unikaluria yvela elementi"
   else:
       return  "elementebi meordeba"
any_list = [1,1,2,2,3,3,4,5,6]
print(uniq_values(any_list))


# print(uniq_values(1,1,1,1,23,2,4)