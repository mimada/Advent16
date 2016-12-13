#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/1
#

class Explosives:
    def __init__(self):
        self.expMsg = ''
        
    def expandMessage(self, message):
        self.expMsg = ''
        pos = 0
        while pos < message.__len__():
            if message[pos] == '(':
                p = message.find(')', pos)
                if p == -1: continue
                rep = message[pos+1:p].split('x')
                for n in range(int(rep[1])):
                    self.expMsg = self.expMsg + message[p+1:p+1+int(rep[0])]
                pos = pos + (p+1+int(rep[0]) - pos)
            else:
                self.expMsg = self.expMsg + message[pos]
                pos = pos + 1
        
        print message, self.expMsg
        
    def expandMessageV2(self, message):
        pos = 0
        cnt = 0
        while pos < message.__len__():
            if message[pos] == '(':
                p = message.find(')', pos)
                if p == -1: continue
                rep = message[pos+1:p].split('x')
                
                n = self.expandMessageV2(message[p+1:p+1+int(rep[0])])
                cnt = cnt + n * int(rep[1])
                
                pos = pos + (p+1+int(rep[0]) - pos)
            else:
                pos = pos + 1
                cnt = cnt + 1
        
        return cnt
        
    def getCount(self):
        return self.expMsg.__len__()
    
def main():
    print('Start Explosives')
    
    message = []
#     with open('Day9_message_test.txt') as f: 
    with open('Day9_message.txt') as f: 
        messages = [line.rstrip('\n') for line in f]

    c = Explosives()
#     c = Explosives()
    for message in messages:
        c.expandMessage(message)
        print 'V1: Number of letters:', c.getCount()

        print 'V2: Number of letters:', c.expandMessageV2(message)
 

if __name__ == '__main__':
    main()