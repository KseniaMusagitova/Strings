greeting = 'Hello'
first_name = 'Jack'
last_name = 'White'
exclamation_sign = '!'
white_space = ' '
whole_sentence = greeting + white_space + first_name + ' ' \
                 + last_name + exclamation_sign
print(whole_sentence)

long_string = 'This is the long string'
print(long_string)

# экранирование, Escaping \ (back slash)
some_string = 'I\'m a programmer'
print(some_string)

another_string = "I want to learn \"Python\""
print(another_string)

string_with_new_lines = "Hello \n My name is YouRa"
print(string_with_new_lines)

string_with_new_lines = "Hello \nMy name is YouRa"
print(string_with_new_lines)

string_with_new_lines = "Hello \n        \rMy name is YouRa"
print(string_with_new_lines)

numbers = '1\t23\t4567'
print(numbers)

some_text = "\t Hello! \nI'm very glad to see you!"
print(some_text)

# тройные кавычки Triple quotes
string = """This is 
text 
with "triple quotes" """
print(string)
another_string = '''This is text with "triple quotes" '''
print(another_string)

first_name = 'Ivan'
last_name = 'Ivanov'
age = '18'
info = "Hi! My name is" + first_name + ' ' + last_name, "I'm" + ' ' + age + ' ' 'years old'
print(info)

# 1 способ
t = '\t\tBaa, baa, black sheep, \
\n\t\tHave you any wool? \
\n\t\tYes sir, yes sir,\
\n\t\tThree bags full, \
\n\t\tOne for the master,\
\n\t\tOne for the dame,\
\n\t\tAnd one for the little boy \
\n\t\tWho lives down the lane \
\n\t\tBaa, baa, black sheep, \
\n\t\tHave you any wool? \
\n\t\tYes sir, yes sir, \
\n\t\tThree bags full'
print(t)

# 2 способ
t = """\t\tBaa, baa, black sheep, 
\t\tHave you any wool? 
\t\tYes sir, yes sir,
\t\tThree bags full, 
\t\tOne for the master,
\t\tOne for the dame,
\t\tAnd one for the little boy
\t\tWho lives down the lane 
\t\tBaa, baa, black sheep, 
\t\tHave you any wool?
\t\tYes sir, yes sir, 
\t\tThree bags full"""
print(t)