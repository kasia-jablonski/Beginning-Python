# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.

#The num_teachers function should return an integer for how many teachers are in the dict
def num_teachers(dict):
  return(len(dict))

#The function num_courses should return the total number of courses for all of the teachers.
def num_courses(dict):
  courses = 0
  for key in dict.keys():
    courses += len(dict[key])
  return(courses)

# function named courses should return a single list of all of the available courses in the dictionary. 
def courses(dict):
  course_list = []
  for key in dict.keys():
    for course in dict[key]:
      course_list.append(course)
  return(course_list)

# function most_courses should return the name of the teacher with the most courses
def most_courses(dict):
  max_count = 0
  teacher = ""
  for key in dict.keys():
    counter = len(dict[key])
    if counter > max_count:
      max_count = counter
      teacher = key
  return(teacher)

#function stats should return a list of lists where the first item in each inner list is the teacher's name and the second item is the number of courses that teacher has. For example, it might return: [["Kenneth Love", 5], ["Craig Dennis", 10]]
def stats(dict):
  list_of_lists = []
  for key in dict.keys():
    list = []
    list.append(key)
    list.append(len(dict[key]))
    list_of_lists.append(list)
  return list_of_lists


teachers = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections'], 'name': ['course1', 'course2', 'course3']}
print(num_teachers(teachers))
print(num_courses(teachers))
print(courses(teachers))
print(most_courses(teachers))
print(stats(teachers))