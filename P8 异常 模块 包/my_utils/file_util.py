# 文件相关的工具

def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, 'r', encoding = 'utf-8')
    except Exception as e:
        print(e)
    else:
        print(f.read())
    finally:
        if f: # 若f == None，相当于False，不会执行if块；若f是其他内容，相当于True
            f.close()
        print('文件信息查询功能结束')

def append_to_file(file_name, data):
    f = open(file_name, 'a', encoding = 'utf-8')
    f.write('\n' + data)
    f.close()

if __name__ == '__main__':
    print_file_info('../Test.txt')