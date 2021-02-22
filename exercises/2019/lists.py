banner = list("Congratulations")    # return list ["C", "o", "n", "g", "r", "a", "t", "u", "l", "a", "t", ...]

temperatures = []
temperatures.append(98.6)
temperatures.append(99.4)
er_temp = [102.2, 103.5]
temperatures.extend(er_temp)    # extend returns temperatures list [98.6, 99.4, 102.2, 103.5]

# Concatenation doesn't modify lists
primary_care_doctors = ["Dr. Scholls", "Dr. Pepper"]
er_doctors = ["Doug", "Susan"]
all_doctors = primary_care_doctors + er_doctors

#Wishlist
books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

books[-1]   # the last element  books[(len(books)-1)]
books.insert(0, "Learning Python: Powerful Object-Oriented Programming")

# Slices

books[1:4]  # takes from element with index 1 do element with index 3; 3 list items
books[:2]   # starts with index 0; first 2 items
books[2:]   # takes from element with index 2 to the last element
books[-2:]  # the last 2 items
books[-2:-5:-1] # the last 3 items backwards
books[::-1] # entire list backwards

"\N{TACO}"  #changes to unicode'🌮'

#del books[0]   - removes label of element with index .. 
#recommend = books.pop()    - returns the last element and removes it from list
#list.remove("item")    - removes first instance of the item in the list

# Split and Join
quote = "The greatest teacher failure is"
words = quote.split()   # creates a list of words separated by blank space in string

attendees = ["Ken", "Alena", "Ashley", "James"]
to_line = ", ".join(attendees)  # returns "Ken, Alena, Ashley, James"
to_line.split(", ") #splits by separator ", "

# Multidimentional lists

travel_expenses = [
    [5.00, 2.75, 22.00, 0.00, 0.00],
    [24.75, 5.50, 15.00, 22.00, 8.00],
    [2.75, 5.50, 0.00, 29.00, 5.00],
]
print("Travel expenses:")
week_number = 1
for week in travel_expenses:
    print("Week #{}: ${}".format(week_number,sum(week)))
    week_number += 1

