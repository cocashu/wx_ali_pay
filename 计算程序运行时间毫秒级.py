import time

ss=int(round(time.time() * 1000))    #毫秒级时间戳
#print(ss)
#需要计时的过程代码
for num in range(10,5000):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
       #  print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print ('%d 是一个质数' % num)
en=int(round(time.time() * 1000))    #毫秒级时间戳
#print(en)

print('过程耗时：', en - ss, '毫秒')
