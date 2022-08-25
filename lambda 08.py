#Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function

nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]

Netgative_num = list(filter(lambda nums : nums<0,nums))
Positive_num = list(filter(lambda nums : nums>0,nums))

print(sum(Netgative_num))
print(sum(Positive_num))