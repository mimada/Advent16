#
# Mikael Martensson
# http://adventofcode.com/2018/day/1
#

class ChronalCalibration:
    
    def getCurrentFrequency(self, fileName):
        s1 = 0
        
        with open(fileName) as fi:
            for line in fi:
                s1 = s1 + int(line)

        return s1

    def getCurrentFrequencyReachedTwice(self, fileName):
        s1 = 0
        sums = []

        with open(fileName) as fi:
            while True:
                print s1
                fi.seek(0)
                for line in fi:
                    s1 = s1 + int(line)
                    if s1 in sums:
                        return s1
                    sums.append(s1)

        return error


def main():
    print('Start Chronal Calibration')
    
    c = ChronalCalibration()
    
    print c.getCurrentFrequency('2018_01_Input_test_1.txt')
    print c.getCurrentFrequency('2018_01_Input.txt')
    
    print c.getCurrentFrequencyReachedTwice('2018_01_Input_test_1.txt')
    print c.getCurrentFrequencyReachedTwice('2018_01_Input.txt')

if __name__ == '__main__':
    main()