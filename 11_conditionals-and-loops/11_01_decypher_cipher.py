# Decipher the message within the `secret` variable.
# Pick out only the alphabetic characters, not the numbers.

secret = "2827338h6636263e8383746l0909l037389o0294464"
a = ""

for n in secret:
    if n.isalpha():
        a += n
print("The secret message within secret is: ", a)