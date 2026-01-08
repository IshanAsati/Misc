BadReactionTester

A simple Python-based reaction time tester that measures how quickly a user responds after a random delay. Built as a learning project to explore timing, randomness, and basic user interaction in Python.

Overview

BadReactionTester waits for a random amount of time, then prompts the user to react as fast as possible by pressing Enter. The program measures the reaction time and classifies it into rough performance categories.

This project is intentionally minimal and terminal-based.

Features

Randomized wait time before the reaction prompt

High-resolution timing using time.perf_counter()

Reaction time measurement in seconds

Simple performance grading (w, mid, l)

Lightweight and dependency-free

How It Works

The program generates a random delay.

The user waits while the program counts down.

When prompted, the user presses Enter as fast as possible.

The program measures the time between prompt and input.

The reaction time is classified and displayed.

Code
import random
import time

print("Welcome to this goofy aah program")

def main():
    random_num = random.randint(2,7)
    i = 0
    print("press enter to do the thing")
    while i != random_num:
        print("please wait")
        i += 1
        time.sleep(1)

    start_time = time.perf_counter()
    input("press enter NOW")
    end_time = time.perf_counter()

    decimal_time = end_time - start_time
    elapsed_time = int(decimal_time * 100)

    if elapsed_time <= 25:
        print("w")
    elif elapsed_time in range(26, 40):
        print("mid")
    else:
        print("l")

    print(f"your actual time was {decimal_time}s")

main()

Requirements

Python 3.x

Uses only built-in modules (random, time)

Usage

Run the program from the terminal:

python bad_reaction_tester.py


Follow the on-screen instructions and react as fast as possible when prompted.

Limitations

Reaction grading thresholds are arbitrary

Countdown delay is predictable once it starts

No false-start detection

Only a single reaction trial

No result averaging or data persistence

Planned Improvements

Truly random delay using random.uniform

False-start detection

Multiple trials with averaged results

Reaction time grading in milliseconds

Cleaner program structure with proper entry-point guard

Disclaimer

This project is a learning exercise and not a scientifically accurate reaction-time measurement tool. Results should not be taken seriously unless you enjoy lying to yourself.