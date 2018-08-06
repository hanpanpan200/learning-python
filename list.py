wizard_list = ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter']
print('Wizard list: %s' % wizard_list)
print('Third ingredient: %s' % wizard_list[2])
print('First and second ingredients: %s' % wizard_list[0:2])

number_list = [0, 1, 2, 3]
str_list = ['a', 'b', 'c', 'd']
two_dimensional_list = [number_list, str_list]
print('Second element for number_list: %s' % two_dimensional_list[0][1])
print('Second element for str_list: %s' % two_dimensional_list[1][1])
print('First two elements for two_dimensional_list: %s' % two_dimensional_list[0:2])
print('First element for the first two elements in two_dimensional_list: %s' % two_dimensional_list[0:2][1])

# Append element to list

list = [0, 1, 2]
print('Original list: %s' % list)
list.append(3)
print('Result after append 3 to the list: %s' % list)

# Delete element from list

del list[0]
print('Result after delete first element: %s' % list)

# Add two list to one

list1 = [0, 1, 2]
list2 = ['aa', 'bb', 'cc']
list3 = list1 + list2
print('After adding %s and %s, the result is %s' % (list1, list2, list3))

del list3[0]
print('After deleting the first element of list3, the result is %s' % list3)

print(list1 * 2)