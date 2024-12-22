immutable_var = (1, 2, 'a', 'b')
print("Immutable tuple: ", immutable_var)
#immutable_var[0] = 100
# Кортежи в Python являются неизменяемыми (immutable), то есть их элементы не могут быть изменены после создания.
mutable_list = [1, 2, 'a', 'b']
mutable_list.append('Modified')
print("Mutable list: ", mutable_list)