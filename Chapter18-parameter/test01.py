# -*- coding: UTF-8 -*-

def func(a,b=4,c=5):
    print(a,b,c)

if __name__ == '__main__':
    '''
    这里的输出是“125”，因为1和2按照位置传递给了a和b，并且c在调用中被忽略了，默认为5。
    '''
    func(1,2)