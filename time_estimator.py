
def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))


if __name__ == "__main__":
    import timeit

    t1 = timeit.Timer("test1()", "from __main__ import test1")
    print "concat: %f milliseconds" % t1.timeit(1000)

    t2 = timeit.Timer("test2()", "from __main__ import test2")
    print "append: %f millisconds" % t2.timeit(number=1000)

    t3 = timeit.Timer("test3()", "from __main__ import test3")
    print "comprehesion: %f milliseconds" % t3.timeit(number=1000)

    t4 = timeit.Timer("test4()", "from __main__ import test4")
    print "list range: %f milliseconds" % t4.timeit(number=1000)

    pop_zero = timeit.Timer("x.pop(0)", "from __main__ import x")
    pop_end = timeit.Timer("x.pop()", "from __main__ import x")
    
    for i in range(1000000, 100000001, 1000000):
        x = list(range(i))
        pz = pop_zero.timeit(1000)
        x = list(range(i))
        pe = pop_end.timeit(1000)
        print "pop_zero: %f \n pop_end: %f" % (pz, pe)

    t6 = timeit.Timer("x.pop()", "x=range(2000000)")
    print "pop_end: %f " % t6.timeit(1000)


