###################################################################################
# Calling threads in python and C++ are similar
import time
import threading

# Python Threading Example for Beginners
# First Method
def greet_them(people):
    for person in people:
        print("Hello Dear " + person + ". How are you?")
        time.sleep(1)

# Second Method
def assign_id(people):
    i = 1
    for person in people:
        print("Hey! {}, your id is {}.".format(person, i))
        i += 1
        time.sleep(1)


people = ['Richard', 'Dinesh', 'Elrich', 'Gilfoyle', 'Gevin']

#Created the Threads
t1 = threading.Thread(target=greet_them, args=(people,))
t2 = threading.Thread(target=assign_id, args=(people,))

#Started the threads
t1.start()
t2.start()

#Joined the threads
t1.join()
t2.join()