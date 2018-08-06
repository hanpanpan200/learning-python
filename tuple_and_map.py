tuple = (1, 2, 3, 4)
print('First element of the tuple is %s' % tuple[0])

# Can only concatenate tuple
# tuple2 = (0)
# print(tuple + tuple2)

# 'tuple' object does not support item assignment
# tuple[0] = 5

favorite_spots = {'Grace': 'Football', 'Max': 'Basketball'}
print(favorite_spots)

favorite_spots['Grace'] = 'Baseball'
print(favorite_spots)

del favorite_spots['Grace']
print(favorite_spots)

# Key error
# del favorite_spots['Grace']