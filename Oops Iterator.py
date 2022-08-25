"""nums = [7,6,4,8]

it = iter(nums)

print(it.__next__())
print(next(it))
print(it.__next__())
print(next(it))"""

# Create a Own iterartor

class Topten:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration

values = Topten()

for i in values:
    print(i)
