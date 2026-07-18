students = {}

num_of_students = int(input("How many students are there?: "))
print("")
total = 0
for i in range(num_of_students):
    SN = input("Enter student name: ")
    SS = int(input("Enter student's score: "))
    students[SN] = SS
print("")

highest_score = 0
lowest_score = 100
for key, value in students.items():
    print(key, value)
    total += value

    if value > highest_score:
      highest_score = value
      highest_student = key

    if value <= lowest_score:
      lowest_score = value
      lowest_student = key

t = total
avg = t / num_of_students
print("Average: {:.2f}".format(avg))
print("Highest Student: {}, {}".format(highest_student, highest_score))
print("Lowest Student: {}, {}". format(lowest_student, lowest_score))
