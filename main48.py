class Employee:
    def __init__(self):
        print("Employee created.")
    def __del__(self):
        print("Destructor called.")
def display():
    print("Making object...")  
    emp=Employee()
    print("Function end...")
    return emp

print("Calling display() function...")
obj=display()
print("Program End...")


