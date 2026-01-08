import random
import time



def main():
    random_num = random.randint(2,7)
    i = 0
    print("press enter to do the thing")
    while i != random_num:
        print("please wait")
        i += 1
        time.sleep(1)
#        print(i)
#        print(random_num)
    start_time =time.perf_counter()
    input("press enter NOW")
    end_time = time.perf_counter()
    decimal_time = end_time - start_time
    elapsed_time = int(decimal_time * 100)
#    print(elapsed_time, decimal_time)
    if elapsed_time <= 25:
        print("w")
    elif elapsed_time in range(26, 40):
        print("mid")
    else:
        print("l")
    print(f"your actual time was {decimal_time}s")
if __name__ == "__main__":
    print("Welcome to this goofy aah program")
    main()