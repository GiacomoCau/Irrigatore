from datetime import time as hm
def sm(s, m): return [s, m]

progs = {
	'a': [['every', 1], [hm(9,30), hm(11,30)], [sm(2,4), sm(1,6)]],
	'b': [['even'], [hm(9,30)], [sm(3,5), sm(4,2)]],
	'c': [['dow', 1, 1, 0, 1, 1, 0, 1], [hm(10,30)], [sm(9,1), sm(1,5)]],
}
