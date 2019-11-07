def print_dict(d):
  for key, value in d.items():
    print(f"\t{key}\t{value[0]}\t {value[1]}")
  
courses = {'Chem 103':  ('Sarp Kaya', {'Gamze', 'Ata', 'Ayse', 
                                 'Furkan', 'Mahsa'}),
     'Engr 200':  ('Fikri Karaesmen', {'Ahmet', 'Gonca', 
                                  'Canan', 'Furkan'}),
     'Econ 201':  ('Seda Ertac', {'Ayse', 'Emirhan', 'Gokce', 
                                  'Meva', 'Abdullah'}),
     'Math 205':  ('Nadim Rustom', {'Ilayda', 'Zeynep', 'Ahmet', 'Mahsa'}),
     'Python Section 2':  ('Gul Sena Altintas', {'Canan', 'Gamze', 
                                  'Abdullah', 'Emirhan', 'Ahmet', 
                                  'Gokce', 'Mahsa', 'Furkan', 'Gonca', 
                                  'Meva', 'Ayse', 'Ilayda'})
     }
# Task 1
info_engr = courses['Engr 200']
students = info_engr[1]    # courses['Engr 200'][1]
courses['Engr 200'] = ('Lerzan Ormeci', students)
print_dict(courses)

# Task 2
set_of_all_students = set()
for course in courses:
  students_in_the_course = courses[course][1]
  set_of_all_students = set_of_all_students.union(students_in_the_course)

missing_students = set_of_all_students - courses['Python Section 2'][1]
print(missing_students)
courses['Python Section 2'] = (courses['Python Section 2'][0], set_of_all_students)
print(courses)

# Task 3 
num_chairs = len(courses['Chem 103'][1].union(courses['Econ 201'][1]))
print(num_chairs)

# Task 4
available_slots = []
math_205_students = courses['Math 205'][1]
for course, info in courses.items():
  if math_205_students.isdisjoint(info[1]):
    available_slots.append(course)
print(available_slots)