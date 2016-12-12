#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/1
#
import md5

class DoorPass:
    def __init__(self):
        self.counter = 0
        
    def getPass(self, doorId):
        pwd = ''
        self.counter = 0
        
        while pwd.__len__() < 8:
            
            m = md5.new('{0}{1}'.format(doorId, self.counter))
            hashStr = m.hexdigest()
#             print self.counter, hashStr, hashStr[:5], pwd
            self.counter = self.counter + 1
            
            if hashStr[:5] == "00000":
                pwd = pwd + hashStr[5:6]
        
        return pwd
    
    def getPass2(self, doorId):
        pwd = list('________')
        pwdCnt = 0
        self.counter = 0
                
        while pwdCnt < 8:
            
            m = md5.new('{0}{1}'.format(doorId, self.counter))
            hashStr = m.hexdigest()
#             print self.counter, hashStr, hashStr[:5], pwd
            self.counter = self.counter + 1
            
            if hashStr[:5] == "00000":
                pos = hashStr[5]
                if pos.isdigit() and int(pos) >= 0 and int(pos) <= 7 and pwd[int(pos)] == '_':
                    pwd[int(pos)] = hashStr[6]
                    pwdCnt = pwdCnt + 1
                    print 'Door password:', ''.join(pwd) 
    
def main():
    print('Start DoorPass')
    
    c = DoorPass()
#     c.getPass('abc')
#     c.getPass2('abc')
#     c.getPass('ugkcyxxp')
    c.getPass2('ugkcyxxp')
 

if __name__ == '__main__':
    main()