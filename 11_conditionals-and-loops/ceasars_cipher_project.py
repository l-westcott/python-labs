# make a ceasar's cipher to secure the secret using the below inputs
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
secret = "I Hear the goosEberries are doing well this yeaR, and so are the mangoes."
cipher = 7

# inputs
encryption = ""

for n in secret:
    # filter out the " "'s
    if n == " ":
        encryption += n
    elif n == ".":
        encryption += n
    elif n == ",":
        encryption += n
    else:
            # find the corresponding letter value in letters
            a = lowercase_letters.find(n)
            # find the corresponding number when cipher is used cipher
            b = a - cipher
            # apply the encryption
            encryption += (lowercase_letters[b])

print(encryption)