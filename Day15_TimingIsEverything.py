#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/1
#

class TimeSlot:
    def __init__(self, start):
        self.start = start
        self.discs = self.start
        
    def reset(self):
        self.discs = self.start
        
    def press(self, time):
        start = 1
        stop = self.discs.__len__() + 1
        for n in range(start, stop):
            a = n + time + self.discs[n]['pos']
            b = self.discs[n]['max']
            print n, a, b, 
            if (n + time + self.discs[n]['pos']) % self.discs[n]['max'] == 0:
                print 'OK'
            else:
                print 'NOK'
                return False
        return True
    
def main():
    print('Start Time is everything')
    
    start0 = {1:{'pos':4, 'max':5}, 2:{'pos':1, 'max':2}}

    start1 = { 1:{'pos':15, 'max':17}, 
               2:{'pos':2, 'max':3},
               3:{'pos':4, 'max':19},
               4:{'pos':2, 'max':13},
               5:{'pos':2, 'max':7},
               6:{'pos':0, 'max':5}
              }
    
    start2 = { 1:{'pos':15, 'max':17}, 
               2:{'pos':2, 'max':3},
               3:{'pos':4, 'max':19},
               4:{'pos':2, 'max':13},
               5:{'pos':2, 'max':7},
               6:{'pos':0, 'max':5},
               7:{'pos':0, 'max':11}
              }
    
    c = TimeSlot(start2)
    c.reset()
    
    cont = True
    t = 0
    while cont:
        c.reset()
        capsule = c.press(t)
        if capsule:
            cont = False
        else:
            t = t + 1
        
    print 'Time:', t
 

if __name__ == '__main__':
    main()