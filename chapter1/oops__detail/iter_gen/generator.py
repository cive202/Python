'''

you can create a generator by using `yeild`. yeild statement returns a value for the generator and suspendes the exectution of the fucntion until the next value is requested

'''


def my_generator(n):
    for i in range(n):
        yield i


gen = my_generator(3)
# it can be seen by:
# next(gen)
for i in gen:
    print(i)


'''
generator is very efficent

in the above case gen --> this would be a iterator(list). and if the length of the length is 400000.
the list size would be 400000 which is memory inefficent 

and in the case of generator the list in not pre made it is used . it is dyamically generated. it generates the values when 
the value is requested
'''
