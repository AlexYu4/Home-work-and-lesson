my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print("Dict: ", my_dict)
print(my_dict['Masha'])
print(my_dict.get('Artem'))
my_dict['Artem'] = 1915
my_dict['Kamila'] = 1981
del my_dict['Egor']
print(my_dict)
my_set = {1, 'Яблоко', 42.314}
print(my_set)
my_set.add(13)
my_set.add((5, 6, 1.6))
my_set.remove(1)
print(my_set)