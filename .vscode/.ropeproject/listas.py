my_list = [1,2,3]
my_list[0]
my_list.append(4)
print(my_list)
my_list[0] = 'Holas'
print(my_list)
print(my_list.pop())
print(my_list)
a = [0,1,2,3,4,5]
b = a
b.pop()
# print(id(b))
# print(id(a))
print('Clonar listas')
a = [1,2,3]
print(id(a))
c = list(a)
print(id(c))
d = a[::]
print(id(d))
