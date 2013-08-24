import timeit
import random

time_get = timeit.Timer("'x[%d]' % random.randrange(len(x))", 'from __main__ import random, x')
time_set = timeit.Timer("'x[%d]=%d' % (random.randrange(len(x)), random.randrange(len(x)))", \
                        "from __main__ import random, x")

for i in range(100000, 1000001, 100000):
    x = list(range(i))
    print '%d => L_G: %f & L_S: %f ' % (i, time_get.timeit(1000), time_set.timeit(1000))
    x = {j:None for j in range(i)}
    print '%d => D_G: %f & D_S: %f ' % (i, time_get.timeit(1000), time_set.timeit(1000))
