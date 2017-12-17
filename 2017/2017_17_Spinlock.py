#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2017/day/6
#

import time

class Spinlock:
    
    def getTest1Result(self, steps, times):
        array = []
        array.append(0)
        pos = 0
        
        for t in range(1, times):
            pos = 1 + (pos + steps) % len(array)
            array.insert(pos, t)
            
        print array
        return array[pos + 1]
    
def main():
    start_time = time.time()
    print('Start Spinlock')
    
    c1 = Spinlock()
#     print c1.getTest1Result(3, 2018)
#     print c1.getTest1Result(316, 2018)

    print c1.getTest1Result(316, 50000000)
    
    
    print("--- %s seconds ---" % (time.time() - start_time))
if __name__ == '__main__':
    main()