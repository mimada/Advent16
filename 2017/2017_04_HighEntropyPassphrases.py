#
# Mikael Martensson
# http://adventofcode.com/2017/day/4
#

class HighEntropyPassphrases:
    
    def getOkPassphrases1(self, fileName):
        okPassphrases = 0
        
        with open(fileName) as fi:
            for line in fi:
                wa = line.split()
                c = 1
                for w in wa:
                    c = c * wa.count(w)
                        
                if c > 1:
                    continue
                okPassphrases = okPassphrases + 1
        return okPassphrases
    
    def getOkPassphrases2(self, fileName):
        okPassphrases = 0
        
        with open(fileName) as fi:
            for line in fi:
                wa = map (lambda x:sorted(x), line.split())
                c = 1
                for w in wa:
                    c = c * wa.count(w)
                    
                if c > 1:
                    continue
                okPassphrases = okPassphrases + 1
        return okPassphrases
    
def main():
    print('Start High-Entropy Passphrases')
    
    c = HighEntropyPassphrases()
    
    print c.getOkPassphrases1('2017_04_Input_test_1.txt')
    print c.getOkPassphrases1('2017_04_Input.txt')
    
    print c.getOkPassphrases2('2017_04_Input_test_2.txt')
    print c.getOkPassphrases2('2017_04_Input.txt')

if __name__ == '__main__':
    main()