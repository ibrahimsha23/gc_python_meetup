import sys

a = 5
b = 5

def print_id(var_val, var):
    print("id of {0} - {1}".format(var_val, id(var)))

print_id("a", a)
print_id("b", b)
print("===================== value change ===============")

a = 6 # new value

print_id("a", a)
print_id("b", b)
