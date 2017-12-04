#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/1
#

class StreetGrid:
    def __init__(self, before = False):
        self.heading = 'N'
        self.x = 0
        self.y = 0
        self.pointArr = []
        self.before = before

    def move(self, point, ):
        step = int(str(point)[1:])
        if self.heading == 'N':
            if str(point).startswith('L'):
                self.heading = 'V'
                return self.moveStep(step)
            else:
                self.heading = 'E'
                return self.moveStep(step)
        elif self.heading == 'S':
            if str(point).startswith('L'):
                self.heading = 'E'
                return self.moveStep(step)
            else:
                self.heading = 'V'
                return self.moveStep(step)
        elif self.heading == 'E':
            if str(point).startswith('L'):
                self.heading = 'N'
                return self.moveStep(step)
            else:
                self.heading = 'S'
                return self.moveStep(step)
        elif self.heading == 'V':
            if str(point).startswith('L'):
                self.heading = 'S'
                return self.moveStep(step)
            else:
                self.heading = 'N'
                return self.moveStep(step)
                
        
    def moveStep(self, steps = 0):
        while steps != 0:
            if self.heading == 'N':
                self.y = self.y + 1
            elif self.heading == 'E':
                self.x = self.x + 1
            elif self.heading == 'S':
                self.y = self.y - 1
            elif self.heading == 'V':
                self.x = self.x - 1
            
            if self.before:
                if self.pointArr.count((self.x, self.y)) > 0:
                    return True
                else:
                    print 'x {0}, y {1}'.format(self.x, self.y)
                    self.pointArr.append((self.x, self.y))
            steps = steps - 1

        return False

    def getDistance(self):
        return abs(self.x) + abs(self.y)
    
def main():
    print('Start StreetGrid')
    
    test1 = ['R2', 'L3']
    grid1 = StreetGrid()
    for point in test1:
        grid1.move(point)
    print 'Grid 1: {0}'.format(grid1.getDistance())
 
    test2 = ['R2', 'R2', 'R2']
    grid2 = StreetGrid()
    for point in test2:
        grid2.move(point)
    print 'Grid 2: {0}'.format(grid2.getDistance())
 
    test3 = ['R5', 'L5', 'R5', 'R3']
    grid3 = StreetGrid()
    for point in test3:
        grid3.move(point)
    print 'Grid 3: {0}'.format(grid3.getDistance())
 
    test4 = ['L5', 'R1', 'R3', 'L4', 'R3', 'R1', 'L3', 'L2', 'R3', 'L5', 
             'L1', 'L2', 'R5', 'L1', 'R5', 'R1', 'L4', 'R1', 'R3', 'L4', 
             'L1', 'R2', 'R5', 'R3', 'R1', 'R1', 'L1', 'R1', 'L1', 'L2', 
             'L1', 'R2', 'L5', 'L188', 'L4', 'R1', 'R4', 'L3', 'R47', 'R1', 
             'L1', 'R77', 'R5', 'L2', 'R1', 'L2', 'R4', 'L5', 'L1', 'R3', 'R187', 
             'L4', 'L3', 'L3', 'R2', 'L3', 'L5', 'L4', 'L4', 'R1', 'R5', 
             'L4', 'L3', 'L3', 'L3', 'L2', 'L5', 'R1', 'L2', 'R5', 'L3', 
             'L4', 'R4', 'L5', 'R3', 'R4', 'L2', 'L1', 'L4', 'R1', 'L3', 
             'R1', 'R3', 'L2', 'R1', 'R4', 'R5', 'L3', 'R5', 'R3', 'L3', 
             'R4', 'L2', 'L5', 'L1', 'L1', 'R3', 'R1', 'L4', 'R3', 'R3', 
             'L2', 'R5', 'R4', 'R1', 'R3', 'L4', 'R3', 'R3', 'L2', 'L4', 
             'L5', 'R1', 'L4', 'L5', 'R4', 'L2', 'L1', 'L3', 'L3', 'L5', 
             'R3', 'L4', 'L3', 'R5', 'R4', 'R2', 'L4', 'R2', 'R3', 'L3', 
             'R4', 'L1', 'L3', 'R2', 'R1', 'R5', 'L4', 'L5', 'L5', 'R4', 
             'L5', 'L2', 'L4', 'R4', 'R4', 'R1', 'L3', 'L2', 'L4', 'R3']
    grid4 = StreetGrid()
    for point in test4:
        grid4.move(point)
    print 'Grid 4: {0}'.format(grid4.getDistance())
    
    test5 = ['R8', 'R4', 'R4', 'R8']
    grid5 = StreetGrid(True)
    for point in test5:
        if grid5.move(point):
            break
    print 'Grid 5: {0}'.format(grid5.getDistance())

    grid6 = StreetGrid(True)
    for point in test4:
        if grid6.move(point):
            break
    print 'Grid 6: {0}'.format(grid6.getDistance())

if __name__ == '__main__':
    main()