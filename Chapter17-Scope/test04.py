# -*- coding: UTF-8 -*-
x='spam'
def func():
    global x
    x = 'ni!'

if __name__ == '__main__':
    func()
    print(x)