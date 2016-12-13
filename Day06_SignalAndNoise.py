#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/6
#
class SignalsAndNoise:
    def __init__(self, message = []):
        self.unfilteredMessage = message
    
    def getMessage(self, rev):
        letters = [{},{},{},{},{},{},{},{}]
        for row in self.unfilteredMessage:
            i = 0
            for letter in row:
                if letters[i].has_key(letter):
                    letters[i][letter] = letters[i][letter] + 1
                else:
                    letters[i][letter] = 1
                i = i + 1
        message = ''
        for col in letters:
            if col.__len__() == 0:
                continue
            lettersTup = col.items()
            lettersTup = sorted(lettersTup, key=lambda tup: (tup[1]), reverse=rev )
            message = message + lettersTup[0][0]
        return message
    
def main():
    print('Start SignalsAndNoise')
    
    message = []
#     with open('Day6_message_test.txt') as f: 
    with open('Day6_message.txt') as f: 
        message = [line.rstrip('\n') for line in f]

    c = SignalsAndNoise(message)
    print 'Message:', c.getMessage(False)
 
if __name__ == '__main__':
    main()