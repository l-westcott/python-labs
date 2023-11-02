# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

# Request investment from the User

investment = input("Please enter an investment amount in £: ")

# Only show investment as numbers

inv = ""

for i in investment:
    if i.isdigit() == True:
        inv += i

inv = int(inv)

# Request interest rate in percentage from the User

interest = input("Please enter an interest rate in percentage: ")

# Only show interest as numbers (i.e. remove percentage)

interest_rate = ""

for ir in interest:
    if ir.isdigit() == True:
        interest_rate += ir

interest_rate = int(interest_rate)

# Request number of years to invest from the user

year = input("Please enter the number of years you'd like to invest: ")

# Only show years as numbers (i.e. remove any mention of years etc.)

yr = ""

for y in year:
    if y.isdigit() == True:
        yr += y

yr = int(yr)

# Calculate the return on interest

ret = yr * (interest_rate / 100) * inv

print("The interest you will earn on your investment will be: £", ret)

# Calculate the final value

value = inv + ret

print(f"The final value of your investment after {yr} years will be: £", value)