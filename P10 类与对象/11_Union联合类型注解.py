# 使用Union，需要先导包
from typing import Union

# 列表中的元素既有整数，又有字符串
my_list: list[Union[int, str]] = [1, 2, 'Hello', 'World']
print(my_list)

def func(data: Union[int, str]) -> Union[int, str]:
    return data

func(1) # 鼠标光标放在括号内，按下[ctrl] + [p]，pycharm弹出提示
_str: str = func("Hello")
print(_str)