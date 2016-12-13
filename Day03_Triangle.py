#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/1
#

class Triangles:
    def __init__(self, linesIn = []):
        self.lines = linesIn
        self.count = 0
        self.splitWidth = 5
        self.lengths = []
        
    def convertLineH(self):
        del self.lengths[:]
            
        for line in self.lines:
            lengths = [] 
            lengths.append(int(line[0:5].strip()))
            lengths.append(int(line[5:10].strip()))
            lengths.append(int(line[10:15].strip()))
            lengths.sort()
            self.lengths.append(lengths)
        
    def convertLineV(self):
        del self.lengths[:]
        i = 0
        lengths1 = [] 
        lengths2 = [] 
        lengths3 = []
            
        for line in self.lines:
            i = i + 1
            lengths1.append(int(line[0:5].strip()))
            lengths2.append(int(line[5:10].strip()))
            lengths3.append(int(line[10:15].strip()))
            
            if i == 3:
                lengths1.sort()
                self.lengths.append(lengths1)
                lengths2.sort()
                self.lengths.append(lengths2)
                lengths3.sort()
                self.lengths.append(lengths3)
                i = 0
                lengths1 = [] 
                lengths2 = [] 
                lengths3 = []
        
    def countTriangles(self):
        count = 0
        for lengths in self.lengths:
            if lengths[0] + lengths[1] > lengths[2]:
                count = count + 1
        return count
    
def main():
    print('Start Triangles')
    
    lines = []
    with open('Day3_input1.txt') as f: 
        lines = [line.rstrip('\n') for line in f]

    c = Triangles(lines)
    c.convertLineH()
    print 'Number of correct triangles horizontal: {0}'.format(c.countTriangles())
    c.convertLineV()
    print 'Number of correct triangles vertical: {0}'.format(c.countTriangles())
 

if __name__ == '__main__':
    main()