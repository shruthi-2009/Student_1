import student
def loop_1():
	print("Welcome")
	studentlist=[]
	while True:
		print("Enter -1 to exit")
		print("1. Add a Student")
		print("2. Display Details")
		print("3. Search for a student")
		ch = int(input("Enter choice: "))
		if ch == 1:
			new=student.addstu()
			studentlist.append(new)
		elif ch == 2:
			ind=int(input("Enter the index of the student: "))
			student.displaydet(studentlist[ind])
		elif ch == 3:
			rollno=int(input("Enter the students roll number: "))
			student.searchstu(studentlist,rollno)
		elif ch == -1:
			break
loop_1()
