student_lists = input("Enter student heights: ").split(",")
for n in range(0, len(student_lists)):
    student_lists[n] = int(student_lists[n])
print(student_lists)
print(round(sum(student_lists)/len(student_lists)))
# j = 0
# k = 0
# for i in student_lists:
#     j += 1
#     k += int(i)
# print(j)
# print(k)
# avg = k/j
# print(avg)
