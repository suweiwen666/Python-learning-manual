# -*- coding: UTF-8 -*-

def func():
    x = 'ni!'
    def nested():
        nonlocal x
        x = 'spam'
    nested()
    print(x)

if __name__ == '__main__':
    '''
    这个示例打印出'Spam'，因为nonlocal语句（Python 3.0中可用，但Python2.6中不可用）意味着在嵌套函数中对X赋值，以修改嵌套函数的本地作用域中的X。
    没有这条语句，这个赋值将会把X当作是嵌套函数的本地变量，使它成为一个不同的变量，那么这段代码将会打印出'NI'。
    '''
    func()