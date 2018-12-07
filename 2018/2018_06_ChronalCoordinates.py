#
# Mikael Martensson
# http://adventofcode.com/2018/day/6
#

class ChronalCoordinates:

    def getDataFromFile(self, fileName):
        xy = {}

        with open(fileName) as fi:
            for line in fi:
                s = line.strip().split(', ')
                x = int(s[0])
                y = int(s[1])
                key = '{0}:{1}'.format(x,y)
                xy[key] = {}
                xy[key]['x'] = x
                xy[key]['y'] = y
                xy[key]['closest'] = []

        return xy

    def getMinAndMaxValues(self, xy):
        xmin = 0
        xmax = 0
        ymin = 0
        ymax = 0
        first = True
        for key in xy:
            if first:
                xmin = xy[key]['x']
                xmax = xy[key]['x']
                ymin = xy[key]['y']
                ymax = xy[key]['y']
                first = False
                continue
            if xmin > xy[key]['x']:
                xmin = xy[key]['x']
            if xmax < xy[key]['x']:
                xmax = xy[key]['x']
            if ymin > xy[key]['y']:
                ymin = xy[key]['y']
            if ymax < xy[key]['y']:
                ymax = xy[key]['y']
        return xmin, xmax, ymin, ymax


    def getLargestArea(self, fileName):
        xy = self.getDataFromFile(fileName)
        xmin, xmax, ymin, ymax = self.getMinAndMaxValues(xy)

        finiteList = xy.keys()

        for x in range(xmin - 1, xmax + 1):
            for y in range(ymin - 1, ymax + 1):
                pos = '{0}:{1}'.format(x,y)
                minStep= xmax + ymax
                minKey = ''
                equal = False
                for k in xy:
                    s = abs(xy[k]['x']-x) + abs(xy[k]['y']-y)
                    if s < minStep:
                        minStep = s
                        minKey = k
                        equal = False
                    elif s == minStep:
                        equal = True
                if not equal:
                    xy[minKey]['closest'].append(pos)
                    if x == xmin or x == xmax or y == ymin or y == ymax:
                        if finiteList.count(minKey) > 0:
                            finiteList.remove(minKey)
        largestArea = 0
        for k in finiteList:
            if largestArea < len(xy[k]['closest']):
                largestArea = len(xy[k]['closest'])
        return largestArea

    def getRegionSize(self, fileName, maxDistance):
        xy = self.getDataFromFile(fileName)
        xmin, xmax, ymin, ymax = self.getMinAndMaxValues(xy)
        region = []

        for x in range(xmin - 1, xmax + 1):
            for y in range(ymin - 1, ymax + 1):
                sum = 0
                for k in xy:
                    sum = sum + abs(xy[k]['x']-x) + abs(xy[k]['y']-y)
                if sum < maxDistance:
                    region.append('{0}:{1}'.format(x,y))

        return len(region)


def main():
    print('Start Chronal Coordinates')

    c = ChronalCoordinates()

    print c.getLargestArea('2018_06_Input_test_1.txt')
    print c.getLargestArea('2018_06_Input.txt')

    print c.getRegionSize('2018_06_Input_test_1.txt', 32)
    print c.getRegionSize('2018_06_Input.txt', 10000)


if __name__ == '__main__':
    main()