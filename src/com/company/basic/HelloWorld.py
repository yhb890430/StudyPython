import keyword;# import关键字用于引用类

# print用于输出，默认换行，如果要实现不换行需要在变量末尾加上 end=""
print(100 + 200);
# 单引号包含双引号，此时双引号属于字符串内容的一部分，同理双引号包含单引号也是一样的
print('你好，"大家好"！');
print(100, end=" ");
print(200, end=" ");
# 标识符命名规则
# 第一个字符必须是字母表中字母或下划线'_'。
# 标识符的其他的部分有字母、数字和下划线组成。
# 标识符对大小写敏感。
A1 = '';
_name = "jack";
age = 25;
_name = 'tom';
print(_name);

# keyword表示Python的保留关键字，不可用于标识符
print(keyword.kwlist);

# 单行注释

# 行与缩进
if True:
    print("true");
else:
    print("false");

# 多行语句
a = 100;b=100;c=100; # 同一行显示多条语句，语句之间使用分号(;)分割
total = a + \
        b +\
        c;
print(total);
# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five'];
print(total);

# input()函数用于与用户在控制台进行交互
name = input("请输入你的姓名：");
print("My Name is",name);

# 缩进相同的一组语句构成一个代码块，我们称之代码组。


# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数或者成员变量,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数或者成员变量,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *

# import sys
# print('================Python import mode==========================');
# print ('命令行参数为:')
# for i in sys.argv:
#     print (i)
# print ('\n python 路径为',sys.path)

from sys import argv, path  # 导入特定的成员

print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path