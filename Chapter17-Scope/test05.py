# -*- coding: UTF-8 -*-

x = 'spam'
def func():
    x = 'ni!'
    def nested():
        print(x)
    nested()

if __name__ == '__main__':
    '''这个例子的输出还是'NI'一行，而'Spam'在另一行，因为嵌套函数中的print语句会在所在的函数本地作用域中发现变量名，而末尾的print会在全局作用域中发现这个变量。'''
    func()
    print(x)