#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/1
#

class DragonChk:
    def __init__(self, start ,diskSz):
        self.start = start
        self.diskSz = diskSz
        
    def generate(self):
        sz = self.start.__len__()
        while sz < self.diskSz:
            b = ''
            n = self.start.__len__()
            while n:
                n = n - 1
                if self.start[n] == '1':
                    b = b +'0'
                else:
                    b = b + '1'
            
            self.start = self.start + '0' + b
            sz = self.start.__len__()
        
        self.start = self.start[:self.diskSz]
        s = self.start
        while s.__len__() % 2 == 0:
            chk = ''
            for n in range(0, s.__len__(), 2):
                chk = chk + str(bin(~(int(s[n], 2) ^ int(s[n+1], 2))))[-1:]
            s = chk
            
        return chk
    
def main():
    print('Start DragonChk')
    
#     c = DragonChk('10000', 20)
#     c = DragonChk   ('10010000000110000', 272)
    c = DragonChk   ('10010000000110000', 35651584)
    print 'Checksum:', c.generate()
 

if __name__ == '__main__':
    main()