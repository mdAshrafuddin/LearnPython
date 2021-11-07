# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

my_list = ['First', 'Second', 'Third']

print(my_list)

for x in my_list:
    print(x)

s = "Rune"

for c in s:
    print(s) 
    print("Inside Loop")
print("Outside Loop")

for r in range(1, 10):
    print(r)

for i in range(len(my_list)):
    print(i, my_list[i])

# value = 10

# while value > 0:
#     value = int(input("Value ?"))
# print(value)


s = "abc"
c = 'd'

if c in s:
    print("c is in s")

if c not in s:
    print("c is not in s")

a = 13
b = 12
c = 10

if a < b or b < c:
    print("awesome")