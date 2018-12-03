#
# Mikael Martensson
# http://adventofcode.com/2018/day/1
#

class NoMatterHowYouSliceIt:
    
    def getOverlap(self, fileName):

        grid = []
        idList = []
        # init grid
        for i1 in range(1100):
            grid.append([])
            for i2 in range(1100):
                grid[i1].append([])

        with open(fileName) as fi:
            for line in fi:
                # interpret line
                s1 = line.split()
                xy = s1[2].split(',')
                wh = s1[3].split('x')
                x = int(xy[0])
                y = int(xy[1].strip(':'))
                w = int(wh[0])
                h = int(wh[1])
                id = s1[0].strip('#')
                idList.append(id)

                # fill grid
                for py in range(y, y + h):
                    for px in range(x, x + w):
                        grid[py][px].append(id)

        # Check overlap
        overlap = 0
        for i1 in range(1100):
            for i2 in range(1100):
                if len(grid[i1][i2]) > 1:
                    overlap = overlap + 1
                    for i in grid[i1][i2]:
                        if i in idList:
                            idList.remove(i)

        return overlap, idList

    def getProductId(self, fileName):

        lines = []
        with open(fileName) as fi:
            for line in fi:
                lines.append(line.strip())
        lines.sort()
        for i in range(len(lines) - 1):
            errors = []
            for ii in range(len(lines[i])):
                if not lines[i][ii] == lines[i+1][ii]:
                    errors.append(ii)
            if len(errors) == 1:
                print lines[i], lines[i+1]
                print lines[i][:errors[0]] + lines[i][errors[0]+1:]




def main():
    print('Start No Matter How You Slice It')
    
    c = NoMatterHowYouSliceIt()
    
    print c.getOverlap('2018_03_Input_test_1.txt')
    print c.getOverlap('2018_03_Input.txt')
    
#    print c.getProductId('2018_03_Input_test_2.txt')
#    print c.getProductId('2018_03_Input.txt')

if __name__ == '__main__':
    main()