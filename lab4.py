#First task---------------------------------

# text = "Hello, World!"

# # 1. len()
# length = len(text)
# print("Length of the text:", length)

# # 2. lower()
# lower_text = text.lower()
# print("Lowercase text:", lower_text)

# # 3. upper()
# upper_text = text.upper()
# print("Uppercase text:", upper_text)

# # 4. replace()
# replaced_text = text.replace("o", "0")
# print("Replaced text:", replaced_text)

# # 5. split()
# splitted_text = text.split(", ")
# print("Splitted text:", splitted_text)

# # 6. join()
# joined_text = ", ".join(splitted_text)
# print("Joined text:", joined_text)

# # 7. find()
# index = text.find("World")
# print("Index of 'World':", index)

# # 8. count()
# count = text.count("l")
# print("Count of 'l':", count)

# # 9. startswith()
# starts_with = text.startswith("Hello")
# print("Starts with 'Hello':", starts_with)

# # 10. endswith()
# ends_with = text.endswith("!")
# print("Ends with '!':", ends_with)

#Second task---------------------------------

# def get_sorted_students():
#     students = []
#     while True:
#         student = input("Enter student name and class (or just press enter to stop): ").strip()
#         if not student:
#             break
#         name, cls = student.split()
#         students.append((name, int(cls)))
#     return sorted(students, key=lambda x: x[1])

# def print_students(students):
#     for student in students:
#         print(student[0], student[1])

# students = get_sorted_students()
# print("\nSorted list of students:")
# print_students(students)

#Third task---------------------------------
#a

# def change_case(string):
#     upper_count = 0
#     lower_count = 0
#     for char in string:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1
    
#     if upper_count > lower_count:
#         return string.upper()
#     else:
#         return string.lower()

# string = input()
# print(change_case(string))

#b

while True:
  a = input("Enter the first number: ")
  b = input("Enter the second number: ")
  if a.isdigit() and b.isdigit():
    print("The sum of the numbers is:", int(a) + int(b))
    break
  else:
    print("Invalid input. Please try again.")


