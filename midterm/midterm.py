"""
Midterm Practical Exam — Network Device Inventory Tool
Student: Stephen Sedrick C. Basilio
"""

devices = []  # starts empty — the user adds devices as the program runs

def display_menu():
    # print the menu, return the user's choice
    print(f"=== Network Device Inventory ===")
    print(f"1. Add a device")
    print(f"2. View all devices")
    print(f"3. Count active vs inactive devices")
    print(f"4. Find a device by name")
    print(f"5. Exit")
    user_choice = int(input("Choose an option: "))
    return choice
    pass

def add_device(device_list):
    # ask for name, IP, status — build the string, add to the list
    name = input("Enter Device Name: ")
    name = input("Enter IP Address: ")
    name = input("Active/Inactive: ")
    pass

def view_devices(device_list):
    # loop through and print every device — handle empty list
    for device in devices:
        print(f"{name} - {address} - {status}")
    pass

def count_active_inactive(device_list):
    # loop through, count Active vs Inactive, return both
    pass

def find_device(device_list):
    # ask for a name, search the list, print result or "not found"
    for device in devices:
        if device["name"] == name:
            return device
        else:
            print("Not Found")
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
        if user_choice == 1:
            add_device
        if user_choice == 2:
            view_devices
        if user_choice == 3:
            count_active_inactive
        if user_choice == 4:
            find_device
        if user_choice == 5:
            set running = False

main()
