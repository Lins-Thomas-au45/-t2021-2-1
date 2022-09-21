class calculator():
    def __init__(self,a,b): 
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a -self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b

a = float(input("Enter first number"))
b = float(input("Enter second number"))
c = input("Choose type of operation => Add,sub,mul,div")
obj = calculator(a,b)
if (c == "Add"):
    print("The answer is ",obj.add())
elif(c == "Sub"):
    print("The answer is ",obj.sub())
elif(c == "mul"):
    print("The answer is ",obj.mul())
elif(c == "div"):
    print("The answer is ",obj.div())
else:
    print("Invalid entry")    