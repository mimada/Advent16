#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/1
#

class LikeARogue:
    def __init__(self, start = '', rows = 0):
        self.row = [start]
        self.rowCnt = rows
        self.count = 0
        
        self.pattern = {'...':'.', '^..':'^', '.^.':'.', '..^':'^', 
                        '.^^':'^', '^.^':'.', '^^.':'^', '^^^':'.'}
        
    def creaste(self):
        l = self.row[0].__len__()
        for r in range(1, self.rowCnt):
            row = []
            
            for n in range(l):
                if n == 0:
                    k = '.' + self.row[r-1][n:n+2]
                elif n == l-1:
                    k = self.row[r-1][n-1:n+1] + '.'
                else:
                    k = self.row[r-1][n-1:n+2]
                
                row.append(self.pattern[k])
            
            self.row.append(''.join(row))
        for r in self.row:
            self.count = self.count + r.count('.')
            print r
    
    def getCount(self):
        return self.count
    
def main():
    print('Start LikeARogue')
    
#     c = LikeARogue('..^^.', 3)
#     c = LikeARogue('.^^.^.^^^^', 10)
#     c = LikeARogue('.^^..^...^..^^.^^^.^^^.^^^^^^.^.^^^^.^^.^^^^^^.^...^......^...^^^..^^^.....^^^^^^^^^....^^...^^^^..^', 40)
    c = LikeARogue('.^^..^...^..^^.^^^.^^^.^^^^^^.^.^^^^.^^.^^^^^^.^...^......^...^^^..^^^.....^^^^^^^^^....^^...^^^^..^', 400000)
    c.creaste()
    print 'Number of safe tiles:', c.getCount()
 

if __name__ == '__main__':
    main()