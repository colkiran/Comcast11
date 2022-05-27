
class MyNumbers:

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <= self.max:
            res = self.n
            self.n += 1
            return res
        else:
            raise StopIteration


myObj = MyNumbers(10)
iterObj = iter(myObj)

print(next(myObj))
print(next(myObj))
print(next(myObj))
print(next(myObj))
print(next(myObj))
# print(next(myObj))

print("-" * 40)
for i in myObj:
    print(i, end=" ")
print(' ')
