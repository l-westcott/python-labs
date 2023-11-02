# You wake up in a maze of `if` statements and you need
# to find the path to get out:
#
# .--.--.--.  .--.--.
# |     |        |  |
# :  :--:  :  :  :  :
# |  |     |  |     |
# :  :  :  :--:--:--:
# |  |  |           |
# :  :  :--:--:--:  :
# |  |   You  |  |  |
# :  :--:--:  :  :  :
# |     |     |  |  |
# :--:  :  :--:  :  :
# |        |        |
# :--:--:--:--:--:--:
#
# However, this maze has a BIG limitation!
# There are only two actions you can take, you can only ADD
# either one of the following lines of code:
#
#     flag = True
#     flag = False
#
# You can add as many of them as you want to, but you can't change
# any of the code that is already there.
#
# Add the code so when you run it, it will print out all steps
# that you need to take in order to get out of the maze!
# You are always facing North and you can take sideways steps
# without changing the direction that you're looking.

# To get out of the maze I need to go left once, straight ahead twice, right once, straight ahead once, right once and straight ahead once

print("To get out of the maze I need to:")
print("1. Go left once")
print("2. Go straight ahead twice")
print("3. Go right once")
print("4. Go straight ahead once")
print("5. Go right once")
print("6. Go straight ahead once and exit")



flag = True

if flag == True:
    print("left")

flag = False

if flag == False:
    print("straight ahead")

if flag == True:
    print("left")

if flag == False:
    print("straight ahead")

if flag == True:
    print("straight ahead")

if flag == True:
    print("straight ahead")

if flag == True:
    print("DEAD END")

if flag == True:
    print("left")

if flag == False:
    print("right")

flag = True

if flag == True:
    print("straight ahead")

if flag == False:
    print("straight ahead")

if flag == False:
    print("DEAD END")

if flag == True:
    print("right")

if flag == True:
    print("straight ahead")

flag = False

if flag == True:
    print("left")

if flag == False:
    print("EXIT!!")

if flag == True:
    print("DEAD END")
