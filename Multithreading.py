#more than one: multi threading in python allows you to run multiple threads concurrently in with in a single process
#each thread represent a seperate flow of control ,it is useful when u have tasks that can run independently and can run from parallel execution
import threading
import time
def print_numbers():
    for i in range(1,6):
        print("thread A:",i)
        time.sleep(0.5)#simulate some work
def print_letters():
    for letter in ['a','b','c','d','e']:
        print("thread B:", letter)
        time.sleep(0.5)

#create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

#start threads
thread1.start()
thread2.start()

#wait for threads to finish
thread1.join()
thread2.join()

print("main thread exiting...")


# gil:global interpretter lock
"""sleep(5) will take strict orders but wait(5) will not take strict orders it will take if servers are available then it starts at that time only"""
