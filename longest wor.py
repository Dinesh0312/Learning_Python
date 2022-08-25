list = ['potato', 'tomato', 'apple', 'kiwi', 'avocado','lichi', 'pear', 'pineapple']

def longest_word(list):
        z = max(list,key=len)
        return z

z = longest_word(list)

print(f"longest word : {z} and length is : {len(z)}")