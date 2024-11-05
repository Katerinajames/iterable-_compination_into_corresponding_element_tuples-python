
names=['Bob', 'Sue', 'Amanda']
grade_point_averages = [3.5, 4.0, 3.75]

for name,gpa in zip (names,grade_point_averages):
	 print("The student's name is %s  and the corresponding point average is %.2f"%(name ,gpa))
