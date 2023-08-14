import time as time_library
import math as math_library
import multiprocessing as ml_library

results_a=[]
results_b=[]

def cube_calculations(numbers):
    for num in numbers:
        results_a.append(math_library.sqrt(math_library.pow(num, 3)))

def fourth_calculations(numbers):
    for num in numbers:
        results_b.append(math_library.sqrt(math_library.pow(num, 4)))


if __name__=="__main__":
    number_list=list(range(5000000))
    start_time=time_library.time()
    cube_calculations(number_list)
    fourth_calculations(number_list)
    finish_time=time_library.time()
    print("No threads: ", finish_time-start_time)
    p1=ml_library.Process(target=cube_calculations, args=(number_list, ))
    p2=ml_library.Process(target=fourth_calculations, args=(number_list, ))
    start_time2=time_library.time()
    p1.start()
    p2.start()
    finish_time2=time_library.time()
    print("With threads: ", finish_time2-start_time2)