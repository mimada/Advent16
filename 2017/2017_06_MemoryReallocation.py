#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2017/day/6
#

import time

class MemoryReallocation:
#     def __init__(self):
#         pass
    def arrayToString(self, arr):
        s = ""
        for a in arr:
            s = s + '{:02d} '.format(a)
        return s
    
    def getCycles(self, inp = []):
        cycles = 0
        cycles1 = 0
        stay = True
        history = []
        history.append(self.arrayToString(inp))
        history1 = ''
        
        while(stay):
            pos = 0
            val = 0
            for i, v in enumerate(inp):
                if v > val:
                    pos = i
                    val = v
            inp[pos] = 0
            
            for i in range(val):
                pos = pos + 1
                if pos >= len(inp):
                    pos = 0
                inp[pos] = inp[pos] + 1
            
            cycles = cycles + 1
            
            if history1 == self.arrayToString(inp):
                stay = False
            
            if history.count(self.arrayToString(inp)) > 0 and history1 == '':
                history1 = self.arrayToString(inp)
                cycles1 = cycles
                cycles = 0 
                
            history.append(self.arrayToString(inp))
        
        return cycles1, cycles
    
def main():
    start_time = time.time()
    print('Start Memory Reallocation')
    
    input1 = [0, 2, 7, 0]
    input2 = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6]
    
    ic = MemoryReallocation()
    
    print 'Memory Reallocation a: cycles = {0}'.format(ic.getCycles(input1))
    print 'Memory Reallocation b: cycles = {0}'.format(ic.getCycles(input2))
    
    print("--- %s seconds ---" % (time.time() - start_time))
if __name__ == '__main__':
    main()