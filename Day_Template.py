#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/1
#

class Triangles:
    def __init__(self):
        self.count = 0
        
    def getCount(self):
        return self.count
    
def main():
    print('Start Triangles')
    
    moves1 = []

    c = Triangles()
    c.move(moves1[0])
    print 'KeyPad 1 code:', c.getCount()
 

if __name__ == '__main__':
    main()