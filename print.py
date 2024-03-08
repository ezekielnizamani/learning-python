# print('Hello World','and',87,False)
# print('Hello')


# hello ='tim'
# world = 'World'
# world = hello;
# hello = 'no';
# print(hello,world)

# hello = 'hello'.upper()
# print(hello)


# x = input('Name: ')

# if x == 'hizqeel':
#     print('Hizqeel you are great')
# elif x == 'adam':
#     print('Bye Adam')
# else:
#     print(' else print this')


# list and tupple
# list
# list are mutable 
# x = [4,True,'Hi']
# Add item at the end of list
# x.append('hello');
# add  multiple item at the end of list
# x.extend([4,5])
# pop remove remove from list and return it by deafult it is last item if you provide index it will do same  to that
# print(x.pop())
# x[0] =  'hello'
# print(x);

# tupple
# tupple are immutable   which means we can't modify it 
# x = (0,0,2,2)

# loops
# for
# while
# start, stop,step in range 
# if just pass one arugemnt it if by deafult Stop
# if we pass two arugemnt first is Start second is stop
# if pass three arugment first is start second is stop thaird is step
x = [3,4,51,3131,1]
 
# for i in range(1,10,3):
#     print(i)

# for i,cur in enumerate(x):
#     print(i,cur)

# while loop

# i = 0 
# while i < 10:
#     print(i,'run')
#     i+= 1



# slice
# x = [0,1,2,3,4,5,6,7,8]
# y = ['hi','hello','bye']
# s = 'hello'
# sliced = x[start:stop:step]

# sliced = x[0:9:3]

# print(sliced)

# sets
# set is 
# x = set()
# s = {4,32,2,2}
# s2 = {32,4,22,1}
# s.add(5)
# s.remove(2)
# print(4 in s)
# print(s.union(s2))
# print(s.intersection(s2))

# dect
x = {'key':4}

# print('key' in x); # return true
# print(list(x.values())) # return list of values
# print(list(x.keys())) # return list of keys


# del x['key']
# for key, value in x.items():
    # print(key,  value)

# comprehensions

# x = [i for i in range(100) if i % 10 == 0]
# print(x)


# functions

# def run(x,y,z =None):
#     print('run',x,y,z)
#     return x*y,x+y

# r1,r2 = run(5,6,4)
# print(r1,r2);

# def func(x):
#     def func2():
#         print(x)
#     return func2

# print(func(3)())


# def func(x,y):
#     print(x,y)

# pairs = [(1,2),(3,4)]

# for pair in pairs:
#     func(*pair)
# unpack
# print(*x)

# def func(*args,**kwargs):
#     print(*args)

# func(1,2,3,4,5,one=0,two=1)

# x = 'tim'

# def func(name):
#     global x
#     x = name
# print(x)
# func('changed')
# print(x)
# error
# raise Exception('Bad')

# handle Exception
# try:
#     x= 7 / 0
# except Exception as e:
#     print(e)
# finally:
#     print('finally')

# lambda 
# x = lambda x: x+5

# print(x(2))

# map and filter

# x = [1,2,3,4,5,6,7,8,9,5,24,14141]


# mp = map(lambda i: i+2,x)

# print(list(mp))

# fp = filter(lambda i: i % 2 ==0,x)
# print(list(fp))

# F strings 
name = 'hizqeel'
x = f'hello {name}'
print(x)