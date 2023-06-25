male = int(input("Enter the number of male students registered in the class: "))
female = int(input("Enter the number of female students registered in the class: "))

total_students = male + female
male_percentage = male / total_students * 100
female_percentage = female / total_students * 100

print("The total number of students: ")
print("The number of males: ", male)
print("The number of females: ", female)
print("The percentage of male Students:", (male_percentage),"%") 
print("The percentage of female Students:", (female_percentage),"%")  
