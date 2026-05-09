"""
while 条件:
    条件满足时执行的事
    ...(条件控制)
"""

# 只要条件满足，循环一直持续

i = 0
while i < 10:
    print(f'第{i + 1}次学python')
    i += 1 # python有i++么？好像没有。

print("Loop over!")

sum = 0
num = 1
while num <= 100:
    sum += num
    num += 1
print(f'1 ~ 100的累加和为{sum}')