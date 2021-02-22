set([1, 3, 5])
{1, 3, 5}       # order of elements does not matter in sets

low_primes = {1, 3, 5, 7, 11, 13}
low_primes.add(17)
low_primes.update({19, 23}, {2, 29})    # {1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
low_primes.add(15)
low_primes.remove(15)

set1 = set(range(10))
set2 = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23}
set1.union(set2)             # returns {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 17, 19, 23}                                                           # the same: set1 | set2
set1.difference(set2)       # returns {0, 4, 6, 8, 9}                                                                                               # the same: set1 - set2
set2.difference(set1)      # returns {11, 13, 17, 19, 23}
set2.symmetric_difference(set1)     # returns {0, 4, 6, 8, 9, 11, 13, 17, 19, 23}                                                                           # the same: set1 ^ set2
set1.intersection(set2)     # returns {1, 2, 3, 5, 7}
                                # the same: set1 & set2

# Write a function named covers that accepts a single parameter, a set of topics. Have the function return a list of courses from COURSES where the supplied set and the course's value (also a set) overlap.
# For example, covers({"Python"}) would return ["Python Basics"]

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(set): 
  list = []
  for course in COURSES.keys():
    if set.intersection(COURSES[course]):
      list.append(course)
  return list

#  Function named covers_all takes a single set as an argument. Return the names of all of the courses, in a list, where all of the topics in the supplied set are covered.
# For example, covers_all({"conditions", "input"}) would return ["Python Basics", "Ruby Basics"]. Java Basics and PHP Basics would be excluded because they don't include both of those topics.

def covers_all(set):
  list = []
  for course in COURSES.keys():
    if set.intersection(COURSES[course]) == set:
      list.append(course)
  return list


