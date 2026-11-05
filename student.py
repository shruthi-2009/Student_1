#student.py
def addstu():
	name=input("Enter student name: ")
	clas=int(input("Enter class: "))
	roll=int(input("Enter roll number: "))
	student= [name,clas,roll]
	return student
def displaydet(stu):
	print("Name: ",stu[0])
	print("Class: ",stu[1])
	print("Roll number: ",stu[2])
	return
def searchstu(allstulist,roll):
	for i in allstulist:
		if i[2]==roll:
			print("Student found in index position: ",i)
		else:
			print("No student found")
			
