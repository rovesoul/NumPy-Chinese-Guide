#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import random
import time
import numpy as np
np.random.seed(1234567890)

a=[]
t0=time.time()
for i in range(100000000):
    a.append(random.random())
t1=time.time()

c=np.random.rand(1,100000000)

t2=time.time()

sum1=sum(a)
t3=time.time()

b=np.array(a)
t4=time.time()
sum3=np.sum(b)
t5=time.time()

print('py前十',a[:10],b.size,'\nnp前十',c[:10],c.size)
print('\n生成列表py法',t1-t0,
      '\n生成列表np法',t2-t1,
      '\n自动求和py法',t3-t2,
      '\n自动求和np法',t5-t4)