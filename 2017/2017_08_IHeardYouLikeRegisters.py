#
# Mikael Martensson
# http://adventofcode.com/2017/day/4
#

class IHeardYouLikeRegisters:
    def __init__(self):
        self.registers = {}
    
    def getHighestValue(self):
        value = -99
        keys = self.registers.keys()
        for v in keys:
            if self.registers[v] > value:
                value = self.registers[v]
        return value
    
    def compare(self, reg, comp, value):
#         print reg, self.registers[reg], comp, value
        if comp == '>':
            return self.registers[reg] > value
        elif comp == '<':
            return self.registers[reg] < value
        elif comp == '<=':
            return self.registers[reg] <= value
        elif comp == '>=':
            return self.registers[reg] >= value
        elif comp == '!=':
            return self.registers[reg] != value
        elif comp == '==':
            return self.registers[reg] == value
        else:
            print 'Unknown comparator:', comp
    
    def execute(self, reg, cmd, value):
#         print reg, self.registers[reg], cmd, value
        if cmd == 'inc':
            self.registers[reg] = self.registers[reg] + value
        elif cmd == 'dec':
            self.registers[reg] = self.registers[reg] - value
        else:
            print 'Unknown command:', cmd
    
    def parseFile(self, fileName):
        highestValue = -99
        with open(fileName) as fi:
            for line in fi:
#                 print self.registers
                cmd = line.split()
#                 print cmd
                
                if not cmd[0] in self.registers:
                    self.registers[cmd[0]] = 0
                
                if not cmd[4] in self.registers:
                    self.registers[cmd[4]] = 0
                
                if self.compare(cmd[4], cmd[5], int(cmd[6])):
                    self.execute(cmd[0], cmd[1], int(cmd[2]))
                    
                value = self.getHighestValue()
                if value > highestValue:
                    highestValue = value
                    
        print self.getHighestValue(), highestValue
    
def main():
    print('Start I Heard You Like Registers')
    
    c = IHeardYouLikeRegisters()
#     c.parseFile('2017_08_Input_test_1.txt')
    c.parseFile('2017_08_Input.txt')
    
if __name__ == '__main__':
    main()