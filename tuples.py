my_tuple = (1, 2, 3)
my_second_tuple = 1, 2, 3   # commas make tuple
tuple_with_a_list = (1, "apple", [3, 4, 5])
tuple_with_a_list[2][1] = 7     # changes list to [3, 7, 5], but elements in the tuple can't be changed


a = 5
b = 20
a, b = b, a     # assigns 20 to a and 5 to b

# UNPACKING

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

def add2(base, *args):
    total = base
    for num in args:
        total += num
    return total
add(5, 20)      # returns 25


course_minutes = {"Python Basics": 232, "Django Basics": 237, "Flask Basics": 189, "Java Basics": 133}

for course, minutes in course_minutes.items():
    print("{} is {} minutes long".format(course, minutes))


list(enumerate("abc"))      # returns [(0, 'a'), (1, 'b'), (2, 'c')] walks through iterable and assign index to each                                element


for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
    print("{}: {}".format(index+1, letter))