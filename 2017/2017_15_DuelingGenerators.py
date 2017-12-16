#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2017/day/6
#

import time

class DuelingGenerators:
    
    def generatorA(self, rounds, startValue, mod):
        cnt = 0
        reminder = startValue
        while cnt < rounds:
            reminder = reminder * 16807 % 2147483647
            if (reminder % mod) == 0:
                cnt = cnt + 1
                yield reminder
    
    def generatorB(self, rounds, startValue, mod):
        cnt = 0
        reminder = startValue
        while cnt < rounds:
            reminder = reminder * 48271 % 2147483647
            if (reminder % mod) == 0:
                cnt = cnt + 1
                yield reminder
    
    def getTest1Result(self, rounds, a, b, modA, modB):
        if rounds > 1000000:
            r = 1000000
        else:
            r = rounds
            
        matchingValues = 0
        for i in range(0, rounds, r):
            for a, b in zip(self.generatorA(r, a, modA), self.generatorB(r, b, modB)):
                if (a & 0xffff) == (b & 0xffff):
                    matchingValues = matchingValues + 1
            print i, matchingValues
        
        return matchingValues

def main():
    start_time = time.time()
    print('Start Dueling Generators')
    
    c = DuelingGenerators()
#     print c.getTest1Result(5, 65, 8921, 1, 1)
#     print c.getTest1Result(40000000, 65, 8921, 1, 1)
#     print c.getTest1Result(40000000, 873, 583, 1, 1)
#     print c.getTest1Result(5, 65, 8921, 4, 8)
#     print c.getTest1Result(5000000, 65, 8921, 4, 8)
    print c.getTest1Result(5000000, 873, 583, 4, 8)
    
    
    print("--- %s seconds ---" % (time.time() - start_time))
if __name__ == '__main__':
    main()