# A List is an ordered and mutable python container begin on of the most common data structure
import random
my_list = ['Apple', 'Orange', 'Banana']
print(my_list)
print(my_list[0])
print(my_list[-1])
my_list.pop()
my_list.append("Tanjil")
print(my_list)

print(random.choice(my_list))
print(random.shuffle(my_list))

s = "awesome" 
result = ''.join(random.sample(s, len(s)))


print(result)

my_numbers = [3, 5, 2, 6, 8, 2]

print(max(my_numbers))
print(min(my_numbers))
print(sum(my_numbers) / len(my_numbers))
