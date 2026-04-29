'''

Iterables vs Iterators

'''


lst = [1, 2, 3, 4]

for i in lst:
    print(i)

'''

Since we can Iterate over list. List is an iterable

iter() funciton converts iter(iterable) --> iterator

iterator__
          |
           it traverses a collection one element at a time
           it doesnot store the the values in the collection at once it get one value at a time

We can retrive the values from the iterator one by one by using the next(iterator)

'''

next(gen)  # 1
next(gen)  # 2
next(gen)  # 3
next(gen)  # 4
next(gen)  # ERROR --> this gives a StopIteration
'''

you need to handle that using try catch block 

but in 
for i in gen:
    print(i)

the StopIteration is alreadt handled and this will stop the iteration
'''


'''
there are protocols of iterator

1) there must be a __iter__() method
        this returns the iterator object itself
'''

gen.__iter__()
# returns the object gen itself

gen.__next__()
# returns the next item in the sequence
