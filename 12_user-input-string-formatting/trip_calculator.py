# Request inputs from the User

km = input("Please input the kilometers to drive: ")
litres_per_km = input("Please input litres per km of your car: ")
price = input("Please input the price per litre: ")

# Convert into a number

km_num = ""

for k in km:
    if k.isdigit() == True:
        km_num += k
km_num = int(km_num)

litres_num = ""

for l in litres_per_km:
    if l.isdigit() == True:
        litres_num += l
litres_num = int(litres_num)

price_num = ""

for p in price:
    if p.isdigit() == True:
        price_num += p
price_num = int(price_num)

# Calculate the cost of the trip

cost = km_num * litres_num * price_num

print(f"The price to drive {km_num} km \
in a car with {litres_num} litres per km \
at £{price_num} per litre is: £", cost)