#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@note: python数据类型
@author: yuanhaibo
@contact: yuanhaibo@dnion.com
@time: 2017/7/28 11:07
'''

# 变量
# 变量名必须是大小写英文、数字和_的组合，且不能用数字开头
# 整型
a = b = 12;
c,d = 10,'你好';
print(a);
print(b);
print(c);
print(d);
a= 0x97;# 十六进制数
print(a);# 打印时自动转为十进制

# 浮点数
a = 3.121314
print(a);

#字符串 用''或者""表示字符串
e,f = 'hello',"world!";
print(e,f);# print 多字符串会自动加空格

# 布尔类型
res = True;
print(res);
res = not False;
print(res);

# 空值
res = None;
print(res);

# python变量引用思考
a = 'ABC'
b = a
a = 'XYZ'
print(b)
print(a == b);

a = 1;
b = a;
a = 2;
print(a);
print(b);
print(a == b);

# 常量
PI = 3.1415926;
