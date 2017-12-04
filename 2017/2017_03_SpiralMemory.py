#
# Mikael Martensson
# http://adventofcode.com/2017/day/3
#

class SpiralMemory:
#     def __init__(self):
#         pass
    
    def getSteps1(self, data):
        counter = 1
        sideLength = 1
        sideStep = 0
        steps = 0
        
        while counter < data:
            steps = steps + 1
            sideLength = (steps * 2 + 1)
            counter = sideLength ** 2
        
        print steps, counter, sideLength
        
        if sideLength > 1:
            sideStep = ((counter - data) % (sideLength - 1)) - (sideLength - 1)/2
        
        
        return steps + abs(sideStep)
    
    def getValue(self):
        a = []
        a.append(1)
        a.append(a[0])
        
        a.append(a[0]+a[1])
        a.append(a[0]+a[1]+a[2])
        
        a.append(a[0]+a[3])             # 4
        a.append(a[0]+a[3]+a[4])
        
        a.append(a[0]+a[5])             # 6
        a.append(a[0]+a[1]+a[5]+a[6])
        a.append(a[0]+a[1]+a[7])
        
        a.append(a[1]+a[8])             # 9
        a.append(a[1]+a[2]+a[8]+a[9])
        a.append(a[1]+a[2]+a[10])
        
        a.append(a[2]+a[11])             # 12
        a.append(a[2]+a[3]+a[11]+a[12])
        a.append(a[2]+a[3]+a[4]+a[13])
        a.append(a[3]+a[4]+a[14])
        
        a.append(a[4]+a[15])             # 16
        a.append(a[4]+a[5]+a[15]+a[16])
        a.append(a[4]+a[5]+a[6]+a[17])
        a.append(a[5]+a[6]+a[18])
        
        a.append(a[6]+a[19])             # 20
        a.append(a[6]+a[7]+a[19]+a[20])
        a.append(a[6]+a[7]+a[8]+a[21])
        a.append(a[7]+a[8]+a[9]+a[22])
        a.append(a[8]+a[9]+a[23])
        
        print a
        
    
def main():
    print('Start Inverse Captcha')
    
#     dataArray = [1, 12, 23, 1024]
    dataArray = [1, 12, 23, 1024, 289326]
    
    ic = SpiralMemory()
    
    for inp in dataArray:
        print 'Spiral Memory a: {0} givs {1} steps'.format(inp, ic.getSteps1(inp))
    
    ic.getValue()
    

if __name__ == '__main__':
    main()