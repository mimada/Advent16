#
# Mikael Martensson
# http://adventofcode.com/2017/day/4
#

class AMazeOfTwistyTrampolinesAllAlike:
    
    def getNumberOfHops1(self, fileName):
        na = []
        with open(fileName) as fi:
            for line in fi:
                na.append(int(line)) 
        
        escape = False
        jumpCnt = 0
        pos = 0
        while not escape:
            posBefore = na[pos]
            na[pos] = na[pos] + 1
            pos = pos + posBefore
            jumpCnt = jumpCnt + 1
        
            if pos >= len(na):
                escape = True
        
        return jumpCnt
    
    def getNumberOfHops2(self, fileName):
        na = []
        with open(fileName) as fi:
            for line in fi:
                na.append(int(line)) 
        
        escape = False
        jumpCnt = 0
        pos = 0
        while not escape:
            posBefore = na[pos]
            
            if posBefore >= 3:
                na[pos] = na[pos] - 1
            else:
                na[pos] = na[pos] + 1
            pos = pos + posBefore
            jumpCnt = jumpCnt + 1
        
            if pos >= len(na):
                escape = True
        
        return jumpCnt
    
def main():
    print('Start A Maze of Twisty Trampolines, All Alike')
    
    c = AMazeOfTwistyTrampolinesAllAlike()
    
    print c.getNumberOfHops1('2017_05_Input_test_1.txt')
    print c.getNumberOfHops1('2017_05_Input.txt')
    
    print c.getNumberOfHops2('2017_05_Input_test_1.txt')
    print c.getNumberOfHops2('2017_05_Input.txt')

if __name__ == '__main__':
    main()