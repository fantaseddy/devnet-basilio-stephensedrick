"""
Module 2 — Lesson 3: Loops & Lists
Student: Stephen Sedrick C. Basilio
Date: September 23, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
A list allows me to store several values together instead of creating a separate variable for every value, like I can have one list containing my favorite foods, or names of my family members, or VALORANT win-lose match histories. A loop allows the program to repeat a set of instructions, where a for loop is useful when I want to go through each item in a list or repeat something a specific number of times but a while loop keeps repeating as long as its condition is True.


============================================
KEY VOCABULARY
============================================
- list: a collection of multiple values stored together in one variable
- for loop: a loop that repeats through a sequence, such as the items in a list
- while loop: a loop that continues running while a condition remains True
- index: the position of an item in a list. Python starts counting indexes from 0
- iteration: one complete repetition of a loop
(add more as needed)
- loop: repeats a set of instructions
- item: an individual value stored inside a list

============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

subjects = ["DEVNET", "CYBSEC", "SYSADM", "NET2", 'ELEC1', 'ELEC2', 'IOT']

for subject in subjects:
print(f"I study {subject}.")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
Orders can be confusing because Python starts list indexes at 0 instead of 1. So that is something to consider and remember for me.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
They will be useful when I start working with larger programs and bigger amounts of data in the future, such as networking or cybsersecurity.
"""
