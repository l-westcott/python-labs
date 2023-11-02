# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

# Request for an honest opinion

opinion = input("Please enter an honest opinion ")

# Convert the opinion

a = ""

for n in range(len(opinion)):
    if n % 2 == 0:
        a += opinion[n].upper()
    else:
        a += opinion[n].lower()

print(a)
