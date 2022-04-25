# Here we learn the sintax for classes and how they are used.

class Add:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def add(self):
        result = self.var1 + self.var2
        return result

result = Add(2, 2)

solution = result.add()

print("The result of the operation", '"' + str(result.var1), "+", str(result.var2) + '"', "is", solution) #The result of the operation "2 + 2" is 4

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Here we learn that classes are useful for functions that are related to each other, like adding and subtracting.

class Math:
    def __init__(self, var21, var22):
        self.var21 = var21
        self.var22 = var22

    def subtract(self):
        result2 = self.var21 - self.var22
        return result2

    def add(self):
        result2 = self.var21 + self.var22
        return result2

Math = Math(5, 2)

solutionAdd = Math.add()
solutionSubtract = Math.subtract()


print("The result of the operation", '"' + str(Math.var21), "+", str(Math.var22) + '"', "is", solutionAdd) #The result of the operation "5 + 2" is 7 
print("The result of the operation", '"' + str(Math.var21), "-", str(Math.var22) + '"', "is", solutionSubtract) #The result of the operation "5 - 2" is 3

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

# And here we learn that classes are used to return specific variables and not execute any functions like you see below.
# ! This returns an Error:

# class Print:
#      def __init__(self, printBad):
#         self.printBad = printBad

#     def actualPrint(self):
#         printVar = print(self.printBad)
#         return printVar

# hereWeGo = Print("Hello World")

# Print.actualPrint()
