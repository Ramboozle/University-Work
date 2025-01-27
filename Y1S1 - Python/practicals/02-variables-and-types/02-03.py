studentNo = int(input("Enter your student number: "))
groupSize = int(input("Enter the size of your group: "))
groups = studentNo // groupSize
remainder = studentNo % groupSize
print("There will be " + str(groups), "full groups with " + str(remainder) + " students left over.")