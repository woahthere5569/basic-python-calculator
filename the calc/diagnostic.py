import sys
import os

print("Python executable:", sys.executable)
print("Current working directory:", os.getcwd())
print("sys.path:")
for p in sys.path:
    print("  ", p)

import Functions as func

print("Functions module loaded from:", func.__file__)
print("Has attribute 'value'? ->", hasattr(func, "value"))

try:
    print("func.value =", func.value)
except AttributeError as e:
    print("AttributeError:", e)
