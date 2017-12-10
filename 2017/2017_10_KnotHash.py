#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2017/day/6
#

import time

class KnotHash:
    
    def getTest1Result(self, nArray, inputData):
        sparseHash = self.getScrambledArray(nArray, 1, inputData)
        print sparseHash
        return sparseHash[0] * sparseHash[1]
        
    
    def getTest2Result(self, nArray, inputData):
        array = []
        for c in inputData:
            array.append(ord(c))
        array.extend([17, 31, 73, 47, 23])
        print array
        
        sparseHash = self.getScrambledArray(nArray, 64, array)
        print sparseHash
        
        denseHash = []
        denseHashValue = 0
        for n in range(len(sparseHash)):
            if not n % 16 and n > 0:
                denseHash.append(denseHashValue)
                denseHashValue = 0
            denseHashValue = denseHashValue ^ sparseHash[n]
        denseHash.append(denseHashValue)
        
        hexHash = ''
        for v in denseHash:
            hexHash = hexHash + '{:02X}'.format(v)
        
        return hexHash.lower()
        
    
    def getScrambledArray(self, nArray, rounds, inputData):
        currentPos = 0
        skipSize = 0
        
        array = []
        for n in range(nArray):
            array.append(n)
        
        for n in range(rounds):
            for length in inputData:
                if (currentPos + length) > (nArray - 1):
                    overLap = (currentPos + length) % nArray
                    cut = array[currentPos : nArray] + array[0 : overLap]
                    cut.reverse()
                    array[currentPos : nArray] = cut[0 : nArray - currentPos]
                    array[0 : overLap] = cut[nArray - currentPos:]
                else:
                    array[currentPos : currentPos + length] = reversed(array[currentPos : currentPos + length])
                
                currentPos = (currentPos + length + skipSize) % nArray
                skipSize = skipSize + 1
            
        print currentPos, array
        return array
    

def main():
    start_time = time.time()
    print('Start Knot Hash')
    
    input1 = [3, 4, 1, 5]
    input2 = [187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216]
    
    c = KnotHash()
    print c.getTest1Result(5, input1)
    print c.getTest1Result(256, input2)
    
    print c.getTest2Result(256, '')
    print 'a2582a3a0e66e6e86e3812dcb672a272'
    print c.getTest2Result(256, 'AoC 2017')
    print '33efeb34ea91902bb2f59c9920caa6cd'
    print c.getTest2Result(256, '1,2,3')
    print '3efbe78a8d82f29979031a4aa0b16a9d'
    print c.getTest2Result(256, '1,2,4')
    print '63960835bcdc130f0b66d7ff4f6a5a8e'
    print c.getTest2Result(256, '187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216')
    
#     print 'Memory Reallocation a: cycles = {0}'.format(ic.getCycles(input1))
#     print 'Memory Reallocation b: cycles = {0}'.format(ic.getCycles(input2))
    
    print("--- %s seconds ---" % (time.time() - start_time))
if __name__ == '__main__':
    main()