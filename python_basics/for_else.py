def example_1():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print('%d equals %d * %d' % (n, x, n/x))
                break
        else:
            print('%d is a prime number.' % n)

def example_2(list, n):
    for i in list:
        if i == n:
            print('%d is in the list.' % n)
            break
    else:
        print('%d is not in the list.' % n)


example_1()

ls = list(range(1, 10))
example_2(ls, 5)
example_2(ls, -1)
