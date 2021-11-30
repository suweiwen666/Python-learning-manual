# -*- coding: UTF-8 -*-

x = 'spam'

def func():
    x = 'ni!'

if __name__ == '__main__':
    '''这里的输出也是'Spam'，因为在函数中赋值变量会将其变成本地遍历，从而隐藏了同名的全局变量。print语句会找到没有发生改变的全局（模块）作用域中的变量。'''
    print(func())
    print(x)