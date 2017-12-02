#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/1
#

class AnElephantNamedJoseph:
    def __init__(self, noOfElfs):
        self.noOfElfs = noOfElfs
        self.count = 0
        
    def getElfNo(self):
        
        a = []
        for n in range(1, self.noOfElfs, 2):
            a.append(n)
        if  self.noOfElfs % 2:
            a.pop(0)
        while a.__len__() > 1:
            a.pop(1)
            n = a.pop(0)
            a.append(n)
            
            
        return a[0]

    def getElfNoAlt(self):
        b = str(bin(self.noOfElfs))
        b = b[3:]
        
        return int(b, 2) * 2 +1
    
def main():
    print('Start AnElephantNamedJoseph')
    
#     c = AnElephantNamedJoseph(22)
#     c = AnElephantNamedJoseph(300000)
    c = AnElephantNamedJoseph(3005290)
#     print 'Elf No:', c.getElfNo()
    print 'Elf No:', c.getElfNoAlt()
 

if __name__ == '__main__':
    main()