from datetime import time as hm
def sm(s, m): return [s, m]

giorni = {'c':['dow', 1, 1, 0, 1, 1, 0, 1], 'b':['even'], 'a':['every', 1]}
orari = {'c':[hm(10,30)], 'b':[hm(9,30)], 'a':[hm(9,30), hm(11,30)]}
durate = {'c':[sm(9,1), sm(1,5)], 'b':[sm(4,2), sm(3,5)], 'a':[sm(2,4), sm(1,6)]}
