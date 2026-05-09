def func_a():
    print('\t\ta\t\t')

def func_b():
    print('\tb1\t')
    func_a() # 嵌套调用：定义b函数时调用a函数
    print('\tb2\t')

func_b()