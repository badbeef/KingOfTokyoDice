from random import *
import time

'''
King of Tokyo dice rolling simulator
combination : The combination you want with case insensitive string from
              '1', '2', '3' are the numbers on dice,
              'H' is Heart,
              'P' is Power,
              'A' is Attack
              Use '*' to mean don't care
              e.g. '111***'
              The number of characters represents the number of dices you use

rolls       : the number of rolls allowed, default 3
repeats     : number of times to repeat, default 1 million times
'''
def KoT(combination, rolls = 3, repeats = 1000000):
    starttime = time.time()
    allfaces = '123HPA'
    faces = len(allfaces)
    success = 0
    TARGET = list(combination.upper())
    for i in range(repeats):
        target = TARGET.copy()
        for j in range(rolls):
            myroll = [allfaces[randint(0, faces - 1)] for _ in range(len(target))]
            for d in myroll:
                if d in target:
                    target.remove(d)
        success += 1
        for d in target:
            if d != '*':
                success -= 1
                break
    prob = float(success) / repeats
    print('Time Taken: %.2fs ' % (time.time() - starttime))
    return f"{prob:.3%}"
