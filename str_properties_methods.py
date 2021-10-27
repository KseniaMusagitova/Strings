# свойства и методы
# Immutable. Строки не изменяемы и чтобы заменить символ...
first_name = 'Jake'

first_two_letters = first_name[:2]
print(first_two_letters)
last_letter = first_name[-1:]
print(last_letter)

# Concatenable
new_first_name = first_two_letters + 'n' + last_letter
print(new_first_name)


greeting = 'Hello'
greeting = greeting + ' Python'
print(greeting)

# Multiplication
yummy = 'Yum '
print(yummy * 3)

print(yummy.upper())
print(yummy.lower())
print(yummy)

# Примеры
long_srting = 'This is long srting'
print(long_srting.split())
print(long_srting.split('s'))

greeting = 'Hello Python!'
text1 = greeting[6]
text2 = greeting[8:10]
text3 = text1 + 'a' + text2
print(text3)

z = 'z'
text = z * 7
print(text)
print(text.upper())

