# -*- coding: UTF-8 -*-
def func(a,b,c=3,d=4):
    print(a,b,c,d)

if __name__ == '__main__':
    '''
    这里的输出是“1564”：1按照位置匹配a，5和6按照*name位置匹配b和c（6覆盖了c的默认值），并且d默认为4，因为它没有传递一个值。
    '''
    func(1,*(5,6))