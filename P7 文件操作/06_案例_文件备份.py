f1 = open('D:\\Develop\\LearnPython\\File\\bill.txt', 'r', encoding = 'utf-8')
f2 = open('D:\\Develop\\LearnPython\\File\\bill.txt.bak', 'w', encoding = 'utf-8')

for line in f1:
    temp = line.strip() # 去掉前后空格&换行
    if temp.split(',')[4] == '测试':
        continue
    else:
        f2.write(line)

f1.close()
f2.close()