#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/1
#

class Bots:
    def __init__(self, v1, v2):
        self.values = []
        self.values.append(v1)
        self.values.append(v2)
        self.values.sort()
        self.bots = {}
        
    def createBot(self, bot):
        self.bots[bot] = {}
        self.bots[bot]['values'] = []
        self.bots[bot]['high'] = ''
        self.bots[bot]['low'] = ''
        
    def giveValue(self, bot, value):
        
        if not self.bots.has_key(bot):
            self.createBot(bot)
        self.bots[bot]['values'].append(value)
        
    def setDestination(self, bot, low, high):
        if not self.bots.has_key(bot):
            self.createBot(bot)
        if not self.bots.has_key(low):
            self.createBot(low)
        if not self.bots.has_key(high):
            self.createBot(high)
        
        self.bots[bot]['high'] = high
        self.bots[bot]['low'] = low
        
    def formatName(self, type, no):
        return '{:s}{:03d}'.format(type, no)
    
    def doCommand(self, cmd):
        cmdSplit = cmd.split()
        print cmdSplit
        
        if cmdSplit[0].find('bot') != -1:
            # bot 2 gives low to bot 1 and high to bot 0
            b = self.formatName(cmdSplit[0], int(cmdSplit[1]))
            l = self.formatName(cmdSplit[5], int(cmdSplit[6]))
            h = self.formatName(cmdSplit[10], int(cmdSplit[11]))
            self.setDestination(b, l, h)
            
        elif cmdSplit[0].find('value') != -1:
            # value 5 goes to bot 2
            b = self.formatName(cmdSplit[4], int(cmdSplit[5]))
            self.giveValue(b, int(cmdSplit[1]))
            
        else:
            print "Unknown command"
            
    def evaluate(self):
        val = 1
        while val > 0:
            val = 0
            for key in self.bots.iterkeys():
                if key.find('output') == 0:
                    continue
                if self.bots[key]['values'].__len__() != 2:
                    val = val + self.bots[key]['values'].__len__()
                    continue
                else:
                    self.bots[key]['values'].sort()
                    high = self.bots[key]['values'].pop()
                    low = self.bots[key]['values'].pop()
                    
                    self.giveValue(self.bots[key]['low'], low)
                    self.giveValue(self.bots[key]['high'], high)
                        
                    if low == self.values[0] and high == self.values[1]:
                        print '{0} compare {1} and {2}'.format(key, low, high)
                    
def main():
    print('Start Bots')
    
    cmds = []
#     with open('Day10_commands_test.txt') as f: 
    with open('Day10_commands.txt') as f: 
        cmds = [line.rstrip('\n') for line in f]

#     c = Bots(5, 2)
    c = Bots(61, 17)
    for cmd in cmds:
        c.doCommand(cmd)
    c.evaluate()
    keys = c.bots.keys()
    keys.sort()
    for key in keys:
        print 'Key: ', key, ': ', c.bots[key]
    
    print c.bots['output000']['values'][0] * c.bots['output001']['values'][0] * c.bots['output002']['values'][0]
 

if __name__ == '__main__':
    main()