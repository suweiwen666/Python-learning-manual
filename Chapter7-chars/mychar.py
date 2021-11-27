# -*- coding: UTF-8 -*-

'''
1.字符串find方法能用于搜索列表吗？
---不行，因为方法是类型特定的，只能用于单一数据类型上。
像X+Y这样的表达式和len（X）这样的内置函数是通用的，可以用于多种类型上。
在这个例子中，in关系表达式和字符串查找具有类似的效果，但它可以用来查找字符串和列表。
在Python 3.0中，有一些对方法分组的尝试（例如，不可变序列类型list和bytearray具有类似的方法集合），但方法仍然比其他的操作集更特定于类型。

2.字符串切片表达式能用于列表吗？
---可以。和方法不同的是，表达式是通用的，可用于多种类型。
就这一点来说，切片表达式其实是序列运算，可用于任何类型的序列对象上，包括字符串、列表以及元组。
唯一的差别就是当你对列表进行切片时，你得到的是新列表。

3.你如何将字符转成其ASCII码？你如何反向转换，从整数转换成字符？
---内置的ord（S）函数可将单个字符的字符串转换成整数字符编码。chr（I）则是从整数代码转换回字符串。

4.在Python中，怎么修改字符串？
---字符串无法被修改，字符串是不可变的。
尽管这样，你可以通过合并、切片运算、执行格式化表达式、方法调用（例如，replace）创建新的字符串，再将结果赋值给最初的变量名，从而达到相似的效果。

5.已知字符串S的值为"s,pa,m"，提出两种从中间抽取两个字符的方式。
---你可以使用S[2:4]对字符串进行切片，或者使用S.split（','）[1]以逗号分隔字符串，再进行索引运算。通过交互模式亲自实验，看一下结果。

6.字符串"ab\x1f\000d"之中有多少字符？
---6个。字符串"ab\x1f\000d"包含一些字节a、新行（）、b、二进制值31（十六进制转义\x1f）、二进制值0（八进制转义\000）以及d。
把字符串传给内置的len函数可以验证它，然后印出每个字符的ord结果，从而查看实际的字节值。参见表7-2的细节。

7.你为什么要使用string模块，而不使用字符串方法调用？
---如今不应该使用string模块，而应该使用字符串对象方法调用。string模块已经弃用，Python 3.0完全删除其调用。
使用string模块的唯一原因就是可以使用其他工具，例如，预定义的常数。现在，在非常陈旧的Python代码中，它才会出现。
'''

if __name__ == '__main__':
    print("spam's") #单引号和双引号相同
    print('s\np\ta\x00m') #转义序列
    print("""...""") #三重引号字符串块
    print(r"\temp\spam") #Raw字符串
    print(b'spam') #字节字符串
    print(u'spam') #unicode字符串

    print('shghjsbak'+'shghjsbak') #拼接
    print('haliluya'*3) #重复
    print('haliluuya'[3]) #索引
    print('haliluya'[4:8]) #分片 步长默认为1
    print('haliluya'[4:8:2])  #分片 步长为2；
    print('haliluya'[8:4:-1])  # 分片 步长为2；负数的步长表示从后往前找
    print(len('haliluya')) #长度

    kind = 'very'
    print("a %s parrot" %kind) #字符串格式化表达式
    print("a {} parrot".format(kind)) #字符串格式化方法
    print(kind.find('ry')) #搜索
    print(kind.strip()) #移除空格
    print(kind.replace('y','ies'))#替换
    print(kind.split(','))#分割
    print(kind.isdigit())#内容测试
    print(kind.upper())#短信息转换
    print(kind.endswith('y'))#结束测试
    print(kind.join('1234'))#插入分隔符
    print(kind.encode('latin-1'))#Unicode编码

    print(str('spam'),repr('spam'))
    print(ord('s')) #转ASCII码
    print(chr(115)) #逆ASCII码

    pass