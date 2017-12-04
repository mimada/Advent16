#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/1
#
import md5

class OneTimePad:
    def __init__(self, salt, stretched = False):
        self.salt = salt
        self.stretched = stretched
        self.codes = []
        self.okCodes = []
        
    def getHash(self):
        self.counter = 0
        
        while self.okCodes.__len__() < 64:
            
            m = md5.new('{0}{1}'.format(self.salt, self.counter))
            hashStr = m.hexdigest()
            
            if self.stretched:
                c = 2016
                while c:
                    m = md5.new(hashStr)
                    hashStr = m.hexdigest()
                    c = c - 1
                
            for n in range(hashStr.__len__() - 2):
                if hashStr[n] == hashStr[n+1] and hashStr[n+1] == hashStr[n+2]:
                    a = {}
                    a['key'] = hashStr[n : n+3]
                    a['n'] = self.counter
                    a['hash'] = hashStr
                    self.codes.append(a)
#                     print a
                    break
                
            for n in range(hashStr.__len__() - 4):
                if hashStr[n] == hashStr[n+1] and hashStr[n+1] == hashStr[n+2] and hashStr[n+2] == hashStr[n+3] and hashStr[n+3] == hashStr[n+4]:
                    key = hashStr[n : n+3]
                    
                    for k in self.codes[:]:
                        if k['n'] < self.counter - 1000:
                            self.codes.remove(k)
                            continue
                        if k['key'] == key and k['n'] != self.counter:
                            b = self.codes.pop(self.codes.index(k))
                            self.okCodes.append(b)
                            print b
                        if self.okCodes.__len__() == 64:
                            break
            
            self.counter = self.counter + 1
    
    def getCount(self):
        return self.counter - 1
    
def main():
    print('Start OneTimePad')
    
#     c = OneTimePad('abc')
#     c = OneTimePad('abc', True)
#     c = OneTimePad('ngcjuoqr')
    c = OneTimePad('ngcjuoqr', True)
    c.getHash()
    print 'last count:', c.getCount()
 

if __name__ == '__main__':
    main()