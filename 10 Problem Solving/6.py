mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))

average = (mark1 + mark2 + mark3) / 3

print("Average:", average)

if average >= 40:
    print("Pass")
else:
    print("Fail")