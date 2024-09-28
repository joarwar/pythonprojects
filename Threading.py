
import time 
import threading

number = 1

def user_input():
    global number

    while True:
        input_val = input('ange nytt tal ')
        number = int(input_val)
        if number == 0:
            break

def file_printer():
    f = open('my_thread_numbers.txt', mode="w")
    while number !=0: 
        time.sleep(1)
        f.write(str(number))
        f.flush()
    f.close()


print(" start of program - no no threads")

t1 = threading.Thread(target=user_input)
t2 = threading.Thread(target=file_printer)

t1.start()
print("thread 1 started")

t2.start()
print("thread 2 started")

t1.join()
print("end of thread 1")
t2.join()
print("end of thread 2")