money = 5000000
# name = None
name = input('欢迎来到Python银行，请输入你的名字：')

def query(BOOL):
    if BOOL == True:
        print("------------😊\t查询余额\t😊------------")
    print(f'{name}的银行账户还有{money}￥💕')

def saving(num):
    global money
    money += num
    query(False)

def extract(num):
    global money
    if num <= money:
        money -= num
    else:
        print('您的余额为不够取这么多钱！😥')
    query(False)

def mainTable():
    print(f'{name}你好，欢迎来到Python银行。请选择操作：')
    print('查询余额\t【输入1】')
    print('存款\t\t【输入2】')
    print('取款\t\t【输入3】')
    print('退出\t\t【输入4】')
    return int(input('请输入你的选择：'))

while True:
    choice = mainTable()
    if choice == 1:
        query(True)
        continue
    elif choice == 2:
        saving(int(input('请输入存款数额：')))
        continue
    elif choice == 3:
        extract(int(input('请输入取款数额：')))
        continue
    else:
        print('程序即将退出...')
        break
print('程序已退出.')