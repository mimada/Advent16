#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/1
#

class FirewallRules:
    def __init__(self, blackList):
        self.blackList = []
        for line in blackList:
            l = line.split('-')
            ll = (int(l[0]), int(l[1]))
            self.blackList.append(ll)
            
        self.blackList.sort()
        self.whileList = []
        
    def sortBlacklist(self):
        c = True
        n = 0
        
        
    def getWhileList(self):
        ip = []
        ipMin = 0
        ipMax = 0
        for l in self.blackList:
            
            if ipMin == 0 and ipMax == 0:
                ipMin = l[0]
                ipMax = l[1]
                continue
                
            if l[0] == ipMax + 1:
                ipMax = l[1]
                continue
            
            if l[0] >= ipMin and l[1] <= ipMax:
                continue
                
            
            if l[0] < ipMax and l[1] > ipMax:
                ipMax = l[1]
                continue

            if l[0] > ipMax + 1:
                for n in range(ipMax+1, l[0]):
                    self.whileList.append(n)
                    ipMax = l[1]
                    
        
        return self.whileList.__len__(), self.whileList
    
def main():
    print('Start FirewallRules')
    
    blackList = []
#     with open('Day10_commands_test.txt') as f: 
    with open('Day20_input.txt') as f: 
        blackList = [line.rstrip('\n') for line in f]

    c = FirewallRules(blackList)
    print 'White list:', c.getWhileList()
 

if __name__ == '__main__':
    main()