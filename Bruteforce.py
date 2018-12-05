from string import printable
from itertools import product
import time

start_time = time.time() # defines start time for program

found = False

for length in range(1, 6): # safe length for trying password
    password = 'admin' # use a test password
    attempted_password = product(printable, repeat=length)

    for attempt in attempted_password:
        attempt = ''.join(attempt) # It joins letters together

        if attempt == password: #If password is found in the above attempt break
            print("Your password is: " + attempt)
            found = True
            break

    if found:
        break

print("The program took --- %s seconds ---" % (time.time() - start_time)) # prints total time taken for program

#4 letter characters usually take 6 seconds
#5 letter characters can take more than 800 seconds
