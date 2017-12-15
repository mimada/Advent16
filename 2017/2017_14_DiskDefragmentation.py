#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2017/day/6
#

import time

class DiskDefragmentation:
    
    def getHash(self, nArray, inputData):
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
    
    def getTest1Result(self, nArray, inputData):
        usedSquares = 0
        for i in range(128):
            data = self.getHash(nArray, '{0}-{1}'.format(inputData, i))
            data = "{0:0128b}".format(int(data, 16))
            for c in data:
                if c == '1':
                    usedSquares = usedSquares + 1
            print data
        return usedSquares

def main():
    start_time = time.time()
    print('Start Disk Defragmentation')
    
    c = DiskDefragmentation()
    print c.getTest1Result(256, 'flqrgnkx')
    print c.getTest1Result(256, 'ljoxqyyw')
    
    
    print("--- %s seconds ---" % (time.time() - start_time))
if __name__ == '__main__':
    main()