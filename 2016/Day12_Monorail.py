#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/1
#

class Monorail:
    def __init__(self):
        self.count = 0
        self.registers = {'a':0, 'b':0, 'c':1, 'd':0 }
        
    def doCmds(self, cmds = []):
        cnt = 0
        while cnt < cmds.__len__():
            
            cmdSplit = cmds[cnt].split()
            print cnt, cmdSplit
            
            if cmdSplit[0] == 'cpy':
                if cmdSplit[1].isalpha():
                    self.registers[cmdSplit[2]] = self.registers[cmdSplit[1]]
                else:
                    self.registers[cmdSplit[2]] = int(cmdSplit[1])
            elif cmdSplit[0] == 'inc':
                self.registers[cmdSplit[1]] = self.registers[cmdSplit[1]] + 1
            elif cmdSplit[0] == 'dec':
                self.registers[cmdSplit[1]] = self.registers[cmdSplit[1]] - 1
            elif cmdSplit[0] == 'jnz':
                if cmdSplit[1].isalpha():
                    if self.registers[cmdSplit[1]] != 0:
                        cnt = cnt + int(cmdSplit[2]) - 1
                elif int(cmdSplit[1]) != 0:
                    cnt = cnt + int(cmdSplit[2]) - 1
            else:
                print 'unknown command'
            
            print 'cnt {0}, a {1}, b {2}, c {3}, d {4}'.format(cnt, self.registers['a'], self.registers['b'], self.registers['c'], self.registers['d'])
            cnt = cnt + 1
    
    def getRegisterValue(self, reg):
        return self.registers[reg]
    
def main():
    print('Start Monorail')
    
    cmds = []
#     with open('Day12_commands_test.txt') as f: 
    with open('Day12_commands.txt') as f: 
        cmds = [line.rstrip('\n') for line in f]

    c = Monorail()
    c.doCmds(cmds)
    print 'Register value a:', c.getRegisterValue('a')
    print 'Register value b:', c.getRegisterValue('b')
    print 'Register value c:', c.getRegisterValue('c')
    print 'Register value d:', c.getRegisterValue('d')
 

if __name__ == '__main__':
    main()