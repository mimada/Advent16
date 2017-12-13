#
# Mikael Martensson
# http://adventofcode.com/2017/day/4
#

class DigitalPlumber:
    def __init__(self):
        self.pipes = {}
        self.programCnt = 0
         
    
    def parseFile(self, fileName):
        
        with open(fileName) as fi:
            for line in fi:
                s0 = line.split(' <-> ')
                p = s0[0]
                s1 = map (lambda x:x.strip(), s0[1].split(','))
                
                self.pipes[p] = s1
                
        print self.pipes
    
    def getPipesInGroup(self, pipesInGroup, pipe):
        
        pipesInGroup.append(pipe)
        
        for child in self.pipes[pipe]:
            if not child in pipesInGroup:
                pipesInGroup = self.getPipesInGroup(pipesInGroup, child)
        
        return pipesInGroup
    
    def getGroups(self):
        
        pipesInGroup = []
        pipes = self.pipes.keys()
        pipes.sort()
        groups = []
        for pipe in pipes:
            if not pipe in pipesInGroup:
                groups.append(pipe)
                self.getPipesInGroup(pipesInGroup, pipe)
            
        return groups
    
def main():
    print('Start Digital Plumber')
    
    c = DigitalPlumber()
#     c.parseFile('2017_12_Input_test_1.txt')
    c.parseFile('2017_12_Input.txt')
    pipesInGroup = []
    print len(c.getPipesInGroup(pipesInGroup, '0'))
    print len(c.getGroups())
    
    
if __name__ == '__main__':
    main()