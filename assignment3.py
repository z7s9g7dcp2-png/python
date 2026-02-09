#Premium Rates
#Using If Else...Else if Statements Determine the Monthly Contribution Someone will Pay.

gross_income = float(input("Please enter your gross income"))

contribution = 0
if gross_income < 5999:
    contribution = 150
elif gross_income < 7999:
    contribution = 300
elif gross_income < 11999:
    contribution = 400
elif gross_income < 14999:
    contribution = 500
elif gross_income < 19999:
    contribution = 600
elif gross_income < 24999:
    contribution = 750
elif gross_income < 29999:
    contribution = 850
elif gross_income < 49999:
    contribution = 1000
elif gross_income < 99999:
    contribution = 1500
else:
    contribution = 2000

print(f"Gross Income: Ksh {gross_income}") 
print(f"Monthly Contribution: Ksh {contribution}")
