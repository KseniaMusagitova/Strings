# Форматирование
age = 23
print('Jack is ' + str(age) + ' years old.')

name = 'Jack'
age = 23
name_and_age = 'My name is {0}. I\'m {1} years old.'.format(name, age)
print(name_and_age)

name_and_age = 'My name is {0}. I\'m {1} years old.'.format('Jack', 23)
print(name_and_age)

name_and_age = 'My name is {}. I\'m {} years old.'.format(23, 'Jack')
print(name_and_age)

week_days = 'There are 7 days in a week: {}, {}, {}, {}, {}, {}, {}.'\
    .format('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday')
print(week_days)

week_days = 'There are 7 days in a week: {su}, {mo}, {tu}, {we}, {th}, {fr}, {sa}.'\
    .format(mo = 'Monday', we = 'Wednesday', th = 'Thursday', tu = 'Tuesday',
            fr = 'Friday', su = 'Sunday', sa = 'Saturday')
print(week_days)

week_days = 'There are 7 days in a week: {su}, {su}, {su}, {su}, {su}, {su}, {su}.'\
    .format(mo = 'Monday', we = 'Wednesday', th = 'Thursday', tu = 'Tuesday',
            fr = 'Friday', su = 'Sunday', sa = 'Saturday')
print(week_days)

float_result = 1000 / 7
print(float_result)
print('The result of division is {0:5.3f}'.format(float_result))
print('The result of division is {0:10.3f}'.format(float_result))

print("""
{} {} {}
{} {} {}
{} {} {}
""".format(1.34344, 345.564564, 44.54645645, 2424.4366,
           1.34344, 345.564564, 44.54645645, 2424.4366,
           453.43543))

print("""
{0:10.2f} {1:10.2f} {2:10.2f}
{3:10.2f} {4:10.2f} {5:10.2f}
{6:10.2f} {7:10.2f} {8:10.2f}
""".format(1.34344, 345.564564, 44.54645645, 2424.4366,
           1.34344, 345.564564, 44.54645645, 2424.4366,
           453.43543))

name = 'Jack'
age = 23
name_and_age = 'My name is {0}. I\'m {1} years old.'.format(name, age)
print(name_and_age)
name_and_age = f'My name is {name}. I\'m {age} years old.'
print(name_and_age)

print('My name is %s. I\'m %d years old.' %(name, age))
print('My name is %s. %s %d years old.' %(name, "I'm", age))


print("""
{0:15.4f} {1:15.4f} {2:15.4f} {3:15.4f}
{3:15.4f} {4:15.4f} {5:15.4f} {6:15.4f}
""".format(1.34344, 5.564564, 4.54645645, 4.4366787,
           1.34344, 3.564564, 4.54645645, 2.43667))