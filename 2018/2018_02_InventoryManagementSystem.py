#
# Mikael Martensson
# http://adventofcode.com/2018/day/1
#

class InventoryManagementSystem:
    
    def getChecksum(self, fileName):
        cnt2 = 0
        cnt3 = 0

        with open(fileName) as fi:
            for line in fi:
                ch = {}
                line.strip()
                for c in line:
                    if c in ch:
                        ch[c] = ch[c] + 1
                    else:
                        ch[c] = 1
                done2 = False
                done3 = False
                for c in ch:
                    if ch[c] == 2 and not done2:
                        done2 = True
                        cnt2 = cnt2 + 1
                    if ch[c] == 3 and not done3:
                        done3 = True
                        cnt3 = cnt3 + 1
        return cnt2, cnt3, cnt2 * cnt3

    def getProductId(self, fileName):

        lines = []
        with open(fileName) as fi:
            for line in fi:
                lines.append(line.strip())
        lines.sort()
        for i in range(len(lines) - 1):
            errors = []
            for ii in range(len(lines[i])):
                if not lines[i][ii] == lines[i+1][ii]:
                    errors.append(ii)
            if len(errors) == 1:
                print lines[i], lines[i+1]
                print lines[i][:errors[0]] + lines[i][errors[0]+1:]




def main():
    print('Start Inventory Management System')
    
    c = InventoryManagementSystem()
    
    print c.getChecksum('2018_02_Input_test_1.txt')
    print c.getChecksum('2018_02_Input.txt')
    
    print c.getProductId('2018_02_Input_test_2.txt')
    print c.getProductId('2018_02_Input.txt')

if __name__ == '__main__':
    main()