class IOString():
    def __init__(self):
        self.str1=""
    def getString(self):
            self.str1=input("Enter a string:")
    def printString(self):
            print("Result:",self.str1.upper())

object=IOString()
object.getString()
object.printString()