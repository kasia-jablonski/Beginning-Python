# Create a function named combiner that takes a single argument, which will be a list made up of strings and numbers.

# Return a single string that is a combination of all of the strings in the list and then the sum of all of the numbers. For example, with the input ["apple", 5.2, "dog", 8], combiner would return "appledog13.2".

def combiner(list):
  string = ""
  number = 0
  for item in list:
    if isinstance(item, str):
      string += item
    else:
      number += item
  return string + str(number)

print(combiner(["apple", 5.2, "dog", 8]))