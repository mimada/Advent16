#
# Mikael Martensson
# http://adventofcode.com/2018/day/7
#

class TheSumOfItsParts:
    def __init__(self):
        self.first = []
        self.last = []
        self.data = {}
        self.data['before'] = {}
        self.data['after'] = {}

    def getDataFromFile(self, fileName):
        self.first = []
        self.last = []
        self.data = {}
        self.data['before'] = {}
        self.data['after'] = {}

        with open(fileName) as fi:
            for line in fi:
                s = line.strip().split()
                before = s[1]
                after = s[7]

                if before not in self.data['before']:
                    self.data['before'][before] = []
                self.data['before'][before].append(after)

                if after not in self.data['after']:
                    self.data['after'][after] = []
                self.data['after'][after].append(before)

        beforeKeys = self.data['before'].keys()
        beforeKeys.sort()
        print 'beforeKeys', beforeKeys
        afterKeys = self.data['after'].keys()
        afterKeys.sort()
        print 'afterKeys', afterKeys

        # Get first letter
        for a in beforeKeys:
            if a not in afterKeys:
                self.first.append(a)

        # Get last letter
        for a in afterKeys:
            if a not in beforeKeys:
                self.last.append(a)

        print self.first, self.last, self.data

    def getInstructionOrder(self, fileName):
        self.getDataFromFile(fileName)
        candidateList = []
        candidateList.extend(self.first)
        candidateList.sort()
        string = candidateList[0]
        candidateList.remove(string[-1])
        self.last.sort()

        while not string[-1] == self.last[-1]:

            candidateList.extend(self.data['before'][string[-1]])
            candidateList.sort()

            for letter in candidateList:
                prerequisitesOk = True
                # is prerequisites ok?
                if letter not in self.first:
                    for la in self.data['after'][letter]:
                        if la not in string:
                            prerequisitesOk = False
                            break

                if prerequisitesOk:
                    string = string + letter
                    break

            for i in range(candidateList.count(string[-1])):
                candidateList.remove(string[-1])

        return string

    def getSec(self, letter='', baseTime=0):
        a = ord(letter.upper()) - ord('A') + 1 + baseTime

    def getInstructionOrderX(self, fileName, workers, baseTime):
        self.getDataFromFile(fileName)
        candidateList = []
        candidateList.extend(self.first)
        candidateList.sort()
        string = candidateList[0]
        candidateList.remove(string[-1])
        self.last.sort()

        while not string[-1] == self.last[-1]:

            candidateList.extend(self.data['before'][string[-1]])
            candidateList.sort()

            for letter in candidateList:
                prerequisitesOk = True
                # is prerequisites ok?
                if letter not in self.first:
                    for la in self.data['after'][letter]:
                        if la not in string:
                            prerequisitesOk = False
                            break

                if prerequisitesOk:
                    string = string + letter
                    break

            for i in range(candidateList.count(string[-1])):
                candidateList.remove(string[-1])

        return string


def main():
    print('Start The Sum of Its Parts')

    c = TheSumOfItsParts()

    print c.getInstructionOrder('2018_07_Input_test_1.txt')
#    print c.getInstructionOrder('2018_07_Input.txt')

    print c.getInstructionOrderX('2018_07_Input_test_1.txt', 2, 0)
#    print c.getInstructionOrderX('2018_07_Input.txt', 5, 60)


if __name__ == '__main__':
    main()