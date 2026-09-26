"""
Midterm Practical Exam — Network Device Inventory Tool
Student: Stephen Sedrick C. Basilio
"""

devices = []  # starts empty — the user adds devices as the program runs

def display_menu():
    # print the menu, return the user's choice
    pass

def add_device(device_list):
    # ask for name, IP, status — build the string, add to the list
    pass

def view_devices(device_list):
    # loop through and print every device — handle empty list
    pass

def count_active_inactive(device_list):
    # loop through, count Active vs Inactive, return both
    pass

def find_device(device_list):
    # ask for a name, search the list, print result or "not found"
    pass

# BONUS (optional)
def remove_device(device_list):
    # your code here
    pass

def main():
    running = True
    while running:
        choice = display_menu()
        # use if/elif to call the right function based on choice
        # set running = False when the user picks Exit

main()
