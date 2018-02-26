import math


class Matrix(object):

    #m1 * m2 -> m2
    @staticmethod
    def mult( m1, m2 ):
        pass
    
    def __init__(self, rows = 4, cols = 4):
        m = []
        for c in range( cols ):
            m.append( [] )
            for r in range( rows ):
                m[c].append( 0 )
        return m

    def print_matrix( self ):
        pass

    def ident( self ):
        pass




