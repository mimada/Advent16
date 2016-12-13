#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/1
#

class TwoFactAuth:
    def __init__(self, w, h):
        self
        self.w = w
        self.h = h
        self.pixels = [[0 for x in range(w)] for y in range(h)]
        
    def printPixels(self):
        for row in self.pixels:
            txt = ''
            for x in row:
                if x:
                    txt = txt + '*'
                else:
                    txt = txt + ' '
            print txt
            
    def doCommand(self, cmd):
        if cmd.find('rect') != -1:
            cmdSplit = cmd.split()
            values = cmdSplit[1].split('x')
            print 'create rect, {0} wide and {1} high (cmd: {2})'.format(values[0], values[1], cmd)
            for row in range(int(values[1])):
                for col in range(int(values[0])):
                    self.pixels[row][col] = 1
            
        elif cmd.find('rotate column') != -1:
#             rotate column x=1 by 1
            cmdSplit = cmd.split()
            values = cmdSplit[2].split('=')
            col = int(values[1])
            step = int(cmdSplit[4]) % self.h
            print 'rotate column {0}, {1} steps (cmd: {2}'.format(col, step, cmd)
            for s in range(step):
                for r in range(self.h):
                    if r == 0:
                        v = self.pixels[self.h - 1][col]
                    elif r == self.h - 1:
                        self.pixels[1][col] = self.pixels[0][col]
                        self.pixels[0][col] = v
                    else:
                        self.pixels[self.h - r][col] = self.pixels[self.h - 1 - r][col]
            
        elif cmd.find('rotate row') != -1:
            cmdSplit = cmd.split()
            values = cmdSplit[2].split('=')
            row = int(values[1])
            step = int(cmdSplit[4]) % self.w
            print 'rotate row {0}, {1} steps (cmd: {2}'.format(row, step, cmd)
            for s in range(step):
                for c in range(self.w):
                    if c == 0:
                        v = self.pixels[row][self.w - 1]
                    elif c == self.w - 1:
                        self.pixels[row][1] = self.pixels[row][0]
                        self.pixels[row][0] = v
                    else:
                        self.pixels[row][self.w - c] = self.pixels[row][self.w - 1 - c]
            
        else:
            print "Unknown command"
        
    def getCount(self):
        count = 0
        for row in self.pixels:
            for v in row:
                count = count + v
        return count
    
def main():
    print('Start TwoFactAuth')
    
    cmds = []
#     with open('Day8_commands_test.txt') as f: 
    with open('Day8_commands.txt') as f: 
        cmds = [line.rstrip('\n') for line in f]

    c = TwoFactAuth(50, 6)
#     c = TwoFactAuth(7, 3)
    for cmd in cmds:
        c.doCommand(cmd)
    c.printPixels()
    print 'number of pixels:', c.getCount()
 

if __name__ == '__main__':
    main()