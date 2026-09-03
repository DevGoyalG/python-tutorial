# static methods - are methods that belong to a class rather than an instance of the class.
# they are defind using the @staticmethod decorator and do not have access to the instance of the class (i.e. self)

class Math:
    def __init__(self, num):
        self.num = num

    def addNum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a,b):
        return a+b

# result = Math.add(4,5)
# print(result)

a= Math(5)
print(a.num)
a.addNum(6)
print(a.num)
print(a.add(4,5))