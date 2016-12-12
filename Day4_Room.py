#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/1
#
import collections

class Rooms:
    def __init__(self, roomsIn = []):
        self.unfilteredRooms = roomsIn
        self.rooms = []
        self.a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
    def filterRooms(self):
        for ufRoom in self.unfilteredRooms:
            print ufRoom,
            room = {}
            roomSplit = ufRoom.rstrip().split('[', 2)
            room['chk'] = roomSplit[1].strip('] ')
            roomSplit = roomSplit[0].rsplit('-', 1)
            room['name'] = roomSplit[0]
            room['sector'] = roomSplit[1]
            
            if self.calculateCheckSum(room['name']) == room['chk']:
                print '- OK'
                self.rooms.append(room)
            else:
                print '- NOK'
                
#             print self.rooms
            
            
    def calculateCheckSum(self, name):
        chk = ''
        letters = {}
        for letter in name:
            if letters.has_key(letter):
                letters[letter] = letters[letter] + 1
            else:
                letters[letter] = 1
        
        lettersTup = letters.items()
        lettersTup = sorted(lettersTup, key=lambda tup: (tup[0]))
        lettersTup = sorted(lettersTup, key=lambda tup: (tup[1]), reverse=True )
        
        for k, v in lettersTup:
            if k == '-': continue
            chk = chk + k
        
        print chk[:5],
        return chk[:5]
    
    def getSectorSum(self):
        sectorSum = 0
        for room in self.rooms:
            sectorSum = sectorSum + int(room['sector'])
        return sectorSum
    
    def encrypt(self):
        
        for room in self.rooms:
            sector = int(room['sector'])
            offset = sector % 26
            words = ''
            
            for letter in room['name']:
                if letter == '-':
                    words = words + ' '
                    continue
                asc = ord(letter) + offset
                if asc > 122:
                    asc = asc - 26
                words = words + chr(asc)
            room['encrypted'] = words
            print words
            
    def getRoomSector(self, name):
        for room in self.rooms:
            if room['encrypted'].find(name) > -1:
                print room['encrypted']
                return room['sector']
        return 'None'
    
def main():
    print('Start Rooms')
    
    rooms = []
#    with open('Day4_roomlist_test.txt') as f: 
    with open('Day4_roomlist.txt') as f: 
        rooms = [line.rstrip('\n') for line in f]

    c = Rooms(rooms)
    c.filterRooms()
    c.encrypt()
    print 'Sum of sector id:', c.getSectorSum()
    print 'Sector id:', c.getRoomSector('object')
#    print 'Sector id:', c.getRoomSector('encrypted')
 
    testSum = 1514

if __name__ == '__main__':
    main()