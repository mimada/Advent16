#
# Mikael Martensson
# http://adventofcode.com/2017/day/4
#

class RecursiveCircus:
    def __init__(self):
        self.modules = {}
        self.parentModules = []
        self.childModules = []
    
    def parseFile(self, fileName):
        
        with open(fileName) as fi:
            for line in fi:
                if len(line) < 2:
                    continue
                s0 = line.split(' -> ')
                s1 = s0[0].split()
                
                self.modules[s1[0]] = {}
                self.modules[s1[0]]['weight'] = int(s1[1].strip('()'))
                if len(s0) > 1:
                    self.parentModules.append(s1[0])
#                     s2 = s0[1].split(',')
                    s2 = map (lambda x:x.strip(), s0[1].split(','))
                    self.childModules.extend(s2)
                    self.modules[s1[0]]['childs'] = s2
#                     for v in s2:
#                         self.modules[s1[0]][v.strip()] = {}
#                         self.childModules.append(v.strip())
    
    def getRoot(self):
        
        print 'modules:', self.modules
        print 'parentModules:', self.parentModules
        print 'childModules:', self.childModules
        
        keys = self.modules.keys()
        for k in keys:
            if self.childModules.count(k) == 0:
                return k
    
    def checkWheight(self, root = {}):
        if not root.has_key('childs'):
            return root['weight']
        
        weight = 0
        weights = []
        tot = 0
        for child in root['childs']:
            weight = self.checkWheight(self.modules[child])
            weights.append(weight)
            tot = tot + weight
            
        if weight != (tot / len(root['childs'])):
            for i, v in enumerate(root['childs']):
                print self.modules[v]['weight'], 
            print weights
        
        return tot + root['weight']
    
    
def main():
    print('Start Recursive Circus')
    
    c = RecursiveCircus()
#     c.parseFile('2017_07_Input_test_1.txt')
    c.parseFile('2017_07_Input.txt')
    root = c.getRoot()
    print root
    c.checkWheight(c.modules[root])
#     print c.getNumberOfHops1('2017_07_Input_test_1.txt')
#     print c.getNumberOfHops1('2017_07_Input.txt')
    
if __name__ == '__main__':
    main()