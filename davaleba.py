from operator import ifloordiv

geo = " ააბბგგდდეევვზთიიკკლლმმნნოოპპჟრსტუუფფქქღყყშჩცძწჭხხჯჰჰ?.,!;sad)1234567890-=+_'\"`~”\n"
eng = " aAbBgGdDeEvVzTiIkKlLmMnNoOpPJrstuUfFqQRyYSCcZwWxXjhH?.,!;sad)1234567890-=+_'\"`~”\n"
text ="ბთუ მზიური"
text2 =""
# for i in text:
#     text2 += (geo[eng.index(i)])
# print(text2)

for i in text:
    if i in eng:
        text2 += (geo[eng.index(i)])
    elif i in geo:
        text2 += (eng[geo.index(i)])
print(text2)

def sum_two_number(a,b):
    return a + b
sum_1 = sum_two_number(89,90)
print(sum_1)

def is_odd(number: int) ->bool:
    # if number % 2 == 1:
    #     return True
    # return False
    return True if number % 2 == 1 else False
print(is_odd(5))













