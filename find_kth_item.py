import random
import timeit

def find_kth_item(numbers, k):
    num_d = dict()
    for i in range(len(numbers)):
       num_d[numbers[i]] = num_d.setdefault(numbers[i], 0) + 1
    accum = 0
    for j in range(max(list(num_d.keys()))):
        accum += num_d.get(j, 0)
        if accum > k: return j

if __name__ == "__main__":
    for l in range(100, 1001, 100):
        numbers = [random.randint(0,j) for j in range(l)]
        k = random.randrange(0, l)
        print "%dth item in %d length list: %f milliseconds" % (k, l, timeit.timeit("find_kth_item(numbers, k)", \
                                                                                    setup="from __main__ import find_kth_item, numbers, l, k"))
    
        
        
        
