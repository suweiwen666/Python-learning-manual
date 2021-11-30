# -*- coding: UTF-8 -*-

x='spam'

def func():
    print(x)

if __name__ == '__main__':
    '''这里的输出是'Spam'，因为函数引用的是所在模块中的全局变量（因为不是在函数中赋值的，所以被当作是全局变量）。'''
    func()
    pass