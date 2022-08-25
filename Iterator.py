nums = [1,2,4,7]

it = iter(nums)

print(next(it))
print(next(it))

print(it.__next__())
print(it.__next__())

