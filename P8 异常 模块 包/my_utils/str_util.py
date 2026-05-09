# 字符串相关的工具

def str_reverse(s):
    """
    接受传入字符串，将字符串反转返回
    :param s: 输入的字符串
    :return: 反转后的字符串
    """
    return s[: : -1]

def substr(s, x, y) -> list[str]: # 对返回值的类型注解
    """
    按照下标x和y，对字符串进行切片
    :param s: 输入的字符串
    :param x: 切片的开始下标
    :param y: 切片的结束下标
    :return: 一个切片后的列表（包含三个字符串）
    """
    s1 = s[: x]
    s2 = s[x: y]
    s3 = s[y: ]
    return [s1, s2, s3]

if __name__ == '__main__':
    print(str_reverse('hello'))
    print(substr('hello world', 3, 7))