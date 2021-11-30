# -*- coding: UTF-8 -*-

def func(a,**kwargs):
    print(a,kwargs)

if __name__ == '__main__':
    '''
    这次，代码打印出“1,{'c': 3,'b': 2}”，因为1按照名称传递给a，**kargs把其他关键字参数收集到一个字典中。
    我们可以用任何迭代工具来步进任何额外的关键字参数字典（例如，for key in kargs:）。
    '''
    func(a=1,c=3,b=2)