import os
from CallMethod import method

# Get the path of the imported CallMethod module
import CallMethod

print("File path of CallMethod:", CallMethod.__file__)

obj = method("Habib", 21120124130081)

obj.intro()

obj.timer(10)
