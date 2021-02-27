
import sys

a = "890"

# b = a # step 1


# def bar(a):
#     print("Inside bar function:reference counter", sys.getrefcount(a))


# bar(a) # step 2
print("variable reference counter", sys.getrefcount(a))
