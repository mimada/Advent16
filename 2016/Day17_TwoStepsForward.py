#
# 119804-20161201-18fba1ee
# http://adventofcode.com/2016/day/17

#########
#S| | | #
#-#-#-#-#
# | | | #
#-#-#-#-#
# | | | #
#-#-#-#-#
# | | |  
####### V#


import md5

class TwoStepsForward:
    def __init__(self):
        self.count = 0
        
    def getCount(self):
        return self.count
    
def main():
    print('Start TwoStepsForward')
    
    moves1 = []

    c = TwoStepsForward('ihgpwlah')    # DDRRRD
#     c = TwoStepsForward('kglvqrro')    # DDUDRLRRUDRD
#     c = TwoStepsForward('ulqzkmiv')    # DRURDRUDDLLDLUURRDULRLDUUDDDRR
#     c = TwoStepsForward('ioramepc')    # ?
    c.move(moves1[0])
    print 'KeyPad 1 code:', c.getCount()
 

if __name__ == '__main__':
    main()