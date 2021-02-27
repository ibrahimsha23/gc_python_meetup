import gc
import pprint
import sys
import objgraph

import ctypes


class PyObject(ctypes.Structure):
    _fields_ = [
        ("refcnt", ctypes.c_long),
        ("1", ctypes.c_char_p),
        ]

gc.disable()  # Disable generational gc

lst = [5]
lst.append(lst)

# Store address of the list
lst_address = id(lst)


object_1 = {"1": "onne"}
object_2 = {"1": "twowo"}
object_1['obj2'] = object_2
object_2['obj1'] = object_1

obj_address = id(object_1)

objgraph.show_refs([object_1, object_2], filename='sample-graph_1.png')
# objgraph.show_refs([1], filename='sample-graph_1.png')

# Destroy references
del object_1, object_2

# Destroy the lst reference
del lst


# Uncomment if you want to manually run garbage collection process 
# gc.collect()


# Check the reference count
print(PyObject.from_address(obj_address).refcnt)
print(PyObject.from_address(lst_address).refcnt)

