#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/1
#

class Maze:
    def __init__(self, x, y, fn):
        self.x = x
        self.y = y
        self.fn = fn
        self.maze = []
        self.graph = {}
        
        for yp in range(self.y):
            self.maze.append([])
            for xp in range(self.x):
                n = xp*xp + 3*xp + 2*xp*yp + yp + yp*yp + self.fn
                if str(bin(n))[2:].count('1') % 2 == 0:
                    self.maze[yp].append('.')
                else:
                    self.maze[yp].append('#')
        
    def printMaze(self, p = []):
        for yp in range(self.y):
            for xp in range(self.x):
                if p.count((xp, yp)) > 0:
                    self.maze[yp][xp] = '0'
        for row in self.maze:
            print ''.join(row)
    
    def printGraph(self):
        keys = self.graph.keys()
        keys.sort()
        for key in keys:
            print key, ':',self.graph[key]
    
    def evaluateGraph(self):
        for yp in range(self.y):
            for xp in range(self.x):
                if self.maze[yp][xp] == '#':
                    continue
                self.graph[(xp, yp)] = []
                if xp+1 < self.x and self.maze[yp][xp+1] == '.':
                    self.graph[(xp, yp)].append((xp+1, yp))
                if yp+1 < self.y and self.maze[yp+1][xp] == '.':
                    self.graph[(xp, yp)].append((xp, yp+1))
                if xp-1 >= 0 and self.maze[yp][xp-1] == '.':
                    self.graph[(xp, yp)].append((xp-1, yp))
                if yp-1 >= 0 and self.maze[yp-1][xp] == '.':
                    self.graph[(xp, yp)].append((xp, yp-1))
        
    
    def findShortestPath(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not self.graph.has_key(start):
            return None
        shortest = None
        for node in self.graph[start]:
            if node not in path:
                newpath = self.findShortestPath(node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest
    
    def findAllPaths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not self.graph.has_key(start):
            return []
        paths = []
        for node in self.graph[start]:
            if node not in path:
                newpaths = self.findAllPaths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
    
    
    
def main():
    print('Start Maze')
    
#     c = Maze(10, 7, 10)
    c = Maze(50, 42, 1352)
    c.evaluateGraph()
    c.printGraph()
    
#     p1 = c.findShortestPath((1,1), (7,4))
#     p1 = c.findShortestPath((1,1), (31,39))
    p1 = c.findShortestPath((1,1), (27,21))

#     p2 = c.findShortestPath((1,1), (7,4))
#     p2 = c.findAllPaths((1,1), (31,39))

    
    c.printMaze(p1)
    print 'Shortest path is {0} steps'.format(p1.__len__()-1)
 

if __name__ == '__main__':
    main()