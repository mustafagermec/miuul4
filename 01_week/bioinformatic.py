print('Hello World!')
lis = [2, 5, 7, 8, 12]
for i in lis:
    if i % 2 == 0:
        print('the number is even')
    else:
        print('the number is odd')


def say_hello():
    print('hello!')

set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

set2.issuperset(set1)
set1.issuperset(set2)