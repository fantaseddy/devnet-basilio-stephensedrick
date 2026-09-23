"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Stephen Sedrick C. Basilio
Date: September 23, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Control flow is how a program decides what it should do based on a situation, basically controlling the flow. What that means is that instead of always running every instruction in the exact same way, we can use if, elif, and else to make the program choose between different paths.  Like a CYOA RPG!


============================================
KEY VOCABULARY
============================================
- condition: something that the program checks to decide what to do
- if / elif / else: statements used to create different paths depending on whether conditions are either true or false
- comparison operator: an operator used to compare values, such as ==, !=, >, <, >=, and <=
- boolean expression: an expression that results in either True or False
(add more as needed)
- control flow: the order or path that a program follows while it is running

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

ac_temperature = 26

if ac_temperature >= 32:
print("Ang init, sira na naman AC?")
elif temperature >= 25:
print("*sleeps comfortably*")
else:
print("Ayun, nilagnat sa lamig.")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
I have experienced mixing up = and ==. = is used to assign a value to a variable, while == is used to check if two values are equal.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
Control flow and the operators above are basics in Python that also help me further understand future lessons in this language. If/elif/else can get very complicated when nested, though.
"""
