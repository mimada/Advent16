#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/1
#

class WcPass:
    def __init__(self, keyPadType = 1):
        self.key = '5'
        
        if keyPadType == 1:
            # KeyPad 1
            # 1 2 3
            # 4 5 6
            # 7 8 9
            #
            self.keyPad = {}
            self.keyPad['1'] = {'U':'1','D':'4', 'L':'1', 'R':'2'}
            self.keyPad['2'] = {'U':'2','D':'5', 'L':'1', 'R':'3'}
            self.keyPad['3'] = {'U':'3','D':'6', 'L':'2', 'R':'3'}
            self.keyPad['4'] = {'U':'1','D':'7', 'L':'4', 'R':'5'}
            self.keyPad['5'] = {'U':'2','D':'8', 'L':'4', 'R':'6'}
            self.keyPad['6'] = {'U':'3','D':'9', 'L':'5', 'R':'6'}
            self.keyPad['7'] = {'U':'4','D':'7', 'L':'7', 'R':'8'}
            self.keyPad['8'] = {'U':'5','D':'8', 'L':'7', 'R':'9'}
            self.keyPad['9'] = {'U':'6','D':'9', 'L':'8', 'R':'9'}
        elif keyPadType == 2:
            # KeyPad 2
            #     1
            #   2 3 4
            # 5 6 7 8 9
            #   A B C
            #     D
            #
            self.keyPad = {}
            self.keyPad['1'] = {'U':'1','D':'3', 'L':'1', 'R':'1'}
            self.keyPad['2'] = {'U':'2','D':'6', 'L':'2', 'R':'3'}
            self.keyPad['3'] = {'U':'1','D':'7', 'L':'2', 'R':'4'}
            self.keyPad['4'] = {'U':'4','D':'8', 'L':'3', 'R':'4'}
            self.keyPad['5'] = {'U':'5','D':'5', 'L':'5', 'R':'6'}
            self.keyPad['6'] = {'U':'2','D':'A', 'L':'5', 'R':'7'}
            self.keyPad['7'] = {'U':'3','D':'B', 'L':'6', 'R':'8'}
            self.keyPad['8'] = {'U':'4','D':'C', 'L':'7', 'R':'9'}
            self.keyPad['9'] = {'U':'9','D':'9', 'L':'8', 'R':'9'}
            self.keyPad['A'] = {'U':'6','D':'A', 'L':'A', 'R':'B'}
            self.keyPad['B'] = {'U':'7','D':'D', 'L':'A', 'R':'C'}
            self.keyPad['C'] = {'U':'8','D':'C', 'L':'B', 'R':'C'}
            self.keyPad['D'] = {'U':'B','D':'D', 'L':'D', 'R':'D'}
        else:
            return
        
    def move(self, directionArr):
        for d in directionArr:
            self.key = self.keyPad[self.key][d]

    def getKey(self):
        return self.key
    
def main():
    print('Start WC Pass')
    
    moves1 = []
    moves1.append('ULL')
    moves1.append('RRDDD')
    moves1.append('LURDL')
    moves1.append('UUUUD')

    wcp = WcPass()
    wcp.move(moves1[0])
    print 'KeyPad 1 code:', wcp.getKey(),
    wcp.move(moves1[1])
    print wcp.getKey(),
    wcp.move(moves1[2])
    print wcp.getKey(),
    wcp.move(moves1[3])
    print wcp.getKey()
 
    moves2 = []
    moves2.append('ULUULLUULUUUUDURUUULLDLDDRDRDULULRULLRLULRUDRRLDDLRULLLDRDRRDDLLLLDURUURDUDUUURDRLRLLURUDRDULURRUDLRDRRLLRDULLDURURLLLULLRLUDDLRRURRLDULRDDULDLRLURDUDRLLRUDDRLRDLLDDUURLRUDDURRLRURLDDDURRDLLDUUDLLLDUDURLUDURLRDLURURRLRLDDRURRLRRDURLURURRRULRRDLDDDDLLRDLDDDRDDRLUUDDLDUURUULDLUULUURRDRLDDDULRRRRULULLRLLDDUDRLRRLLLLLDRULURLLDULULLUULDDRURUDULDRDRRURLDRDDLULRDDRDLRLUDLLLDUDULUUUUDRDRURDDULLRDRLRRURLRDLRRRRUDDLRDDUDLDLUUDLDDRRRDRLLRLUURUDRUUULUDDDLDUULULLRUDULULLLDRLDDLLUUDRDDDDRUDURDRRUUDDLRRRRURLURLD')
    moves2.append('LDLUDDLLDDRLLDLDRDDDDDUURUDDDUURLRLRLDULLLDLUDDDULLDUDLRUUDDLUULLDRLDDUDLUDDLURRRLDUURDDRULLURLLRLLUUDRLDDDLDLDRDUDLRDURULDLDRRDRLDLUURRRRLUDDULDULUUUDULDDRLLDDRRUULURRUURRLDUUUDDDDRUURUDRRRDDDDLRLURRRRUUDDDULRRURRDLULRURDDRDRLUDLURDDRDURRUURDUDUDRRDDURRRDURDLUUUURRUDULLDDRLLLURLDUDRRLDDLULUDUDDDDUDLUUULUURUDRURUUDUUURRLDUUDRDRURLLDLLLLLRLLUDURDRRLULRRDDDRLDRDDURLRDULULLDDURURLRRDRULDULUUUURLDURUDUDUDDLUDRRDURULRDULLLDRRDLDLUDURDULULLDDURDDUDRUUUDUDRLDUURDUUUDUURURUDRULRURLDLRDDURDLUU')
    moves2.append('DDLDRLLDRRDRRLLUUURDDULRDUDRDRUDULURLLDDLRRRUDRDLDLURRRULUDRDLULLULLDUUDRLRUDDLRRURRUULRLDLLLDLRLLLURLLLURLLRDDLULLDUURLURDLLDLDUDLDRUUUDDLLDRRRRRUDRURUURRRDRUURDRDDRLDUUULUDUDRUDLLLLDRDRURRRDUUURLDLRLRDDDRLUDULDRLLULRDLDURDLDURUUDDULLULRDDRLRUURLLLURDRUURUUDUUULRDUDDRDURRRDUUDRRRUDRDLRURDLLDDDURLLRRDDDDLDULULDRLDRULDDLRRRLUDLLLLUDURRRUURUUULRRLDUURDLURRLRLLRDLRDDRDDLRDLULRUUUDDDUDRRURDDURURDDUDLURUUURUUUUDURDDLDRDULDRLDRLLRLRRRLDRLLDDRDLDLUDDLUDLULDLLDRDLLRDULDUDDULRRRUUDULDULRRURLRDRUDLDUDLURRRDDULRDDRULDLUUDDLRDUURDRDR')
    moves2.append('URDURRRRUURULDLRUUDURDLLDUULULDURUDULLUDULRUDUUURLDRRULRRLLRDUURDDDLRDDRULUUURRRRDLLDLRLRULDLRRRRUDULDDURDLDUUULDURLLUDLURULLURRRDRLLDRRDULUDDURLDULLDURLUDUULRRLLURURLDLLLURDUDRLDDDRDULLUDDRLDDRRRLDULLLLDUURULUDDDURUULUUUDURUDURDURULLLDRULULDRRLDRLDLRLRUDUDURRLURLRUUDRRDULULDLLDRDRRRDUDUURLDULLLURRDLUDDLDDRDDUDLDDRRRUDRULLURDDULRLDUDDDRULURLLUDLLRLRRDRDRRURUUUURDLUURRDULLRDLDLRDDRDRLLLRRDDLDDDDLUDLRLULRRDDRDLDLUUUDLDURURLULLLDDDULURLRRURLDDRDDLD')
    moves2.append('UDUULLRLUDLLUULRURRUUDDLLLDUURRURURDDRDLRRURLLRURLDDDRRDDUDRLLDRRUDRDRDDRURLULDDLDLRRUDDULLRLDDLRURLUURUURURDLDUDRLUUURRRLUURUDUDUUDDLDULUULRLDLLURLDRUDRLLRULURDLDDLLULLDRRUUDDLRRRUDDLRDRRRULDRDDRRULLLUDRUULURDUDRDLRRLDLRLRLDDULRRLULUUDDULDUDDULRRURLRDRDURUDDDLLRLDRDRULDDLLRLLRDUDDDDDDRLRLLDURUULDUUUDRURRLLRLDDDDRDRDUURRURDRDLLLUDDRDRRRDLUDLUUDRULURDLLLLLRDUDLLRULUULRLULRURULRLRRULUURLUDLDLLUURDLLULLLDDLRUDDRULRDLULRUURLDRULRRLULRLRULRDLURLLRURULRDRDLRRLRRDRUUURURULLLDDUURLDUDLLRRLRLRULLDUUUULDDUUU')

    wcp = WcPass()
    wcp.move(moves2[0])
    print 'KeyPad 1 code:', wcp.getKey(),
    wcp.move(moves2[1])
    print wcp.getKey(),
    wcp.move(moves2[2])
    print wcp.getKey(),
    wcp.move(moves2[3])
    print wcp.getKey(),
    wcp.move(moves2[4])
    print wcp.getKey()

    wcp = WcPass(2)
    wcp.move(moves1[0])
    print 'KeyPad 2 code:', wcp.getKey(),
    wcp.move(moves1[1])
    print wcp.getKey(),
    wcp.move(moves1[2])
    print wcp.getKey(),
    wcp.move(moves1[3])
    print wcp.getKey()

    wcp = WcPass(2)
    wcp.move(moves2[0])
    print 'KeyPad 2 code:', wcp.getKey(),
    wcp.move(moves2[1])
    print wcp.getKey(),
    wcp.move(moves2[2])
    print wcp.getKey(),
    wcp.move(moves2[3])
    print wcp.getKey(),
    wcp.move(moves2[4])
    print wcp.getKey()

if __name__ == '__main__':
    main()