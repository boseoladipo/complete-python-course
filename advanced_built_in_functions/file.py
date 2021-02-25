class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self

my_gen = FirstHundredGenerator()
print(next(my_gen))
print(next(my_gen))

print(sum(FirstHundredGenerator()))
for i in FirstHundredGenerator():
    print(i)