# questions 1
# Write code to calculate and print:
# 1. Total amount before discount
# 2. Discount amount
# 3. Amount after discount
# 4. Final bill including delivery charge
product_price = 850
quantity = 3
discount_rate = 12
delivery_charge = 80
# calculating the total amount
total_amount = product_price *quantity
print("Total amount is:", total_amount)
# again calculating the discount amount 
discount_amount = total_amount*discount_rate/100
print("The discount amount is:", discount_amount)
# amount after discount 
amount_after_discount = total_amount- discount_amount
print("The amount after discount is :",amount_after_discount)
# calculating the final bill 
final_bill = amount_after_discount+delivery_charge
print("The final bill is :",final_bill)


# question number 2
# Without changing the original string, write Python code to:
# 1. Print the first four characters.
# 2. Print the last seven characters.
# 3. Print the string in reverse order.
# 4. Print the total length of the string.
# 5. Print the final character using negative indexing
course = "DataScience"
print(course[0:4])
print(course[-7:])
print(course[::-1])
print(len(course))
print(course[-1])

# question no 3
# Create a Python program that asks the user to enter their birth year.
# Your program should:
# 1. Take the birth year using input().
# 2. Convert the input into an integer.
# 3. Calculate the person's approximate age in 2026.
# 4. Print the result in a meaningful sentence.
current_year = 2026
birth_year = int(input("Enter your birth year"))
# calculate the persons approximate age in 2026
age = current_year - birth_year
print(f"Your current age is {age} in {current_year}")


# A technology company is selecting students for an internship.
# The eligibility requirements are:
# - The applicant must be at least 18 years old.
# - The applicant must either score at least 70 in Python or have completed a project.
# Your tasks: Write one Boolean expression using comparison and logical operators, save it in is_eligible, and print the result. 
# Then change project_completed to False and check how the result changes.
age = 20
python_score = 65
project_completed = True
is_eligibile = (age>=18 and python_score>= 70) or project_completed
print(is_eligibile)

# Question 6
# You're developing a result-processing system for a college.
# College grading policy
# Marks	      Grade
# 90 or above  	A
# 75–89	        B
# 60–74	        C
# Below 60	    F

# Additional rule: A student must have at least 75% attendance to receive a grade.
#  Otherwise, display "Attendance Requirement Not Met".
# Your tasks:
# 1. Check attendance first.
# 2. If attendance is sufficient, use nested if–elif–else statements to determine the grade.
# 3. Print the student's grade.
# 4. If attendance is insufficient, display the rejection message instead.
# Test afterward: Change marks to 90, then change attendance to 70.
marks = 90
attendance = 70
# checking the attendance
if attendance >=75:
    print("Grade Received")
    if marks>=90:
        print("You have received an A garde")
    elif marks <=89:
        print("You have receieved a B grade")
    elif marks <=75:
        print("You have received a C garde")
    elif marks<60:
        print("You have received an F garde")

else:
    print("Attendance Requirement Not Met")


# Question 7
# You're working for a delivery company.
# package_weight = 7is_express = True
# Delivery charges
# Package weight	                Base charge
# 2 kg or less	                           Rs. 100
# More than 2 kg, up to 5 kg	            Rs. 200
# More than 5 kg, up to 10 kg	            Rs. 350
# Express delivery costs an additional Rs. 150.
# Your tasks:
# 1. If the weight is zero, negative, or above 10 kg, print "Invalid Package Weight" and don't calculate a bill.
# 2. Otherwise, determine the base charge using if, elif, and else.
# 3. Add Rs. 150 if is_express is True.
# 4. Print the base charge, express charge, and final delivery bill.
# Test afterward: Try weights of 2 kg, 5 kg, 10 kg, and 11 kg.

package_weight = 7
is_express = True
#  task 1
if package_weight >0 and  package_weight<=10:
    if package_weight <= 2:
        base_charge = 100
    elif package_weight <= 5:
        base_charge = 200
    else:
        base_charge = 350
#task 3
    if is_express == True:
        express_charge = 150
       
    else:
        express_charge = 0
    #  final bill 
    final_bill = base_charge+express_charge
    print("The final bill:", final_bill)
    print("Express Charge:",express_charge)
    print("Base Charge:", base_charge)
else:
    print("Invalid Package weight")


# Question 7
# You're building an enrollment system for an online programming academy.

# Enrollment rules
# The student must be at least 16 years old, must have completed the basics course, and must have paid the enrollment fee.
# Your tasks:
# 1. Check whether the student meets the age requirement.
# 2. If yes, check whether the basics course is completed.
# 3. If yes, check whether payment is completed.
# 4. If all requirements are met, print "Enrollment Successful".
# 5. Otherwise, display the appropriate message: "Age Requirement Not Met", "Complete Basics First", or "Payment Pending".
# Use nested conditional statements. Each failed requirement should produce only its own message.

age = 19
has_completed_basics = True
payment_completed = False
# Task 1: Check age requirement
if age >= 16:
    # Task 2: Check Python basics completion
    if has_completed_basics:
        # Task 3: Check payment
        if  payment_completed == True:
            print("Enrollemnt successful")
        else:
            print("The Payment is pending")
    else:
        print("Complete Basics First")

else:
    print("Age requirement are not met")

