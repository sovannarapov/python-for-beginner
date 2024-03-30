def display(a=0, b=0, *args):
    print(f'a={a}')
    print(f'b={b}')
    # the rest arguments will return as tuple
    print(f'args={args}')
    for i in range(0, len(args)):
        print(f'args={args[i]}')


display(1, 2, 3, 4, 5, 6, 'Setec', 20.22, [10, 20, 30])
