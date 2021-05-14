import py_compile
file = input('Enter File Name:')
def Encrypting():
    n = py_compile.compile(f'{file}')
    print(n)
Encrypting()