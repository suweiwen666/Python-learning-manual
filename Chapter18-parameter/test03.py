# -*- coding: UTF-8 -*-

def func(a,*pargs):
    print(a,*pargs)

if __name__ == '__main__':
    '''
    这段代码打印出“1 （2,3）”，因为1传递给a，*pargs把其他的位置参数收集到一个新的元组对象中。
    我们可以用任何迭代工具来步进任何的额外的位置参数元组（例如，for arg in pargs:）。
    '''
    func(1,2,3)