# -*- coding: UTF-8 -*-

x = 'spam'

def func():
    x = 'ni!'
    print(x)

if __name__ == '__main__':
    '''.这会在一行上打印'NI'，在另一行打印'Spam'，因为函数中引用的变量会找到其本地变量，而print中引用的变量会找到其全局变量。'''
    func()
    print(x)