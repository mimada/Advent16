#
# Mikael Martensson
# http://adventofcode.com/2018/day/1
#

class ReposeRecord:
    
    def getStrategy1(self, fileName):

        lines = []
        with open(fileName) as fi:
            for line in fi:
                lines.append(line)

        lines.sort()
        scheme = {}

        for l in lines:
            sleepStart = -1
            wakeStart = -1
            idPos = l.find('#')
            sleepPos = l.find('asleep')
            wakePos = l.find('wakes')
            splitLine = l.split()
            date = splitLine[0][6:]

            if idPos > -1:
                id = int(splitLine[3].strip('#'))
                if not id in scheme:
                    scheme[id] = {}
                    scheme[id]['sleepPeriods'] = {}
                    scheme[id]['sleepMinutes'] = {}
                    scheme[id]['totalSleep'] = 0
            elif sleepPos > -1:
                sleepStart = int(splitLine[1][3:5])
                if not date in scheme[id]['sleepPeriods']:
                    scheme[id]['sleepPeriods'][date] = []
                scheme[id]['sleepPeriods'][date].append(sleepStart)
            elif wakePos > -1:
                wakeStart = int(splitLine[1][3:5])
                scheme[id]['sleepPeriods'][date].append(wakeStart)

        #print scheme
        maxId = 0
        maxTime = 0
        maxMinute = 0
        maxMinuteLen = 0

        for id1 in scheme:
            for date1 in scheme[id1]['sleepPeriods']:
                for minute in range(0, len(scheme[id1]['sleepPeriods'][date1]), 2):
                    # Count number of minutes in sleep
                    scheme[id1]['totalSleep'] = scheme[id1]['totalSleep'] + (scheme[id1]['sleepPeriods'][date1][minute + 1] - scheme[id1]['sleepPeriods'][date1][minute])

                    for n in range(scheme[id1]['sleepPeriods'][date1][minute], scheme[id1]['sleepPeriods'][date1][minute + 1]):
                        if not n in scheme[id1]['sleepMinutes']:
                            scheme[id1]['sleepMinutes'][n] = []
                        scheme[id1]['sleepMinutes'][n].append(date1)

            if scheme[id1]['totalSleep'] > maxTime:
                maxTime = scheme[id1]['totalSleep']
                maxId = id1

        print maxId, maxTime

        for minute in scheme[maxId]['sleepMinutes']:
            if len(scheme[maxId]['sleepMinutes'][minute]) > maxMinuteLen:
                maxMinuteLen = len(scheme[maxId]['sleepMinutes'][minute])
                maxMinute = minute

        print 'Strategy1', maxMinute, maxMinuteLen

        maxId2 = 0
        maxMinute2 = 0
        maxMinuteLen2 = 0

        for id in scheme:
            for minute in scheme[id]['sleepMinutes']:
                if len(scheme[id]['sleepMinutes'][minute]) > maxMinuteLen2:
                    maxMinuteLen2 = len(scheme[id]['sleepMinutes'][minute])
                    maxMinute2 = minute
                    maxId2 = id

        print 'Strategy2', maxId2, maxMinute2, maxMinuteLen2

        return (maxId * maxMinute), (maxId2 * maxMinute2)

def main():
    print('Start Repose Record')
    
    c = ReposeRecord()
    
    print c.getStrategy1('2018_04_Input_test_1.txt')
    print c.getStrategy1('2018_04_Input.txt')
    
if __name__ == '__main__':
    main()