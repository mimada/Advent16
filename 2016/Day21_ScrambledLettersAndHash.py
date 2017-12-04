#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/1
#

class ScrambledLettersAndHash:
    def __init__(self, input = ''):
        self.letters = list(input)
            
    def doScramble(self, cmd):
        cmdSplit = cmd.split()
        
        # swap position 4 with position 0
        if cmd.find('swap position') != -1:
            p1 = int(cmdSplit[2])
            p2 = int(cmdSplit[5])
            
            if p1 > p2:
                l1 = self.letters.pop(p1)
                l2 = self.letters.pop(p2)
                self.letters.insert(p2, l1)
                self.letters.insert(p1, l2)
            else:
                l2 = self.letters.pop(p2)
                l1 = self.letters.pop(p1)
                self.letters.insert(p1, l2)
                self.letters.insert(p2, l1)
            
        # swap letter d with letter b
        elif cmd.find('swap letter') != -1:
            p1 = self.letters.index(cmdSplit[2])
            p2 = self.letters.index(cmdSplit[5])
            
            if p1 > p2:
                l1 = self.letters.pop(p1)
                l2 = self.letters.pop(p2)
                self.letters.insert(p2, l1)
                self.letters.insert(p1, l2)
            else:
                l2 = self.letters.pop(p2)
                l1 = self.letters.pop(p1)
                self.letters.insert(p1, l2)
                self.letters.insert(p2, l1)
            
        # reverse positions 0 through 4
        elif cmd.find('reverse positions') != -1:
            p1 = int(cmdSplit[2])
            p2 = int(cmdSplit[4])
            p = p2
            s = self.letters[p1:p2+1]
            for l in s:
                self.letters[p] = l
                p = p - 1
                
        # rotate left 1 step
        elif cmd.find('rotate left') != -1:
            p1 = int(cmdSplit[2])
            for n in range(p1):
                c = self.letters.pop(0)
                self.letters.append(c)
            
        # rotate right 1 step
        elif cmd.find('rotate right') != -1:
            p1 = int(cmdSplit[2])
            for n in range(p1):
                c = self.letters.pop()
                self.letters.insert(0, c)
            
        # move position 3 to position 0
        elif cmd.find('move position') != -1:
            p1 = int(cmdSplit[2])
            p2 = int(cmdSplit[5])
            c = self.letters.pop(p1)
            self.letters.insert(p2, c)
            
        # rotate based on position of letter b
        elif cmd.find('rotate based on position of letter') != -1:
            p1 = self.letters.index(cmdSplit[6])
            p = 1 + p1
            if p1 >= 4:
                p = p + 1
            for n in range(p):
                c = self.letters.pop()
                self.letters.insert(0, c)
            
            
        else:
            print "Unknown command:", cmd
        
    def doDeScramble(self, cmd):
        cmdSplit = cmd.split()
        
        # rotate left 1 step
        if cmd.find('rotate left') != -1:
            cmd = 'rotate right {0} step'.format(cmdSplit[2])
            
        # rotate right 1 step
        elif cmd.find('rotate right') != -1:
            cmd = 'rotate left {0} step'.format(cmdSplit[2])
            
        # move position 3 to position 0
        elif cmd.find('move position') != -1:
            cmd = 'move position {0} to position {1}'.format(cmdSplit[5], cmdSplit[2])
            
        # rotate based on position of letter b
        elif cmd.find('rotate based on position of letter') != -1:
            p1 = self.letters.index(cmdSplit[6])
            if p1 % 2:
                p = (p1+1)/2
            else:
                p = 4 + (p1+2)/2
                if not p1:
                    p = p + 4
                
            cmd = 'rotate left {0} step'.format(p)
            
        self.doScramble(cmd)
        
    def getWord(self):
        return ''.join(self.letters)
    
def main():
    print('Start ScrambledLettersAndHash')
    
    cmds = []
#     with open('Day21_commands_test.txt') as f: 
    with open('Day21_commands.txt') as f: 
        cmds = [line.rstrip('\n') for line in f]

#     c = ScrambledLettersAndHash('abcde')
    c = ScrambledLettersAndHash('abcdefgh')
#     c = ScrambledLettersAndHash('fbgdceah')
    for cmd in cmds:
        c.doScramble(cmd)
        print c.getWord(), cmd
    print 'Result:', c.getWord()
    
#     c1 = ScrambledLettersAndHash(c.getWord())
    c1 = ScrambledLettersAndHash('fbgdceah')
    cmds.reverse()
    for cmd in cmds:
        c1.doDeScramble(cmd)
        print c1.getWord(), cmd
    print 'Result:', c1.getWord()
    
 

if __name__ == '__main__':
    main()
