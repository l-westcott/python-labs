# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.
from datetime import datetime
now = datetime.now()
print(now.strftime("%d-%m-%Y %H:%M:%S"))
