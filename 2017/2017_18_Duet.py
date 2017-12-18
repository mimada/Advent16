#
# Mikael Martensson
# http://adventofcode.com/2017/day/4
#

class Duet:
    def __init__(self):
        self.instructions = []
        self.registers = {}
    
    def execute(self):
#         print reg, self.registers[reg], cmd, value
        index = 0
        snd = 0
        while index < len(self.instructions):
            cmd = self.instructions[index][0]
            
            x = self.instructions[index][1]
            if x.isalpha():
                if not self.registers.has_key(x):
                    self.registers[x] = 0
            
            if len(self.instructions[index]) > 2:
                y = self.instructions[index][2]
                if y.isalpha():
                    if not self.registers.has_key(y):
                        self.registers[y] = 0
            
            if cmd == 'set':
                if y.isalpha():
                    self.registers[x] = self.registers[y]
                else:
                    self.registers[x] = int(y)
            elif cmd == 'add':
                if y.isalpha():
                    self.registers[x] = self.registers[x] + self.registers[y]
                else:
                    self.registers[x] = self.registers[x] + int(y)
            elif cmd == 'mul':
                if y.isalpha():
                    self.registers[x] = self.registers[x] * self.registers[y]
                else:
                    self.registers[x] = self.registers[x] * int(y)
            elif cmd == 'mod':
                if y.isalpha():
                    self.registers[x] = self.registers[x] % self.registers[y]
                else:
                    self.registers[x] = self.registers[x] % int(y)
            elif cmd == 'snd':
                if x.isalpha():
                    snd = self.registers[x]
                else:
                    snd = int(y)
            elif cmd == 'rcv':
                if x.isalpha():
                    rcv = self.registers[x]
                else:
                    rcv = int(x)
                if x > 0:
                    print snd
                    break
            elif cmd == 'jgz':
                if x.isalpha():
                    jgz = self.registers[x]
                else:
                    jgz = int(x)
                if jgz > 0:
                    if y.isalpha():
                        index = index + self.registers[y]
                    else:
                        index = index + int(y)
                    continue 
            else:
                print 'Unknown command:', cmd
            index = index + 1
    
    def parseFile(self, fileName):
        with open(fileName) as fi:
            for line in fi:
                self.instructions.append(line.split())
                
        print self.instructions
    
def main():
    print('Start Duet')
    
    c = Duet()
#     c.parseFile('2017_18_Input_test_1.txt')
    c.parseFile('2017_18_Input.txt')
    c.execute()
    
if __name__ == '__main__':
    main()