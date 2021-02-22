person = {"first_name": "Kasia", "job": "teacher"}
person["last_name"] = "Latkowska"
person.update({"job": "biology teacher", "age": 25})
del person["age"]

# PACKING

def packer(name=None, **kwargs):       # ** packs all arguments into a dictionary, except the name argument
    print(kwargs)

# UNPACKING

def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else: 
        print("Hi no name!")

unpacker(**{"last_name": "Latkowska", "first_name": "Kasia"})

# my_dict = {'name': 'Kenneth', 'job': 'teacher'}
# >>> "Hi, my name is {name}! I am a {job}".format(**my_dict)
# "Hi, my name is Kenneth! I am a teacher"

# CHALLENGE TASK 1

# I need you to make a function named word_count. It should accept a single argument which will be a string. The function needs to return a dictionary. The keys in the dictionary will be each of the words in the string, lowercased. The values will be how many times that particular word appears in the string.

# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}

def word_count(string):
  lower_string = string.lower()
  list = lower_string.split()
  dict = {}
  for item in list:
    if item not in dict.keys():
      dict[item] = 1
    else:
      dict[item] +=1

  return(dict)