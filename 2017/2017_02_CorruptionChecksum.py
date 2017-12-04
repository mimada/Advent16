#
# Mikael Martensson
# http://adventofcode.com/2017/day/2
#

class CorruptionChecksum:
    
    def getChecksum1(self, fileName):
        s1 = 0
        
        with open(fileName) as fi:
            for line in fi:
                vl = map (lambda x:int(x), line.split())
                vl.sort(reverse = True)
                s1 = s1 + (vl[0] - vl[len(vl)-1])
                    
        return s1
    
    def getChecksum2(self, fileName):
        s1 = 0
        
        with open(fileName) as fi:
            for line in fi:
                vl = map (lambda x:int(x), line.split())
                vl.sort(reverse = True)
                
                for i1, a in enumerate(vl):
                    for i2, b in enumerate(vl):
                        if (i1 != i2) and (not a % b):
                            s1 = s1 + (a / b)
                    
        return s1
    
def main():
    print('Start Corruption Checksum')
    
    c = CorruptionChecksum()
    
    print c.getChecksum1('2017_02_Input_test_1.txt')
    print c.getChecksum1('2017_02_Input.txt')
    
    print c.getChecksum2('2017_02_Input_test_2.txt')
    print c.getChecksum2('2017_02_Input.txt')

if __name__ == '__main__':
    main()