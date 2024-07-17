class calculator1:

    num=100 #class varaibles -- constant

    #Default constcrucor
    def __init__(self,a,b):
        self.firstNumber=a
        self.SecondNumber=b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def summation(self):
         return self.firstNumber +self.SecondNumber +calculator1.num

obj1=calculator1(2,3)

obj1.getData()
#print(obj1.num)
print(obj1.summation())

obj2=calculator1(4,5)

obj2.getData()
#print(obj2.num)
print(obj2.summation())