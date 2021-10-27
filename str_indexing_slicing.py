greeting = 'Hello Python!'
greeting_length = len(greeting)
print(greeting_length)
print(len(greeting))

# Indexing
print(greeting[0])
print(greeting[6])
print(greeting[-1])

# Slicing
print(greeting[2:5])
print(greeting[6:10])
print(greeting[-5:-2])
print(greeting[2:])
print(greeting[:4])
print(greeting[:])
print(greeting[::2])
print(greeting[::3])
print(greeting[1::3])
print(greeting[1:9:3])
print(greeting[::-1])

# Примеры
greeting = 'Hello Python!'
print(greeting[3])

print('Hello Python!'[3])

greeting = 'Hello Python!'
print(greeting[:2])
print('Hello Python!'[:2])

greeting = 'Hello Python!'
new_text = greeting[6] + 'a' + greeting[8:10]
print(new_text)
