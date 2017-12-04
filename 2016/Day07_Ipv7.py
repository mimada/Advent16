#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/1
#

class Ipv7:
    def __init__(self, message = []):
        self.unfilteredMessage = message
        self.tlsMessages = []
        self.sslMessages = []
        self.count = 0
        
    def myRange(self, start, end, step):
        while start <= end:
            yield start
            start += step
            
    def getTlsMessages(self):
        for line in self.unfilteredMessage:
            line = line.replace('[', ' [')
            line = line.replace(']', '] ')
            lineSplit = line.rstrip().split()
            lineOk = 0
            print lineSplit
            for word in lineSplit:
                abba, notOk = self.checkForTls(word)
                if notOk:
                    lineOk = 0
                    break
                else:
                    lineOk = lineOk + abba
            if lineOk:
                print 'line ok'
                self.tlsMessages.append(lineSplit)
                
    def getSslMessages(self):
        for line in self.unfilteredMessage:
            line = line.replace('[', ' [')
            line = line.replace(']', '] ')
            lineSplit = line.rstrip().split()
            print lineSplit
            abas = []
            babs = []
            for word in lineSplit:
                ssl1, ssl2 = self.checkForSsl(word)
                abas.extend(ssl1)
                babs.extend(ssl2)
                
            print abas
            print babs
            
            lineOk = False
            for aba in abas:
                if babs.count(aba) != 0:
                    lineOk = True
                    break
            
            if lineOk:
                print 'line ok'
                self.sslMessages.append(lineSplit)
                
    def checkForTls(self, word = ''):
        offset = 0
        if word[0] == '[':
            offset = 1
        for pos in self.myRange(offset, word.__len__() - 4, 1):
            abba = word[pos:pos+2] + word[pos+1] + word[pos]
            print abba
            if word[pos+1] == word[pos]: continue
            if word.find(abba) != -1:
                if offset:
                    return 1, True
                else:
                    return 1, False
        return 0, False
    
    def checkForSsl(self, word = ''):
        ssl1 = []
        ssl2 = []
        offset = 0
        if word[0] == '[':
            offset = 1
        for pos in self.myRange(offset, word.__len__() - 3, 1):
            if word[pos] == word[pos+2] and word[pos] != word[pos+1]:
                if offset == 1:
                    bab = word[pos+1] + word[pos] + word[pos+1]
                    ssl2.append(bab)
                else:
                    ssl1.append(word[pos:pos+3])
        return ssl1, ssl2
    
    def getTlsCount(self):
        return self.tlsMessages.__len__()
    
    def getSslCount(self):
        return self.sslMessages.__len__()
    
def main():
    print('Start Ipv7')
    
    message = []
#     with open('Day07_message_test.txt') as f: 
    with open('Day07_message.txt') as f: 
        message = [line.rstrip('\n') for line in f]


    c = Ipv7(message)
    c.getTlsMessages()
    c.getSslMessages()
    print 'Number of TLS:', c.getTlsCount()
    print 'Number of SSL:', c.getSslCount()
 

if __name__ == '__main__':
    main()