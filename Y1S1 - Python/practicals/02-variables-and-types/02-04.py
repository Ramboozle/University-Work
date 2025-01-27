sweets = int(input("Enter the number of sweets: "))
students = int(input("Enter the number of students: "))
sweetsPerStudent = sweets // students
sweetsLeft = sweets % students
print("Each student will get " + str(sweetsPerStudent), "sweets and there will be " + str(sweetsLeft) + " sweets left over.")