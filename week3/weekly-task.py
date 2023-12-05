def list_number(first,last):
    for a in range(first,last):
        print(f'0{a}' if 0 <= a <= 9 else a,end=', ')
    print(f'{last}\n')

list_number(0,99)