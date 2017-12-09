#
# Mikael Martensson
# http://adventofcode.com/2017/day/4
#

class StreamProcessing:
    
    def parseFile(self, fileName):
        inStream = ""
        with open(fileName) as fi:
            for line in fi:
                inStream = inStream + line

        return inStream
    
    def getFilteredData(self, dataStream = ""):
        pos = 0
        while pos != -1:
            pos = dataStream.find('!')
            if pos != -1:
                dataStream = dataStream.replace(dataStream[pos:pos + 2], '', 1)
        
        pos = 0
        pos2 = 0
        garbageCount = 0
        while pos != -1:
            pos = dataStream.find('<')
            if pos != -1:
                pos2 = dataStream[pos:].find('>')
                dataStream = dataStream.replace(dataStream[pos:pos2 + pos + 1], '', 1)
                garbageCount = garbageCount + pos2 - 1
        
        print 'garbageCount:', garbageCount
        return dataStream
    
    def getScore(self, data):
        level = 0
        score = 0
        
        for c in data:
            if c == '{':
                level = level + 1
                score = score + level
            elif c == '}':
                level = level - 1
        return score
    
def main():
    print('Start Stream Processing')
    
    streamData = ['{}', '{{{}}}', '{{},{}}',
                  '{{{},{},{{}}}}',
                  '{<{},{},{{}}>}',
                  '{<a>,<b>,<c>,<d>}',
                  '{{<ab>},{<ac>},{<ad>},{<ae>}}',
                  '{{<!!>},{<!!a>},{<!a!b>},{<!}!\\>}}',
                  '{{<a!>},{<b!>},{<c!>},{<a>}}'
                 ]
    
    c = StreamProcessing()
    for data in streamData:
        
        filteredData = c.getFilteredData(data)
        print filteredData
        print c.getScore(filteredData)
    
    print 'data from 2017_09_Input.txt'
    filteredData = c.getFilteredData(c.parseFile('2017_09_Input.txt'))
    print c.getScore(filteredData)
    
    
    
if __name__ == '__main__':
    main()