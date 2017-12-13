#
# Mikael Martensson
# http://adventofcode.com/2017/day/4
#

class PacketScanners:
    def __init__(self):
        self.layers = []
         
    
    def parseFile(self, fileName):
        
        with open(fileName) as fi:
            index = 0
            for line in fi:
                s0 = map (lambda x:int(x), line.split(': '))
                
                layerRange = {}
                layerRange['range'] = s0[1]
                layerRange['scanPos'] = 0
                layerRange['sign'] = 1
                
                if index == s0[0]:
                    self.layers.append(layerRange)
                else:
                    for i in range(s0[0] - index):
                        layerRange1 = {}
                        self.layers.append(layerRange1)
                        index = index + 1
                    self.layers.append(layerRange)
                index = index + 1
        print self.layers
    
    def resetScanner(self):
        for l1 in self.layers:
            if l1.has_key('scanPos'):
                l1['scanPos'] = 0
                l1['sign'] = 1
        
    def runScanner(self, steps):
        for i in range(steps):
            for l1 in self.layers:
                if l1.has_key('scanPos'):
                    if l1['scanPos'] == 0:
                        l1['sign'] = 1
                    elif l1['scanPos'] == (l1['range'] - 1):
                        l1['sign'] = -1
                        
                    l1['scanPos'] = (l1['scanPos'] + l1['sign'])
    
    def getTest1Result(self):
        severity = 0
        for i, l in enumerate(self.layers):
            if l.has_key('scanPos'):
                if l['scanPos'] == 0:
                    severity = severity + i * l['range']
            self.runScanner(1)
        return severity
    
    def getTest2Result(self):
        hit = 1
        steps = 30000
        while hit > 0:
            steps = steps + 2
            self.resetScanner()
            self.runScanner(steps)
            hit = 0
            for i, l in enumerate(self.layers):
                if l.has_key('scanPos'):
                    if l['scanPos'] == 0:
                        hit = hit + 1
                self.runScanner(1)
            if not (steps % 1000):
                print steps, hit
        return steps
    
def main():
    print('Start Packet Scanners')
    
    c = PacketScanners()
#     c.parseFile('2017_13_Input_test_1.txt')
    c.parseFile('2017_13_Input.txt')
    print c.getTest1Result()
    print c.getTest2Result()
    
    
if __name__ == '__main__':
    main()