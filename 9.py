
import objgraph
import ctypes
import sys

a = [5, ]
a.append(a)
print(a)

print(sys.getrefcount(a))


objgraph.show_refs([a,], filename='9.png')


# step 1
# class PyObject(ctypes.Structure):
#     _fields_ = [("refcnt", ctypes.c_long)]


# lst_address = id(a)

# del a

# step 2
# Check the reference count of deleted objects
# print("before deleting ref count of a list...")
# print(PyObject.from_address(lst_address).refcnt)
