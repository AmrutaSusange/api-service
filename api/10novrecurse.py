def print_hello(a):
    if a == 0:
        return

    print_hello(a - 1)
    print(f'hello {a}')

def employee(t):
    if t == 1:
        print(f'I am starting my work for which I have been given time {t}')
        print(f'work is done for employee who was given {t}')
        return

    print(f'I am starting my work for which I have been given time {t}')
    employee(t-1)
    print(f'work is done for employee who was given {t}')



def b(k):
    print('1')
    print('2')

    print('3')

    if k == 0:
        return

    k = k-1
    a(k)
    print(4)

def a(a):
    print('1')
    print('2')

    print('3')

    if a == 0:
        return
    print(4)


if __name__ == "__main__":
    print_hello(5)







