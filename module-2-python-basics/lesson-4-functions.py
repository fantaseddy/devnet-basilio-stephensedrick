"""
Module 2 — Lesson 4: Functions
Student: Stephen Sedrick C. Basilio
Date: September 23, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
A function is a reusable block of code that performs a specific task. Instead of writing the same code again every time I need it, I can put the code inside a function and call the function whenever I need it. Like let's say an animal sound, such as bark.


============================================
KEY VOCABULARY
============================================
- function: reusable block of code that performs a specific task
- def: Python keyword used to define a function
- parameter: variable listed inside a function definition that represents a value the function can receive
- argument: actual value passed to a function when the function is called
- return: statement used to send a value back from a function


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

def calculate_average(waterintakeday1, waterintakeday2, waterintakeday3):
    average = (waterintakeday1 + waterintakeday2 + waterintakeday3) / 3
    return average

my_average = calculate_average(5, 8, 7)
print(f"My average daily water intake these past 3 days is {my_average:.2f}")

def greet_student(name, subject="DEVNET"):
    return f"Hi, I'm {name}! And I bring you {subject}."

message = greet_student("Seddy")
print(message)

message2 = greet_student("Seddy", "VALORANT")
print(message2)

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
This is a tricky and confusing topic. I confused a parameter with an argument, but a parameter is the variable written when I define the function, while an argument is the actual value I give the function when I call it.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
Functions connect to the topics I already learned because they can use variables, data types, conditions, loops, and lists inside them.
"""

