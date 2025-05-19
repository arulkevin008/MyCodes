class calculator():
    def _init_(self,n1,n2):
        self.num1=n1
        self.num2=n2
    def cal(self):
        print("Addition:",self.num1+self.num2)
        print("Subtraction:",self.num1-self.num2)
        print("Division:",self.num1/self.num2)
        print("Multiplication:",self.num1*self.num2)

obj1=calculator("10","2")
obj1.cal()
        
