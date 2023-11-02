# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."

# Butter (57)
b_start = s.find("butter")
b_end = s.find("butter") + len("butter")
b = s[b_start:b_end]
print(b)

# egg
e_start = s.find("egg")
e_end = s.find("egg") + len("egg")
e =s[e_start:e_end]
print(e)

# flour
f_start = s.find("flour")
f_end = s.find("flour") + len("flour")
f = s[f_start:f_end]
print(f)

# grape
g_start = s.find("grap")
g_end = s.find("grap") + len("grap")
and_e = s[2]
g = s[g_start:g_end] + and_e
print(g)