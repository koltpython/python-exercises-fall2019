print('Foo says her name is "Bar".')
print('Bar says her name is "Foo".')
foo_name = 'Bar'
bar_name = 'Foo'

# Your code starts here.

temp = foo_name
foo_name = bar_name
bar_name = temp

# Your code ends here.

print(f'In fact, Foo\'s name is {foo_name}')
print(f'In fact, Bar\'s name is {bar_name}')