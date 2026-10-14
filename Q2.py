marks_list = [78, 35, 92, 40, 61]

marks_tuple = tuple(marks_list)

print("Marks List:", marks_list)
print("Data type of list:", type(marks_list))

print("Marks Tuple:", marks_tuple)
print("Data type of tuple:", type(marks_tuple))

print("Highest mark:", max(marks_list))
print("Lowest mark:", min(marks_list))

pass_count = marks_list.count(40) + (marks_list[0] >= 40) + (marks_list[1] > 40) + (marks_list[2] > 40) + (marks_list[4] > 40)

print("Number of students scoring at least 40:", pass_count)

valid_marks = (
    marks_list[0] >= 0 and marks_list[0] <= 100 and
    marks_list[1] >= 0 and marks_list[1] <= 100 and
    marks_list[2] >= 0 and marks_list[2] <= 100 and
    marks_list[3] >= 0 and marks_list[3] <= 100 and
    marks_list[4] >= 0 and marks_list[4] <= 100
)

print("Are all marks valid?", valid_marks)

marks_list[0] = 80
print("List after changing an element:", marks_list)
