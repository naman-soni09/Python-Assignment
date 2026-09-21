# num=int(input("Enter Your Number-   "))
# if num > 0:
#     print("positive")
# elif num == 0:
#     print("zero")    
# else:
#     print("negative")


# num=int(input("Enter Your Number-   "))
# if num == 0:
#     print("Zero")
# elif num > 0 and num % 2 == 0:
#     print("Positive Even")  
# elif num > 0 and num % 2 != 0:
#     print("Positive Odd")
# elif num < 0 and num % 2 == 0:
#     print("Negative Even")    
# else:
#     print("Negative Odd")    


# num1=int(input("Enter First Number-  "))
# num2=int(input("Enter Second Number-  "))
# if num1 > num2:
#     print(num1)
# elif num2 > num1:
#     print(num2)    
# else:
#     print("Both are equal")


# num1=int(input("Enter First Number-  "))
# num2=int(input("Enter Second Number-  "))
# num3=int(input("Enter Third Number-   "))
# if num1 <= num2 and num1 <= num3:
#     print(num1)
# elif num2 <= num1 and num2 <= num3:
#     print(num2)
# else:
#     print(num3) 


# num1=int(input("Enter First Number-  "))
# num2=int(input("Enter Second Number-  "))
# num3=int(input("Enter Third Number-   "))
# if num1 >= num2 and num1 >= num3:
#     print(str(num1) + " is the largest")
# elif num2 >= num1 and num2 >= num3:
#     print(str(num2) + " is the largest")
# else:
#     print(str(num3) + " is the largest") 
          

# num = int(input("Enter a number:  "))
# if num % 5 == 0 and num % 11 == 0:
#     print("Divisible by both 5 & 11")
# elif num % 5 == 0:
#     print("Divisible Only By 5")
# elif num % 11 ==0:
#     print("Divisible only by 11")
# else:
#     print("Divisible by Neither")


# num = int(input("Enter a number: "))
# if num % 3 == 0 and num % 7 == 0:
#     print("Divisible by both 3 and 7")
# elif num % 3 == 0:
#     print("Divisible only by 3")
# elif num % 7 == 0:
#     print("Divisible only by 7")
# else:
#     print("Divisible by neither")


# marks = int(input("Enter Marks:  "))
# if marks < 0 or marks > 100:
#     print("Invalid marks")
# elif marks >= 40:
#     print("Pass")
# else:
#     print("Fail")

    
# marks = float(input("Enter marks:  "))
# if marks < 0 or marks > 100:
#     print("Invalid marks")
# elif marks >= 90:
#     print("A")            
# elif marks >= 80:
#     print("B")
# elif marks >= 70:
#     print("C")
# elif marks >= 60:
#     print("D")
# elif marks >= 40:
#     print("E")
# else:
#     print("Fail")


# year = int(input("Enter a year: "))

# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print("Leap year")
# else:
#     print("Not a leap year")


# age = int(input("Enter age: "))
# if age < 0 or age > 120:
#     print("Invalid age")
# elif age >= 18:
#     print("Can vote")
# else:
#     print("Cannot vote")






# ==========================================
# 12. Character Type
# ==========================================
char = input("Enter a character: ")

if char >= 'A' and char <= 'Z':
    print("Uppercase alphabet")
elif char >= 'a' and char <= 'z':
    print("Lowercase alphabet")
elif char >= '0' and char <= '9':
    print("Digit")
else:
    print("Special character")


# ==========================================
# 13. Vowel or Consonant
# ==========================================
char = input("Enter a character: ")

if (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z'):
    if char in 'aeiouAEIOU':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")


# ==========================================
# 14. Profit or Loss
# ==========================================
cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

if sp > cp:
    print("Profit =", sp - cp)
elif cp > sp:
    print("Loss =", cp - sp)
else:
    print("No profit and no loss")


# ==========================================
# 15. Profit/Loss Percentage
# ==========================================
cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

if cp <= 0:
    print("Invalid cost price")
elif sp > cp:
    profit = sp - cp
    percentage = (profit / cp) * 100
    print("Profit Percentage: " + str(percentage) + "%")
elif cp > sp:
    loss = cp - sp
    percentage = (loss / cp) * 100
    print("Loss Percentage: " + str(percentage) + "%")
else:
    print("No profit, no loss (0%)")


units = float(input("Enter units consumed: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

if units >= 0:
    print("Total Electricity Bill: ₹" + str(bill))



num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(num1 / num2)
else:
    print("Invalid operator")


temp = float(input("Enter temperature in Celsius: "))

if temp < 0:
    print("Freezing")
elif temp <= 15:
    print("Very Cold")
elif temp <= 25:
    print("Cold")
elif temp <= 35:
    print("Normal")
else:
    print("Hot")


num = float(input("Enter a number: "))

if num < 0:
    print("Negative")
elif num <= 10:
    print("Number is between 0 and 10")
elif num <= 50:
    print("Number is between 11 and 50")
elif num <= 100:
    print("Number is between 51 and 100")
else:
    print("Above 100")


a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Valid triangle")
else:
    print("Invalid triangle")



a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b and b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Invalid triangle")



balance = float(input("Enter account balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

if withdrawal <= 0:
    print("Withdrawal amount must be greater than 0.")
elif withdrawal % 100 != 0:
    print("Withdrawal amount must be divisible by 100.")
elif withdrawal > balance:
    print("Withdrawal amount cannot be greater than the balance.")
elif (balance - withdrawal) < 500:
    print("After withdrawal, at least ₹500 must remain.")
else:
    balance = balance - withdrawal
    print("Withdrawal successful")
    print("Remaining balance:", balance)


username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "python123":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")



amount = float(input("Enter purchase amount: ₹"))

if amount < 500:
    discount_pct = 0
elif amount <= 999:
    discount_pct = 5
elif amount <= 1999:
    discount_pct = 10
elif amount <= 4999:
    discount_pct = 15
else:
    discount_pct = 20

discount_amount = amount * (discount_pct / 100)
final_amount = amount - discount_amount

print("Original amount: ₹" + str(amount))
print("Discount percentage: " + str(discount_pct) + "%")
print("Discount amount: ₹" + str(discount_amount))
print("Final amount: ₹" + str(final_amount))



m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))

if m1 < 0 or m1 > 100 or m2 < 0 or m2 > 100 or m3 < 0 or m3 > 100:
    print("Invalid marks entered.")
elif m1 < 35 or m2 < 35 or m3 < 35:
    print("Fail")
else:
    avg = (m1 + m2 + m3) / 3
    if avg >= 75:
        print("Distinction")
    elif avg >= 60:
        print("First Class")
    elif avg >= 50:
        print("Second Class")
    else:
        print("Pass")



day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
valid_date = False

if year > 0 and 1 <= month <= 12 and day > 0:
    if month == 2:
        if is_leap and day <= 29:
            valid_date = True
        elif not is_leap and day <= 28:
            valid_date = True
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day <= 30:
            valid_date = True
    else:
        if day <= 31:
            valid_date = True

if valid_date:
    print("Valid")
else:
    print("Invalid")



hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
    print("Valid time")
else:
    print("Invalid time")


name1 = input("Person 1 name: ")
age1 = int(input("Person 1 age: "))
name2 = input("Person 2 name: ")
age2 = int(input("Person 2 age: "))
name3 = input("Person 3 name: ")
age3 = int(input("Person 3 age: "))

if age1 < age2 and age1 < age3:
    print(name1, "is the youngest")
elif age2 < age1 and age2 < age3:
    print(name2, "is the youngest")
elif age3 < age1 and age3 < age2:
    print(name3, "is the youngest")
elif age1 == age2 and age1 == age3:
    print("All three have the same age")
elif age1 == age2 and age1 < age3:
    print(name1, "and", name2, "are the youngest")
elif age1 == age3 and age1 < age2:
    print(name1, "and", name3, "are the youngest")
elif age2 == age3 and age2 < age1:
    print(name2, "and", name3, "are the youngest")



n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))
n3 = float(input("Enter number 3: "))

if (n1 > n2 and n1 < n3) or (n1 < n2 and n1 > n3):
    print("Second largest is", n1)
elif (n2 > n1 and n2 < n3) or (n2 < n1 and n2 > n3):
    print("Second largest is", n2)
else:
    print("Second largest is", n3)



age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
income = float(input("Enter family income: "))
attendance = float(input("Enter attendance percentage: "))

approved = True

if age < 18 or age > 25:
    approved = False

if marks < 85:
    approved = False

if attendance < 75:
    approved = False

if income > 300000:
    approved = False

if approved:
    print("Scholarship Approved")
else:
    print("Scholarship Rejected")
    if age < 18 or age > 25:
        print("Reason: Age is not between 18 and 25")
    if marks < 85:
        print("Reason: Marks below 85")
    if attendance < 75:
        print("Reason: Attendance below 75%")
    if income > 300000:
        print("Reason: Family income above ₹300000")